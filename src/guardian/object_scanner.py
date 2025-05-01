from pathlib import Path
from typing import Optional
import zlib

class GitObject:
    """Representa un objeto Git (blob, commit, tree, tag)."""
    def __init__(self, type: str, data: bytes, sha: str):
        self.type = type  # Ej: "blob", "commit"
        self.data = data
        self.sha = sha

def read_loose(path: Path) -> Optional[GitObject]:
    """
    Lee un objeto Git loose y valida su integridad.
    Tipos válidos: 'blob', 'commit', 'tree', 'tag'.
    """
    if not path.exists():
        return None

    try:
        with open(path, "rb") as f:
            raw_data = f.read()
        decompressed = zlib.decompress(raw_data)
    except (zlib.error, FileNotFoundError):
        return None

    header, _, content = decompressed.partition(b"\x00")
    try:
        type, size_str = header.decode().split()
        size = int(size_str)
    except (ValueError, UnicodeDecodeError):
        return None

    # Validar tipos Git conocidos
    if type not in {"blob", "commit", "tree", "tag"}:  # <--- Nueva validación
        return None

    if size != len(content):
        return None

    return GitObject(type, content, sha=path.stem)
