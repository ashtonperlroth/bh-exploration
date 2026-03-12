#!/usr/bin/env python3
"""
Train 3D Gaussian Splatting from ray-traced training views.

Usage:
    python scripts/train_splat.py --data data/training_views --output data/splats/blackhole.ply
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


def main():
    parser = argparse.ArgumentParser(description='Train 3DGS on BH training views')
    parser.add_argument('--data', type=str, required=True,
                        help='Path to training views directory')
    parser.add_argument('--output', type=str, default='data/splats/blackhole.ply',
                        help='Output .ply file path')
    parser.add_argument('--iterations', type=int, default=30_000,
                        help='Training iterations')
    parser.add_argument('--sh_degree', type=int, default=3,
                        help='Spherical harmonics degree')
    args = parser.parse_args()

    print(f"Training 3D Gaussian Splatting")
    print(f"  Data:       {args.data}")
    print(f"  Output:     {args.output}")
    print(f"  Iterations: {args.iterations:,}")
    print(f"  SH degree:  {args.sh_degree}")
    print()

    # TODO: Wire up Stage 3
    # from pipeline.stage3_splatting.train import prepare_colmap_format, train_splat
    print("Not yet implemented — Stage 3 pipeline in progress.")


if __name__ == '__main__':
    main()
