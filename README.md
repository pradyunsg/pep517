# pyproject-hooks

<!-- start-intro -->

This package contains wrappers to call hooks on build backends for `pyproject.toml`-based projects. It is intended to be a low-level shared implementation for tools like `pip` and `build`.

These wrappers provide:

- Fallback for the optional hooks.
  - Build frontends can call the hooks without checking if they are defined.
- Isolation from current process, via a subprocess.
  - Build frontends can control how the subprocess is run.

<!-- end-intro -->

## Usage

<!-- start-usage -->

```python
import os
import tomli
from pyproject_hooks.wrappers import PyProjectHookCaller

source_path = "path/to/source"
pyproject_toml_path = os.path.join(source_path, "pyproject.toml")

with open(pyproject_toml_path) as f:
    build_system = tomli.load(f)["build-system"]

# The caller is responsible for installing these and running the hooks in
# an environment where they are available.
print("static build-time requirements:", build_system["requires"])

hooks = PyProjectHookCaller(
    source_path,
    build_backend=build_system["build-backend"],
    backend_path=build_system.get("backend-path"),
)
config_options = {}  # Optional parameters for build backend

# Again, the caller is responsible for installing these build requirements
print(
    "dynamic build-time requirements:",
    hooks.get_requires_for_build_wheel(config_options),
)

destination = "also/a/folder"
whl_filename = hooks.build_wheel(destination, config_options)
assert os.path.isfile(os.path.join(destination, whl_filename))
```

<!-- end-usage -->
