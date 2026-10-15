import json
from pathlib import Path

def write_csv_reports(reports, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, frame in reports.items():
        frame.to_csv(output_dir / f"{name}.csv", index=False)

def write_json(payload, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
