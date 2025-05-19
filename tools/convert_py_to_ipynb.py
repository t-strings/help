import json
from pathlib import Path
import jupytext, nbformat as nbf

ROOT = Path(__file__).parent.parent
TDOM = ROOT.parent / "tdom"
OUT  = ROOT / "content"
OUT.mkdir(parents=True, exist_ok=True)

notebooks = []

for init_py in TDOM.joinpath("examples").rglob("__init__.py"):
    name = init_py.parent.name                       # e.g. call_function
    ipynb = OUT / f"{name}.ipynb"
    nbf.write(jupytext.read(init_py), ipynb)
    notebooks.append(name)                           # just the bare name

(OUT / "notebooks.json").write_text(json.dumps(sorted(notebooks)))
