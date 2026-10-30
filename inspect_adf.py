#!/usr/bin/env python3
"""Inspect user-supplied Lotus 2 ADF images without running or modifying them."""
import argparse,hashlib,json,re,struct
from pathlib import Path

def inspect(path):
    data=path.read_bytes()
    if len(data)!=901120:
        raise ValueError('Expected an 880 KiB standard DD ADF')
    total=0
    for word in struct.unpack('>256I',data[:1024]):
        previous=total;total=(total+word)&0xffffffff
        if total<previous:total=(total+1)&0xffffffff
    root=data[880*512:881*512]
    return {'name':path.name,'size':len(data),'sha256':hashlib.sha256(data).hexdigest(),
        'boot_signature':data[:4].hex(),'boot_checksum_valid':total==0xffffffff,
        'root_block_is_amigados':struct.unpack_from('>I',root)[0]==2 and struct.unpack_from('>i',root,508)[0]==1,
        'packing_markers':{s.decode('ascii'): [m.start() for m in re.finditer(re.escape(s),data)] for s in (b'PP20',b'RNC',b'ICE!',b'Impl')}}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('directory',type=Path);ap.add_argument('--output',type=Path);a=ap.parse_args()
    result=[inspect(p) for p in sorted(a.directory.glob('*.adf'))]
    encoded=json.dumps(result,indent=2,ensure_ascii=False)+'\n'
    if a.output:a.output.write_text(encoded)
    else:print(encoded,end='')
