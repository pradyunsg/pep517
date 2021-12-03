# API reference

## Calling the build system

```{eval-rst}
.. automodule:: pyproject_hooks
    :members: PyProjectHookCaller
```

## Subprocess runners

These can be passed as `subprocess_runner` keyword arguments to {class}`PyProjectHookCaller`, or {meth}`PyProjectHookCaller.subprocess_runner`.

```{eval-rst}
.. automodule:: pyproject_hooks
    :members: default_subprocess_runner, quiet_subprocess_runner
```

## Exceptions

```{eval-rst}
.. automodule:: pyproject_hooks
    :members: BackendUnavailable, BackendInvalid, HookMissing, UnsupportedOperation
```
