# SeaV2U-SCT

**SeaV2U-SCT: SeaCrossTrack Study Subset** is the study-specific subset of SeaV2U used in the SeaCrossTrack paper for cooperative UAV–USV 3D object detection and tracking.

> Release status: the repository metadata and validation tools are available. The v1.0 data archives have not yet been attached to a GitHub Release.

## Overview

SeaV2U-SCT contains synchronized observations from an unmanned aerial vehicle (UAV) and an unmanned surface vehicle (USV) in three simulated maritime environments. It includes RGB images, semantic-segmentation images, LiDAR point clouds, platform and sensor poses, calibration, 2D annotations, 3D annotations, and timing metadata.

Only the sequences used by the SeaCrossTrack study are in scope. Future SeaV2U scenes, classes, weather conditions, and sequences are intentionally excluded.

## Snapshot statistics

| Item | Value |
|---|---:|
| Sequences | 12 |
| Frames | 2,351 |
| Files | 63,609 |
| Uncompressed size | 29,954,218,380 bytes (27.9 GiB) |
| Split | 8 train / 2 validation / 2 test sequences |
| Environments | channel, lake, port |
| Platforms | UAV and USV |
| Capture rate | 5 Hz |

The six object classes are:

```text
cargo_medium
cargo_small
fishing_boat
passenger_ship
sailboat
small_craft
```

The paper-facing evaluation snapshot contains 1,526/480/345 platform frames in train/validation/test. The corresponding eligible 3D-box counts are 7,151/911/1,913 for UAV LiDAR and 10,279/1,991/3,019 for USV LiDAR.

## Data splits

The split is sequence-level to prevent neighboring frames from leaking across train, validation, and test sets.

- [Train split](splits/train.txt): 8 sequences, 1,526 frames
- [Validation split](splits/val.txt): 2 sequences, 480 frames
- [Test split](splits/test.txt): 2 sequences, 345 frames
- [Sequence metadata](metadata/sequences.csv): scene, route, motion, weather, frame count, file count, and size

## Download

The full dataset is distributed as independent ZIP assets in the [SeaV2U-SCT v1.0 release](https://github.com/Dahuij/SeaV2U-SCT/releases/tag/v1.0):

```text
SeaV2U-SCT_v1.0_part01.zip
SeaV2U-SCT_v1.0_part02.zip
...
SHA256SUMS.txt
release_manifest.json
```

Each archive is kept below GitHub's per-asset limit and can be extracted independently into the same destination directory. Do not add the archives or extracted data to Git history.

After downloading all assets, verify them with:

```bash
python scripts/verify_dataset.py /path/to/SeaV2U-SCT \
  --checksums /path/to/SHA256SUMS.txt \
  --assets-root /path/to/downloaded/assets
```

## Expected layout

```text
SeaV2U-SCT/
├── <sequence>/
│   ├── meta.json
│   ├── processing.json
│   ├── calibration/
│   ├── cooperative/
│   │   ├── labels/
│   │   ├── labels_2d/
│   │   ├── labels_3d/
│   │   └── poses/
│   ├── timing/
│   ├── UAV/
│   │   ├── camera/
│   │   ├── ouster/
│   │   ├── pose/
│   │   └── segmentation/
│   └── USV/
│       ├── camera/
│       ├── ouster/
│       ├── pose/
│       └── segmentation/
└── ...
```

See [directory_structure.md](docs/directory_structure.md), [data_format.md](docs/data_format.md), and [coordinate_system.md](docs/coordinate_system.md) for details.

## Validation and release preparation

Validate an extracted dataset:

```bash
python scripts/verify_dataset.py /path/to/SeaV2U-SCT
```

Preview a release partition without writing archives:

```bash
python scripts/package_release.py /path/to/SeaV2U_processed /path/to/release --dry-run
```

Create deterministic, independently extractable ZIP assets and their checksums:

```bash
python scripts/package_release.py /path/to/SeaV2U_processed /path/to/release
```

## Citation

Please cite the SeaCrossTrack paper and this dataset release. Machine-readable citation metadata is provided in [CITATION.cff](CITATION.cff). Paper bibliographic details and a DOI will be added when available.

## License

Unless a third-party file states otherwise, SeaV2U-SCT is released under the [Creative Commons Attribution 4.0 International License](LICENSE). Attribution is required.

## Related project

SeaCrossTrack is the accompanying cooperative 3D object detection and tracking codebase. A public link will be added when that repository is released.
