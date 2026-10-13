"""
Usage: KARST_INPUT_DIR=/path/to/KarstNSim_Public/Input_files/1_base python tests/smoke_test.py
"""
import os
import sys
from pathlib import Path

from pykarstnsim.config import KarstConfig
from pykarstnsim.karstnsim import run_simulation
from pykarstnsim.models import (ConnectivityMatrix, ProjectBox, Sink, Spring,
                                Surface)

d = Path(os.environ["KARST_INPUT_DIR"])
cfg = KarstConfig()
cfg.selected_seed = 1
cfg.use_cycle_amplification = False
cfg.use_deadend_points = False
cfg.nb_deadend_points = 0
cfg.use_density_property = False
cfg.poisson_radius = float(os.environ.get("KARST_POISSON_RADIUS", 0.03))
cfg.nghb_count = 30
cfg.refine_surface_sampling = 1

res = run_simulation(
    config=cfg,
    project_box=ProjectBox.from_file(d / "example_box.txt"),
    sinks=Sink.from_file(d / "example_sinks.txt"),
    springs=Spring.from_file(d / "example_springs.txt"),
    connectivity_matrix=ConnectivityMatrix.from_file(d / "connectivity_matrix.txt"),
    water_tables=[Surface.from_file(d / "example_watertable_surf1.txt"),
                  Surface.from_file(d / "example_watertable_surf2.txt")],
    topo_surface=Surface.from_file(d / "example_topo_surf.txt"),
    inception_surfaces=[Surface.from_file(d / "example_inception_surf1.txt"),
                        Surface.from_file(d / "example_inception_surf2.txt")],
)
assert res is not None, "simulation returned None"
segs = res.segments
pts = [p for s in segs for p in (s.start, s.end)]
print("segments:", len(segs))
print("branch ids:", len({p.branch_id for p in pts}))
print("cost range:", min(p.cost for p in pts), max(p.cost for p in pts))
if hasattr(pts[0], "vadose_flags"):
    print("vadose_flags len:", len(pts[0].vadose_flags), "sample:", pts[0].vadose_flags)
print("vadose_flag sample:", repr(pts[0].vadose_flag))
print(res.to_string().splitlines()[0])
assert len(segs) > 0
print("OK")
