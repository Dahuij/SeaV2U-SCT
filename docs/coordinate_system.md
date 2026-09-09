# Coordinate Systems

## Native dataset convention

SeaV2U-SCT follows AirSim-style conventions:

- World: NED, in meters (`+X` north, `+Y` east, `+Z` down).
- Vehicle local: FRD (`+X` forward, `+Y` right, `+Z` down).
- LiDAR local: sensor-local FRD (`+X` forward, `+Y` right, `+Z` down).
- Camera local: `+X` forward, `+Y` right, `+Z` down.
- Image pixels: `+u` right, `+v` down, origin at the top-left.

Positions are in meters. Quaternions are serialized as `w, x, y, z`. Euler angles, when present, are in degrees.

## Transforming LiDAR points to world

For a sensor-local point `p_lidar`, the metadata defines the transform as:

```text
p_world = R_world_vehicle × (R_vehicle_lidar × p_lidar + t_vehicle_lidar)
          + t_world_vehicle
```

Use the calibrated local sensor pose and the per-frame vehicle pose. Do not assume that the USV has zero roll or pitch.

## SeaCrossTrack / CenterPoint conversion

SeaCrossTrack's internal LiDAR convention is FLU. The basic point-axis conversion from native FRD is:

```text
(x, y, z) -> (x, -y, -z)
```

The accompanying conversion code also handles:

- pose quaternions and rotation matrices from NED/FRD to FLU;
- world boxes transformed into UAV or USV LiDAR-local coordinates;
- the MMDetection3D LiDAR yaw convention;
- CenterPoint bottom-center versus gravity-center box origins;
- zero-padded NPY point rows;
- NPY XYZ to `float32` XYZI, with intensity set to zero.

CenterPoint represents yaw-only 3D boxes. Exporting USV-local targets therefore approximates full roll/pitch boxes. Retain the native world-frame corners for full-pose geometric checks.

## Practical checks

Before training or evaluation:

1. Verify that projected 3D boxes align with RGB images.
2. Visualize UAV and USV point clouds after conversion.
3. Check several nonzero-roll/pitch USV frames.
4. Confirm that quaternion order is not interpreted as `x, y, z, w`.
5. Filter NPY padding before computing point counts or range statistics.
