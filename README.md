# Lotus2Recomp — early research

Research toward a native Apple Silicon/macOS port of **Lotus Turbo Challenge II** (Amiga, 1991), by translating the original 68000 program and implementing the hardware services it uses.

**This is not a playable port, a finished recompiler, or a release.** No native Lotus 2 application has been built yet. Current contents are a read-only disk inspection utility and initial technical findings. No promise of feature or platform completeness is made.

## Current progress

- Examined eight user-supplied standard 880 KiB ADF variants.
- Selected the Company (CPY) version without a trainer as the initial reference.
- Confirmed valid bootblock checksums and a custom loader rather than a normal AmigaDOS file tree.
- Identified the first boot read: disk offset `0xD3200`, length `0x7600`, destination `0x60000`, followed by a jump to that destination.
- The final game entry point, decompression format, code coverage, graphics and sound behavior still need analysis.

## Inspect your own disk

Python 3, standard library only:

```sh
python3 inspect_adf.py /path/to/your/adfs --output inventory.json
```

The utility reads standard-size ADFs, reports hashes and bootblock checksums, checks the expected root block, and searches for a few common packing signatures. It does not run or modify the game and is not a compatibility test for a future port.

## Next steps

1. Understand and unpack the initial loader, then identify the main program and its disk reads.
2. Establish a reproducible execution and rendering baseline.
3. Build and validate a game-specific 68000 translation and runtime.
4. Package and test a native ARM64 macOS application.

Widescreen and other enhancements are future possibilities, not implemented features.

## References and credits

The original game is by **Magnetic Fields / Gremlin**. This is an independent research project and is not affiliated with or endorsed by the original authors.

- [James Pond 2 RoboCod recompilation](https://github.com/griches/JamesPond2RobocodRecomp): inspiration for the approach; its game-specific extractor cannot simply be reused with Lotus 2. No code from that project is included here.
- [WHDLoad Lotus 2 installer](https://www.whdload.de/games/Lotus2.html), by Wepl, Mr.Larmer, StingRay and JOTD: public technical reference for versions, loading and decompression. Its source and binaries are not included in this repository.

## Game data and licensing

Bring your own game disk. **No ADFs, game executables, extracted game code, graphics, music, Kickstart ROMs or copyrighted game data are included.** Do not commit those files.

The original inspection utility in this repository is licensed under MIT; see [LICENSE](LICENSE). That license does not apply to Lotus 2, its data, or third-party reference material. Any future third-party code must retain its own authorship and license notices.
