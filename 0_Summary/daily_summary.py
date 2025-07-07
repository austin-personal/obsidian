import os, datetime

VAULT_ROOT = os.getenv("VAULT_PATH") or os.getcwd()
BASE_DIR = os.getenv("SUMMARY_BASE_DIR", "_summaries")  # ← 기본값 유지


def save_summary(text: str, cycle: str = "daily"):
    """
    cycle: 'daily' | 'weekly' | 'monthly'
    """
    today = datetime.date.today()
    if cycle == "daily":
        fname = f"{today.isoformat()}.md"
    elif cycle == "weekly":
        yr, wk, _ = today.isocalendar()
        fname = f"{yr}-W{wk:02}.md"
    else:  # monthly
        fname = f"{today.strftime('%Y-%m')}.md"

    out_dir = os.path.join(VAULT_ROOT, BASE_DIR, cycle.capitalize())
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as fp:
        fp.write(text)
