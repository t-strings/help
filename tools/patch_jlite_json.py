import json
import pathlib
import argparse

p = argparse.ArgumentParser()
p.add_argument("json_path")
p.add_argument("--whl-url", required=True)
p.add_argument("--disable-dirty", action="store_true")
p.add_argument("--autosave-interval", type=int)
args = p.parse_args()

path = pathlib.Path(args.json_path)
data = json.loads(path.read_text())

cfg = data.setdefault("jupyter-config-data", {})
lp  = cfg.setdefault("litePluginSettings", {})
k   = "@jupyterlite/pyodide-kernel-extension:kernel"
plugin = lp.setdefault(k, {})
plugin["pyodideUrl"] = "./pyodide/pyodide.js"
opt = plugin.setdefault("loadPyodideOptions", {})
opt["indexURL"] = "./pyodide/"
opt["packages"] = [args.whl_url]

nb_key = "@jupyterlab/notebook-extension:tracker"
cfg.setdefault(nb_key, {})["autoStartDefaultKernel"] = True

if args.disable_dirty:
    de = cfg.setdefault("disabledExtensions", [])
    plug_id = "@jupyterlab/application-extension:dirty"
    if plug_id not in de:
        de.append(plug_id)

if args.autosave_interval is not None:
    dm_key = "@jupyterlab/docmanager-extension:plugin"
    cfg.setdefault(dm_key, {})["autosaveInterval"] = args.autosave_interval

path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
