import os

import nox

PACKAGE_NAME = "pyproject_hooks"


@nox.session(reuse_venv=True)
def docs(session: nox.Session) -> None:
    session.install(
        # fmt: off
        ".",
        "-r", "docs/requirements.txt",
        # fmt: on
    )

    session.run("sphinx-build", "-b", "dirhtml", "-v", "docs/", "build/docs")


@nox.session(name="docs-live", reuse_venv=True)
def docs_live(session: nox.Session) -> None:
    session.install(
        # fmt: off
        "-e", ".",
        "-r", "docs/requirements.txt",
        "sphinx-autobuild",
        # fmt: on
    )

    session.run("sphinx-autobuild", "-b", "dirhtml", "docs/", "build/docs", "-a")


@nox.session(reuse_venv=True)
def lint(session: nox.Session) -> None:
    session.install("pre-commit")

    args = list(session.posargs)
    args.append("--all-files")
    if "CI" in os.environ:
        args.append("--show-diff-on-failure")

    session.run("pre-commit", "run", *args)


@nox.session(python=["3.7", "3.8", "3.9", "3.10"])
def test(session: nox.Session) -> None:
    session.install(
        # fmt: off
        "-e", ".",
        "-r", "tests/requirements.txt",
        # fmt: on
    )

    args = session.posargs or ["-n", "auto", "--cov", PACKAGE_NAME]
    session.run("pytest", *args)


@nox.session
def release(session: nox.Session) -> None:
    session.install("flit", "keyring")
    session.run("flit", "publish", "--no-setup-py", *session.posargs)
