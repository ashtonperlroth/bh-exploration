# Black Hole Explorer

Interactive 3D visualization of a black hole accretion disk, rendered with [3D Gaussian Splatting](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) and explorable in real-time in the browser.

Think: the Event Horizon Telescope image, but you can fly around it.

![Status: In Development](https://img.shields.io/badge/status-in%20development-yellow)

## How It Works

The pipeline has four stages:

```
Emission Model → GR Ray-Tracing → Gaussian Splat Training → Web Viewer
   (Stage 1)       (Stage 2)          (Stage 3)              (Stage 4)
```

**Stage 1 — Generate 3D emission field.** Define an analytical accretion disk model (geometrically thick torus with temperature-dependent emissivity) around a Kerr or Schwarzschild black hole.

**Stage 2 — Ray-trace training views.** Render ~100–200 images from viewpoints on a sphere around the black hole using GR-aware ray-tracing (photon geodesics curve near the event horizon). This produces the photon ring, Doppler-boosted asymmetry, and central shadow.

**Stage 3 — Train 3D Gaussian Splatting.** Optimize a set of 3D Gaussians against the ray-traced training views. The physics is baked into the images — the splat optimizer just learns to reproduce them. Output: a `.ply` splat file.

**Stage 4 — Interactive web viewer.** Load the `.ply` into a browser-based Gaussian Splat renderer. Anyone with a URL can explore the black hole in real-time.

## Project Structure

```
bh-exploration/
├── pipeline/
│   ├── stage1_emission/     # Accretion disk emission models
│   ├── stage2_raytrace/     # GR ray-tracing to generate training views
│   ├── stage3_splatting/    # 3DGS training against ray-traced views
│   └── stage4_viewer/       # Browser-based splat viewer
├── data/
│   ├── training_views/      # Ray-traced images (gitignored)
│   └── splats/              # Trained .ply files (gitignored)
├── scripts/                 # Utility & automation scripts
├── docs/                    # Notes, references, derivations
├── requirements.txt         # Python dependencies (Stages 1–3)
└── package.json             # JS dependencies (Stage 4)
```

## Quickstart

### Prerequisites

- Python 3.10+
- NVIDIA GPU with CUDA 11.8+ (for Stages 2–3)
- Node.js 18+ (for Stage 4)

### Setup

```bash
git clone https://github.com/YOUR_USERNAME/bh-exploration.git
cd bh-exploration

# Python environment (Stages 1–3)
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Web viewer (Stage 4)
cd pipeline/stage4_viewer
npm install
```

### Run the pipeline

```bash
# Stage 1+2: Generate ray-traced training views
python scripts/generate_training_views.py --model thick_disk --metric schwarzschild --n_views 150

# Stage 3: Train Gaussian Splatting
python scripts/train_splat.py --data data/training_views --output data/splats/blackhole.ply

# Stage 4: Launch viewer
cd pipeline/stage4_viewer
npm run dev
```

## Physics Notes

The first version uses a **Schwarzschild** (non-spinning) black hole with an analytical **thick disk** emission model. This is a defensible simplification — the qualitative features (photon ring, shadow, lensing) are all present. Kerr (spinning) adds Doppler beaming asymmetry and frame dragging, planned for v2.

Key references:

- Levis et al., "Gravitational Lensing of Emission Around Kerr Black Holes" ([bhnerf](https://github.com/aviadlevis/bhnerf))
- Chael et al., [eht-imaging](https://github.com/achael/eht-imaging)
- Gralla, Lupsasca & Marrone, "The shape of the black hole photon ring" ([arXiv:2008.03879](https://arxiv.org/abs/2008.03879))

## Roadmap

- [x] Repo & pipeline architecture
- [ ] Stage 1: Analytical emission model (Schwarzschild thick disk)
- [ ] Stage 2: GR ray-tracing → training views
- [ ] Stage 3: 3DGS training
- [ ] Stage 4: Web viewer with orbit controls
- [ ] Kerr metric support (spin parameter)
- [ ] Doppler boosting & time variability
- [ ] Hosted public demo

## License

MIT — see [LICENSE](LICENSE).
