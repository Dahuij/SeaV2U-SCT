#!/usr/bin/env python3
"""Validate SeaV2U-SCT dataset structure and optional release checksums."""
import argparse, csv, hashlib
from pathlib import Path

REQUIRED = ("meta.json", "processing.json", "calibration/cameras.json", "calibration/lidars.json", "calibration/settings_snapshot.json", "timing/summary.json")
def digest(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(8*1024*1024), b""): h.update(b)
    return h.hexdigest()
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("dataset_root",type=Path); ap.add_argument("--repo-root",type=Path,default=Path(__file__).resolve().parents[1]); ap.add_argument("--fast",action="store_true"); ap.add_argument("--checksums",type=Path); ap.add_argument("--assets-root",type=Path)
    a=ap.parse_args(); errors=[]
    with (a.repo_root/"metadata/sequences.csv").open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
    for row in rows:
        seq=a.dataset_root/row["sequence"]
        for rel in REQUIRED:
            if not (seq/rel).is_file(): errors.append(f"{row['sequence']}: missing {rel}")
    if a.checksums:
        root=a.assets_root or a.checksums.parent
        for line in a.checksums.read_text(encoding="utf-8").splitlines():
            if line and not line.startswith("#"):
                wanted,name=line.split(None,1); target=root/name.strip().lstrip("*")
                if not target.is_file() or digest(target).lower()!=wanted.lower(): errors.append(f"checksum mismatch: {target.name}")
    if errors:
        print("Validation failed:")
        for error in errors: print("-",error)
        raise SystemExit(1)
    print(f"Validation passed: {len(rows)} sequences.")
if __name__=="__main__": main()
