# JSON Value Remover

The JSON Value Remover is a lightweight command-line tool developed in Python to remove values from a JSON file. It provides a convenient way to clean sensitive or unwanted data from JSON files while preserving the original structure and keys.

## Installation

1. Please make sure that you have [Python](https://www.python.org) installed on your computer.

2. Clone the repository by running the following command:
   ```
   git clone https://github.com/Gexi0619/JsonValueRemover.git
   ```

## Usage
Run the script using the following command:
```
python JsonValueRemover.py <input_file_path> [output_file_path]
```

- `<input_file_path>`: Required. The path to the input JSON file that you want to process.
- `[output_file_path]`: Optional. The path to the output JSON file. If not provided, the output file will be generated with the name `<input_file_name>_valueless.json` at the same location as the input file.

## License
This script is licensed under the [MIT License](https://opensource.org/licenses/MIT). 
