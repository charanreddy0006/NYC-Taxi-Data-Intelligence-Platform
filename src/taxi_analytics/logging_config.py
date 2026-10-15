import logging
from pathlib import Path

def configure_logging(log_dir: Path):
    log_dir.mkdir(parents=True, exist_ok=True)
    root = logging.getLogger()
    if root.handlers:
        return
    root.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(name)s | %(message)s")
    fh = logging.FileHandler(log_dir / "pipeline.log", encoding="utf-8")
    sh = logging.StreamHandler()
    fh.setFormatter(fmt); sh.setFormatter(fmt)
    root.addHandler(fh); root.addHandler(sh)
