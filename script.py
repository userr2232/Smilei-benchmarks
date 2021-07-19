import subprocess
from pathlib import Path

subdirs = ["plasma_collision_1", "plasma_collision_2", "plasma_collision_3", "plasma_collision_4"]
smilei_path = Path("/home/reynaldo.rojas/smilei/Smilei")
benchmarks_path = Path(smilei_path / "Smilei-benchmarks")
for subdir in subdirs:
    i = 4
    while i <= 32:
        subprocess.run(f"mkdir {i}_procs".split(), cwd=str(benchmarks_path/subdir))
        subprocess.run(f"cp plasma_collision.py {i}_procs".split(), cwd=str(benchmarks_path/subdir))
        subprocess.run(f"cp smilei {i}_procs".split(), cwd=str(benchmarks_path/subdir))
        # Run with X cores | X particles
        subprocess.run(f"srun --mpi=pmix_v2 -n {i} ./smilei plasma_collision.py".split(), cwd=str(benchmarks_path/subdir/f"{i}_procs"))
        i *= 2


