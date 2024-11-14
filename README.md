# VCD Concatenation and Duplication Script

This script allows users to concatenate or duplicate VCD (Value Change Dump) files, which are commonly used for storing digital simulation data. The script supports two main functionalities:

1. **Concatenate multiple VCD files** by appending the timestamps from each file in sequence.
2. **Duplicate a single VCD file multiple times**, with each duplication having incremented timestamps, to simulate multiple iterations of the same test scenario.

NB! It does not check the consistency between designs.
## Prerequisites

- Python 3.x
- Required libraries: `argparse`, `sys`, and `re` (all are part of the Python standard library).

## Usage

Run the script from the command line with the following arguments:

```bash
python vcd_script.py --input-files <input_file(s)> --output-file <output_file> [--iterations <n>]
