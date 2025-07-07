from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()


@dataclass(slots=True)
class Config:
    vault_path: str = os.getenv("VAULT_PATH", os.getcwd())
    base_dir: str = os.getenv("SUMMARY_BASE_DIR", "_summaries")
    model: str = os.getenv("MODEL", "gpt-4o-mini")
    daily_max_chars: int = int(os.getenv("DAILY_MAX_CHARS", 3000))
