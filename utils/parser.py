"""Parser module to parse gear config.json."""

from typing import Tuple
from flywheel_gear_toolkit import GearToolkitContext

def parse_config(
    gear_context: GearToolkitContext,
) -> Tuple[str, str, str]:
    """Parses the config info.
    Args:
        gear_context: Context.

    Returns:
        Tuple of input 

    """
    input = gear_context.get_input_path("input")
    mask  = gear_context.get_input_path("mask")
    age   = gear_context.config.get("age")


    return input, mask, age