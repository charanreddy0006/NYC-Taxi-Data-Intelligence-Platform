from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
def load_config(path=None):
    config_path = Path(path) if path else ROOT / "configs" / "config.yaml"
    if not config_path.is_absolute():
        config_path = ROOT / config_path
    with config_path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}
def resolve_path(path):
    p = Path(path)
    return p if p.is_absolute() else ROOT / p
