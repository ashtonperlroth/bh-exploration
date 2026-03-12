"""
Stage 3: Train 3D Gaussian Splatting against ray-traced training views.

Takes the multi-view images from Stage 2 and optimizes a set of 3D Gaussians
to reproduce them. Uses gsplat (nerfstudio) for fast training.

The physics is already baked into the training images — this stage is
standard 3DGS optimization, no GR required.

Output: a .ply file containing the optimized Gaussians.
"""

from pathlib import Path


def prepare_colmap_format(training_views_dir: str, output_dir: str) -> None:
    """
    Convert our camera poses + images into COLMAP-compatible format
    expected by most 3DGS implementations.

    Our cameras.json from Stage 2 → COLMAP cameras.txt, images.txt, points3D.txt
    """
    # TODO: Convert camera intrinsics/extrinsics to COLMAP format
    # 3DGS implementations typically expect COLMAP's sparse reconstruction format
    raise NotImplementedError


def train_splat(data_dir: str,
                output_path: str = 'data/splats/blackhole.ply',
                n_iterations: int = 30_000,
                sh_degree: int = 3) -> None:
    """
    Run 3DGS training using gsplat.

    Args:
        data_dir: Path to COLMAP-formatted training data.
        output_path: Where to save the final .ply file.
        n_iterations: Training iterations (30k is standard).
        sh_degree: Spherical harmonics degree for view-dependent color.
    """
    # TODO: Implement using gsplat or nerfstudio splatfacto
    # Key hyperparameters to tune:
    #   - densification interval and threshold
    #   - opacity reset interval
    #   - learning rates for position, color, opacity, scale, rotation
    raise NotImplementedError


if __name__ == '__main__':
    print("Stage 3: Gaussian Splatting training")
    print("Requires: training views from Stage 2 in data/training_views/")
    print("Run: python scripts/train_splat.py --data data/training_views")
