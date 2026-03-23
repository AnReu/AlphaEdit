"""
ROME package.

This repo's AlphaEdit path depends on `rome.layer_stats` for second-moment stats.
Importing `rome_main` here eagerly pulls optional deps (e.g. matplotlib) that are
not required for AlphaEdit itself, and can break minimal installs.
"""

from typing import Any

_ROME_IMPORT_ERROR: Exception | None = None

try:
    from .rome_main import ROMEHyperParams, apply_rome_to_model, execute_rome  # noqa: F401
except Exception as e:  # pragma: no cover
    _ROME_IMPORT_ERROR = e


def __getattr__(name: str) -> Any:  # pragma: no cover
    if name in {"ROMEHyperParams", "apply_rome_to_model", "execute_rome"} and _ROME_IMPORT_ERROR:
        raise ImportError(
            "Failed to import ROME. Install optional dependencies (e.g. matplotlib) "
            "or avoid importing ROME entrypoints."
        ) from _ROME_IMPORT_ERROR
    raise AttributeError(name)
