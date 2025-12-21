from pathlib import Path
from dataclasses import dataclass

@dataclass (frozen=True)
class Paths:
    root:Path
    raw:Path
    cache:Path
    processed:Path
    external:Path

def make_paths(root:Path):
    data=root/"data"
    return Paths(
        root=root,
        raw=data/"raw",
        cache=data/"cache",
        processed=data/"processed",
        external=data/"external",
    )