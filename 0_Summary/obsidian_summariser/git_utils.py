import subprocess, pathlib


def changed_md_files(commit_sha: str) -> list[pathlib.Path]:
    out = subprocess.check_output(
        ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", commit_sha],
        text=True,
    )
    root = pathlib.Path(
        subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], text=True
        ).strip()
    )
    return [
        root / p for p in out.splitlines() if p.endswith(".md") and (root / p).exists()
    ]
