"""
Stage 2: General-relativistic ray-tracing to generate training views.

Traces photon geodesics through the Schwarzschild (or Kerr) metric,
integrating the emission field from Stage 1 along each ray to produce
synthetic images from arbitrary camera positions.

First version: Schwarzschild metric (a=0), numerical integration of
null geodesics using the effective potential formulation.

The output is a set of ~100-200 PNG images with known camera poses,
ready to feed into 3DGS training (Stage 3).

References:
    - Luminet (1979) — Image of a spherical black hole with thin accretion disk
    - Levis et al. (2022) — bhnerf: neural radiance fields for black holes
"""

import numpy as np
from dataclasses import dataclass
from pathlib import Path

# TODO: Import from stage1
# from pipeline.stage1_emission.thick_disk import DiskParams, emissivity_field


@dataclass
class Camera:
    """Camera specification in Boyer-Lindquist coordinates."""
    r: float            # Radial distance from BH, in M
    theta: float        # Polar angle (0 = pole, π/2 = equator)
    phi: float          # Azimuthal angle
    fov_deg: float = 10.0   # Field of view in degrees
    resolution: int = 512    # Image resolution (square)


def fibonacci_sphere(n_points: int, r: float = 100.0) -> list[Camera]:
    """
    Distribute cameras on a sphere using Fibonacci spiral.

    Avoids clustering at poles, gives nearly uniform coverage.
    """
    cameras = []
    golden_ratio = (1 + np.sqrt(5)) / 2

    for i in range(n_points):
        theta = np.arccos(1 - 2 * (i + 0.5) / n_points)
        phi = 2 * np.pi * i / golden_ratio
        cameras.append(Camera(r=r, theta=theta, phi=phi))

    return cameras


def trace_ray(alpha: float, beta: float, camera: Camera, metric: str = 'schwarzschild') -> dict:
    """
    Trace a single photon ray from camera pixel (alpha, beta) back to the emission region.

    Args:
        alpha: Horizontal impact parameter on camera screen.
        beta: Vertical impact parameter on camera screen.
        camera: Camera pose.
        metric: 'schwarzschild' or 'kerr'.

    Returns:
        Dict with ray path and integrated intensity.
    """
    # TODO: Implement geodesic integration
    # For Schwarzschild, use effective potential:
    #   (dr/dλ)² = E² - V_eff(r, L)
    #   V_eff = (1 - 2M/r)(L²/r² + μ²)
    # where μ=0 for null geodesics
    raise NotImplementedError("Geodesic integration not yet implemented")


def render_view(camera: Camera, emission_params: dict, metric: str = 'schwarzschild') -> np.ndarray:
    """
    Render a full image from a camera position by tracing all pixel rays.

    Returns:
        HxW numpy array of integrated intensities.
    """
    # TODO: Vectorize ray-tracing across all pixels
    raise NotImplementedError("Full rendering not yet implemented")


def generate_training_views(n_views: int = 150,
                            output_dir: str = 'data/training_views',
                            metric: str = 'schwarzschild') -> None:
    """
    Generate a full set of training views and save with camera metadata.

    Saves:
        - {output_dir}/images/  — PNG images
        - {output_dir}/cameras.json — camera poses + intrinsics (for 3DGS)
    """
    output_path = Path(output_dir)
    (output_path / 'images').mkdir(parents=True, exist_ok=True)

    cameras = fibonacci_sphere(n_views)

    # TODO: Render each view and save
    # For each camera, render_view() → save PNG + record pose
    raise NotImplementedError("Training view generation not yet implemented")


if __name__ == '__main__':
    cameras = fibonacci_sphere(150)
    print(f"Generated {len(cameras)} camera positions")
    print(f"Theta range: [{min(c.theta for c in cameras):.2f}, {max(c.theta for c in cameras):.2f}]")
    print(f"Camera distance: {cameras[0].r} M")
