#!/usr/bin/env python3
"""
Generate ray-traced training views of a black hole accretion disk.

Usage:
    python scripts/generate_training_views.py --model thick_disk --metric schwarzschild --n_views 150
"""

import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))


def main():
    parser = argparse.ArgumentParser(description='Generate BH training views')
    parser.add_argument('--model', choices=['thick_disk', 'thin_disk'], default='thick_disk',
                        help='Emission model (default: thick_disk)')
    parser.add_argument('--metric', choices=['schwarzschild', 'kerr'], default='schwarzschild',
                        help='Spacetime metric (default: schwarzschild)')
    parser.add_argument('--spin', type=float, default=0.0,
                        help='BH spin parameter a/M, 0 to 1 (only for Kerr)')
    parser.add_argument('--n_views', type=int, default=150,
                        help='Number of training views to generate')
    parser.add_argument('--resolution', type=int, default=512,
                        help='Image resolution (square)')
    parser.add_argument('--output', type=str, default='data/training_views',
                        help='Output directory')
    args = parser.parse_args()

    print(f"Generating {args.n_views} training views")
    print(f"  Model:      {args.model}")
    print(f"  Metric:     {args.metric}" + (f" (a={args.spin})" if args.metric == 'kerr' else ''))
    print(f"  Resolution: {args.resolution}x{args.resolution}")
    print(f"  Output:     {args.output}")
    print()

    # TODO: Wire up Stage 1 + Stage 2
    # from pipeline.stage1_emission.thick_disk import DiskParams, sample_emission_volume
    # from pipeline.stage2_raytrace.raytrace import generate_training_views
    print("Not yet implemented — Stage 1+2 pipeline in progress.")


if __name__ == '__main__':
    main()
