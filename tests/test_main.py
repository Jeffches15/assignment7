import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from main import is_valid_url

def test_is_valid_url():
    assert is_valid_url("https://example.com") is True
    assert is_valid_url("not-a-url") is False