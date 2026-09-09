# Dataset Card for SeaV2U-SCT

## Dataset summary

SeaV2U-SCT is a synchronized, simulation-derived maritime perception dataset for cooperative UAV–USV 3D object detection and multi-object tracking. It is the exact sequence subset used by the SeaCrossTrack study, rather than the planned full SeaV2U dataset.

## Intended uses

- Cooperative UAV–USV 3D object detection and tracking.
- Multi-view and multi-agent perception research.
- Sensor-fusion, coordinate-transformation, and synchronization studies.
- Reproduction and comparison of SeaCrossTrack experiments.

## Out-of-scope uses

- Claims about real-world deployment safety without additional validation.
- Maritime navigation or collision avoidance in operational systems.
- Evaluation of people, demographic groups, or personally identifiable behavior.
- Treating the subset as representative of all maritime environments.

## Composition

- 12 sequences and 2,351 synchronized frames.
- Three simulated environments: channel, lake, and port.
- UAV and USV RGB cameras, semantic-segmentation cameras, 32-channel LiDAR, poses, and calibration.
- Per-frame cooperative 2D and 3D annotations with visibility and training-eligibility metadata.
- Six vessel classes: `cargo_medium`, `cargo_small`, `fishing_boat`, `passenger_ship`, `sailboat`, and `small_craft`.
- Sunny, rainy, foggy, and snowy conditions; 500, 800, 1000, 1200, 1500, 2000, 2200, and 2300 time-of-day settings.

The authoritative sequence inventory is [metadata/sequences.csv](metadata/sequences.csv). The split files are under [splits/](splits/).

## Data collection and processing

The data were generated in an AirSim-style simulation with an Unreal Engine maritime environment. Each frame uses a stop-and-scan capture procedure: carrier poses are held while static LiDAR scan phases and sensor reads are completed. The processed dataset preserves sensor-local point clouds and provides calibrated sensor poses and world-frame annotations.

RGB and segmentation images are stored as PNG. LiDAR returns are stored as NumPy `float32` arrays. Structured metadata and annotations use JSON; frame timing uses JSON Lines.

## Annotation policy

3D object records include a world-frame oriented box, class, instance identity, per-camera projections, LiDAR visibility evidence, occlusion diagnostics, and modality-specific `training_eligible` decisions. Consumers should filter with the documented eligibility flags instead of assuming that every catalogued object is observable in every sensor.

## Splits

The 8/2/2 train/validation/test partition is sequence-level. Adjacent frames from the same sequence never cross split boundaries.

## Personal and sensitive information

The dataset is simulation-derived and is not intended to contain real people, real license plates, private communications, or other personally identifiable information.

## Limitations

- Simulation-to-real domain gap in appearance, dynamics, weather, water, and sensor noise.
- Only three environments and 12 study sequences are included.
- The class taxonomy is vessel-focused and does not cover the full maritime long tail.
- CenterPoint-compatible exports may use yaw-only boxes; USV roll and pitch therefore require an approximation at export time.
- LiDAR metadata are frame-level; there is no per-point timestamp or deskew metadata.
- Dataset scale and class balance reflect the SeaCrossTrack study subset, not a general maritime benchmark.

## Maintenance

Versioned data archives, a release manifest, and SHA-256 checksums will be attached to GitHub Releases. Corrections to documentation or metadata will be tracked in Git; any change to released data will use a new versioned release.

## License and citation

The dataset is licensed under CC BY 4.0. See [LICENSE](LICENSE) and [CITATION.cff](CITATION.cff).
