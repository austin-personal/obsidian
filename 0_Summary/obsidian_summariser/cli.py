import click, subprocess, logging, sys
from .config import Config
from .summarizers import daily, weekly, monthly

logging.basicConfig(
    filename="obsidian_summaries.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

cfg = Config()


@click.group()
def app():
    pass


@app.command()
@click.option("--commit", default=None, help="SHA (생략 시 HEAD)")
def daily_cmd(commit):
    sha = (
        commit
        or subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    )
    daily.run(sha, cfg)


@app.command()
def weekly_cmd():
    weekly.run(cfg)  # 구현 동일 패턴


@app.command()
def monthly_cmd():
    monthly.run(cfg)


if __name__ == "__main__":
    sys.exit(app())
