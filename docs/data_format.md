# Data Format

## Frame identifiers

Frames use six-digit, zero-padded identifiers such as `000000`. Files with the same frame identifier across modalities belong to the same synchronized logical frame.

## Images

RGB and semantic-segmentation images are 1280 × 720 PNG files.

- UAV cameras: `down` and `front_oblique`.
- USV cameras: `left`, `middle`, and `right`.
- Pixel coordinates use origin at the top-left, `u` increasing right, and `v` increasing down.
- Camera calibration uses a pinhole model with no distortion in the current snapshot.

## LiDAR

Each `UAV/ouster/<frame>.npy` and `USV/ouster/<frame>.npy` file is a NumPy `float32` array with shape `(N, 3)` and XYZ columns in sensor-local coordinates. Current full scans allocate 65,536 rows; consumers should filter zero-padding when converting the data.

The matching `<frame>.json` contains:

- vehicle and LiDAR names;
- capture timestamp and point count;
- sensor world pose and calibrated local pose;
- point-frame and transform declarations;
- the relative path to the `.npy` payload.

Intensity is not present in the source NPY. SeaCrossTrack's CenterPoint conversion writes XYZI with intensity set to zero.

## Calibration

`calibration/cameras.json` stores per-camera extrinsics, intrinsics, capture settings, and coordinate-system declarations. `calibration/lidars.json` stores LiDAR extrinsics, data frame, channel count, rotation rate, range, and vertical/horizontal field of view. `settings_snapshot.json` records the capture configuration.

## Poses

- `UAV/pose/<frame>.json` and `USV/pose/<frame>.json` store commanded and actual platform poses plus sensor poses.
- `cooperative/poses/<frame>.json` stores the synchronized commanded/actual state shared across agents.
- Orientations are quaternions ordered as `w, x, y, z`; roll, pitch, and yaw in degrees are included where available.

## 3D labels

`cooperative/labels_3d/<frame>.json` uses schema `seav2u.labels_3d` and includes:

- `objects`: instance identity, class, segmentation identity, world pose, and `box3d_world`;
- `box3d_world.center`: XYZ center in meters;
- `box3d_world.size_lwh_m`: length, width, and height in meters;
- `box3d_world.corners`: eight world-frame corners;
- `views`: per-camera projections, visibility, 2D box, truncation, and occlusion;
- `lidar_views`: per-LiDAR point support, range, occlusion diagnostics, and eligibility;
- `training_eligible` and `annotation_decision` fields for modality-aware filtering.

`cooperative/labels_2d/<frame>.json` is a compact per-camera view of visible-pixel boxes and eligibility decisions. `cooperative/labels/<frame>.json` preserves capture-time pose and placeholder label information used by processing.

## Timing and sequence metadata

- `meta.json`: sequence identity, route, motion, environment, sensor configuration, frame count, and processing provenance.
- `processing.json`: processing completion and QA status.
- `timing/frame_times.jsonl`: one timing record per frame.
- `timing/summary.json`: capture frequency, duration, scan strategy, and stop reason.

JSON files may include additional diagnostic fields. Parsers should ignore unknown fields for forward compatibility.
