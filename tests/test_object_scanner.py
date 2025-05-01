import pytest
from pathlib import Path
from src.guardian.object_scanner import read_loose
import zlib

@pytest.fixture
def valid_loose_object(tmp_path: Path) -> Path:
    """Fixture: Objeto Git loose válido (blob)."""
    obj_path = tmp_path / "ab" / "c123"
    obj_path.parent.mkdir()
    content = b"blob 5\0hello"
    compressed = zlib.compress(content)
    obj_path.write_bytes(compressed)
    return obj_path

def test_read_loose_valid(valid_loose_object: Path):
    """Caso 1: Objeto válido."""
    obj = read_loose(valid_loose_object)
    assert obj is not None
    assert obj.type == "blob"
    assert obj.data == b"hello"
    assert obj.sha == "c123"

def test_read_loose_invalid_path():
    """Caso 2: Ruta inválida."""
    assert read_loose(Path("/fake/path")) is None

def test_read_loose_corrupt_data():
    """Caso 3: Objeto corrupto."""
    corrupt_path = Path("fixtures/corrupt-blob.git/objects/ab/c123")
    assert read_loose(corrupt_path) is None

def test_read_loose_unknown_type(tmp_path: Path):
    """Caso 4: Tipo desconocido."""
    unknown_type_path = tmp_path / "unknown"
    content = b"blobX 5\0hello"
    unknown_type_path.write_bytes(zlib.compress(content))
    assert read_loose(unknown_type_path) is None

def test_read_loose_size_mismatch(tmp_path: Path):
    """Caso 5: Tamaño incongruente."""
    size_mismatch_path = tmp_path / "size_mismatch"
    content = b"blob 999\0hello"  # Tamaño declarado ≠ real
    size_mismatch_path.write_bytes(zlib.compress(content))
    assert read_loose(size_mismatch_path) is None

def test_read_loose_empty_object(tmp_path: Path):
    """Caso 6: Objeto vacío."""
    empty_path = tmp_path / "empty"
    empty_path.write_bytes(zlib.compress(b""))
    assert read_loose(empty_path) is None
