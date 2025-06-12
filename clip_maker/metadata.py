"""Metadata CSV generation utilities."""

from typing import List, Dict
import csv
from pathlib import Path


def write_metadata_csv(entries: List[Dict], output_folder: str) -> None:
    """Write clip metadata to a CSV file for scheduling tools."""
    if not entries:
        return

    output_path = Path(output_folder) / "metadata.csv"
    fieldnames = list(entries[0].keys())
    with output_path.open("w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entries)
