from datetime import date
from pathlib import Path
from ..config import Config
from ..llm import chat
from ..utils import build_prompt
from ..git_utils import changed_md_files

TEMPLATE = Path(__file__).with_suffix("").parent.parent / "templates/prompt_daily.md.j2"
SYSTEM_PROMPT = TEMPLATE.read_text()


def run(commit_sha: str, cfg: Config):
    files = changed_md_files(commit_sha)
    if not files:
        return
    prompt = build_prompt(files, cfg.daily_max_chars)
    md = chat(
        [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        model=cfg.model,
    )
    out_dir = Path(cfg.vault_path) / cfg.base_dir / "Daily"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{date.today()}.md"
    out_file.write_text(md, encoding="utf-8")
