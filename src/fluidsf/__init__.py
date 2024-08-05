"""
Structure function calculation package.
This package calculates structure functions from ocean velocity data.
"""

from .bin_data import bin_data
from .calculate_advection_2d import calculate_advection_2d
from .calculate_advection_3d import calculate_advection_3d
from .calculate_separation_distances import calculate_separation_distances
from .calculate_separation_distances_3d import calculate_separation_distances_3d
from .calculate_sf_maps_2d import calculate_sf_maps_2d
from .calculate_structure_function_1d import calculate_structure_function_1d
from .calculate_structure_function_2d import calculate_structure_function_2d
from .calculate_structure_function_3d import calculate_structure_function_3d
from .generate_sf_maps_2d import generate_sf_maps_2d
from .generate_structure_functions_1d import generate_structure_functions_1d
from .generate_structure_functions_2d import generate_structure_functions_2d
from .generate_structure_functions_3d import generate_structure_functions_3d
from .shift_array_1d import shift_array_1d
from .shift_array_2d import shift_array_2d
from .shift_array_3d import shift_array_3d

__version__ = "0.2.0"

__all__ = (
    "generate_sf_maps_2d",
    "generate_structure_functions_1d",
    "generate_structure_functions_2d",
    "generate_structure_functions_3d",
    "calculate_sf_maps_2d",
    "calculate_structure_function_1d",
    "calculate_structure_function_2d",
    "calculate_structure_function_3d",
    "calculate_advection_2d",
    "calculate_advection_3d",
    "calculate_separation_distances",
    "calculate_separation_distances_3d",
    "shift_array_1d",
    "shift_array_2d",
    "shift_array_3d",
    "bin_data",
)
