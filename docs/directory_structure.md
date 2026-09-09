# Directory Structure

The released archives extract into one dataset root containing 12 sequence directories. A representative sequence is:

```text
<sequence>/
├── meta.json
├── processing.json
├── calibration/
│   ├── cameras.json
│   ├── lidars.json
│   └── settings_snapshot.json
├── cooperative/
│   ├── labels/<frame>.json
│   ├── labels_2d/<frame>.json
│   ├── labels_3d/<frame>.json
│   └── poses/<frame>.json
├── timing/
│   ├── frame_times.jsonl
│   ├── summary.json
│   └── ...
├── UAV/
│   ├── camera/
│   │   ├── down/<frame>.png
│   │   └── front_oblique/<frame>.png
│   ├── ouster/
│   │   ├── <frame>.npy
│   │   └── <frame>.json
│   ├── pose/<frame>.json
│   └── segmentation/
│       ├── down/<frame>.png
│       └── front_oblique/<frame>.png
├── USV/
│   ├── camera/
│   │   ├── left/<frame>.png
│   │   ├── middle/<frame>.png
│   │   └── right/<frame>.png
│   ├── ouster/
│   │   ├── <frame>.npy
│   │   └── <frame>.json
│   ├── pose/<frame>.json
│   └── segmentation/
│       ├── left/<frame>.png
│       ├── middle/<frame>.png
│       └── right/<frame>.png
└── qa/
    └── ...
```

The `qa/` subtree contains diagnostic overlays and sequence-level QA products. These files support inspection but are not model inputs.

Some empty compatibility directories such as `depth/` or `yaml/` may appear in the processed snapshot. Consumers should discover supported modalities from the actual files and calibration metadata rather than inferring availability from directory names alone.
