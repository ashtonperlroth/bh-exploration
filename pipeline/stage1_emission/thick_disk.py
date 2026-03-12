"""
Stage 1: Analytical accretion disk emission model.

Defines the 3D emissivity field around a black hole.
First version: geometrically thick disk (Polish doughnut) around a Schwarzschild BH.

The emission field is a function j(r, θ, φ) → emissivity at each point,
where coordinates are Boyer-Lindquist. The temperature / emissivity profile
follows a simple power-law model that captures the qualitative features
without requiring full GRMHD.

References:
    - Abramowicz, Jaroszynski & Sikora (1978) — Polish doughnut model
    - Moscibrodzka et al. (2016) — GRMHD-based emission for Sgr A*
"""

import numpy as np
from dataclasses import dataclass


@dataclass
class DiskParams:
    """Parameters for a geometrically thick accretion disk."""
    r_in: float = 6.0        # Inner edge (ISCO for Schwarzschild), in M
    r_out: float = 20.0       # Outer edge, in M
    r_peak: float = 12.0      # Peak emissivity radius, in M
    h_over_r: float = 0.3     # Disk aspect ratio (height / radius)
    emissivity_index: float = -2.0  # Power-law falloff exponent
    M: float = 1.0            # Black hole mass (geometric units)


def emissivity_field(r: np.ndarray, theta: np.ndarray, params: DiskParams) -> np.ndarray:
    """
    Compute emissivity j(r, θ) for a thick disk model.

    Args:
        r: Radial coordinate array (Boyer-Lindquist), in units of M.
        theta: Polar angle array, in radians.
        params: Disk parameters.

    Returns:
        Emissivity at each (r, θ) point. Zero outside the disk.
    """
    # Distance from midplane in units of local scale height
    z = r * np.abs(np.cos(theta))
    H = params.h_over_r * r
    vertical_profile = np.exp(-0.5 * (z / H) ** 2)

    # Radial profile: power-law with peak and cutoffs
    radial = (r / params.r_peak) ** params.emissivity_index
    radial *= np.exp(-((r - params.r_peak) / (params.r_out - params.r_peak)) ** 2)

    # Mask: zero inside ISCO and outside disk
    mask = (r >= params.r_in) & (r <= params.r_out)

    return radial * vertical_profile * mask


def sample_emission_volume(params: DiskParams,
                           n_r: int = 128,
                           n_theta: int = 64,
                           n_phi: int = 128) -> dict:
    """
    Sample the emission field on a 3D grid in Boyer-Lindquist coordinates.

    Returns:
        Dict with 'r', 'theta', 'phi' coordinate arrays and 'emissivity' volume.
    """
    r = np.linspace(params.r_in * 0.8, params.r_out * 1.2, n_r)
    theta = np.linspace(0, np.pi, n_theta)
    phi = np.linspace(0, 2 * np.pi, n_phi)

    R, Theta, Phi = np.meshgrid(r, theta, phi, indexing='ij')
    J = emissivity_field(R, Theta, params)

    return {'r': R, 'theta': Theta, 'phi': Phi, 'emissivity': J}


if __name__ == '__main__':
    params = DiskParams()
    vol = sample_emission_volume(params)
    print(f"Emission volume shape: {vol['emissivity'].shape}")
    print(f"Max emissivity: {vol['emissivity'].max():.4f}")
    print(f"Non-zero fraction: {(vol['emissivity'] > 1e-6).mean():.2%}")
