#!/usr/bin/env python
"""The run script."""
import logging, subprocess, sys

# import flywheel functions
from flywheel_gear_toolkit import GearToolkitContext
from utils.parser import parse_config
from app.main import fetalvbm

# Set up logging
log = logging.getLogger(__name__)


def main(context: GearToolkitContext) -> None:
    # """Parses metadata in the SDK to determine which template to use for the subject VBM analysis"""
    print("pulling metadata...")
    input_img, mask_img, age = parse_config(context)
    print("running fetal brain segmentation...")
    e_code = fetalvbm(input_img, mask_img, age)
    sys.exit(e_code)

# Only execute if file is run as main, not when imported by another module
if __name__ == "__main__":  # pragma: no cover
    # Get access to gear config, inputs, and sdk client if enabled.
    with GearToolkitContext() as gear_context:

        # Initialize logging, set logging level based on `debug` configuration
        # key in gear config.
        gear_context.init_logging()

        # Pass the gear context into main function defined above.
        main(gear_context)