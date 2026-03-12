# Architecture Decisions

## ADR-001: Schwarzschild first, Kerr later

**Decision:** Start with a non-spinning (Schwarzschild, a=0) black hole for v1.

**Rationale:** Schwarzschild geodesics are simpler (no frame dragging, no ergosphere). All the qualitative features people want to see — photon ring, shadow, gravitational lensing, bright disk — are present. Kerr adds Doppler beaming asymmetry (one side of the disk brighter than the other) and frame dragging, which are important for scientific accuracy but not for a first demo.

**Trade-off:** Loses the left-right brightness asymmetry from the disk's orbital velocity. Acceptable for v1.

## ADR-002: Analytical thick disk, not GRMHD

**Decision:** Use an analytical geometrically-thick disk model (Polish doughnut) rather than full GRMHD simulation data.

**Rationale:** GRMHD simulations require specialized codes (BHAC, iharm3D, KORAL) and significant compute. An analytical model gives a physically motivated emissivity field with a few parameters, runs instantly, and produces visually convincing training views. The 3DGS optimizer doesn't need turbulent substructure — it needs consistent multi-view geometry.

**Trade-off:** No turbulent filaments or magnetic field structure. Fine for demonstrating the pipeline; swap in GRMHD data later for scientific fidelity.

## ADR-003: Custom ray-tracer vs. bhnerf/kgeo

**Decision:** Start with a minimal custom Schwarzschild ray-tracer, with bhnerf/kgeo as a fallback.

**Rationale:** For Schwarzschild, the geodesic equations reduce to a 1D effective potential problem that's straightforward to integrate numerically. Writing our own gives full control over the camera model and output format (we need exact camera poses for 3DGS). bhnerf is JAX-based and powerful but tightly coupled to its own rendering pipeline. If our custom tracer is too slow or inaccurate, we fall back to kgeo.

## ADR-004: gsplat for 3DGS training

**Decision:** Use gsplat (nerfstudio project) over the original 3DGS repo.

**Rationale:** gsplat is actively maintained, Apache 2.0 licensed, has a clean Python API, and supports the latest optimizations (anti-aliasing, densification strategies). The original 3DGS repo works but has a more complex build process and is research-oriented.

## ADR-005: Static splat viewer, not real-time re-rendering

**Decision:** The web viewer loads a pre-trained .ply splat. It does NOT do real-time ray-tracing.

**Rationale:** Real-time GR ray-tracing in WebGL is possible but extremely challenging and would limit the visual quality. Gaussian Splatting gives us a pre-baked 3D representation that renders at 60+ FPS in the browser with no physics computation at runtime. The physics fidelity comes from the training views, not the viewer.
