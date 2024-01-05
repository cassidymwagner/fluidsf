"""
Structure function calculation package.
This package calculates structure functions from ocean velocity data.
"""

from .advection_scalar import advection_scalar  # noqa: F401
from .advection_velocity import advection_velocity
from .calculate_scalar_advection import calculate_scalar_advection  # noqa: F401
from .calculate_velocity_advection import calculate_velocity_advection
from .traditional_scalar import traditional_scalar  # noqa: F401
from .traditional_velocity import traditional_velocity  # noqa: F401

__all__ = (
    "velocity_advection",
    "advection_velocity",
    "advection_scalar" "traditional_velocity",
    "traditional_scalar" "calculate_scalar_advection",
    "calculate_velocity_advection",
)
