import json
from pathlib import Path
import jupytext, nbformat as nbf

ROOT = Path(__file__).parent.parent
TDOM = ROOT.parent / "tdom"
OUT  = ROOT / "content"
OUT.mkdir(parents=True, exist_ok=True)

KERNELSPEC = {
    "display_name": "Python (Pyodide)",
    "language": "python",
    "name": "python"
}

notebooks = []

# default notebook
notebooks.append("greeting")

for init_py in TDOM.joinpath("examples").rglob("__init__.py"):
    if init_py.parent.parent.name == "examples":
        continue
    name = init_py.parent.name                       # e.g. call_function

    nb = jupytext.read(init_py)
    nb.metadata["kernelspec"] = KERNELSPEC
    nb.metadata.setdefault("language_info", {})["name"] = "python"
    ipynb = OUT / f"{name}.ipynb"
    nbf.write(nb, ipynb)
    notebooks.append(name)                           # just the bare name

(OUT / "notebooks.json").write_text(json.dumps(sorted(notebooks)))
