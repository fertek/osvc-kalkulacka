import subprocess
import sys
from importlib import resources


def test_package_importable() -> None:
    __import__("osvc_kalkulacka")


def test_embedded_year_defaults_loads() -> None:
    data = resources.files("osvc_kalkulacka.data").joinpath("year_defaults.toml").read_bytes()
    assert data


def test_cli_help_runs() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "osvc_kalkulacka.cli", "--help"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Usage:" in result.stdout
    assert "calc" in result.stdout
