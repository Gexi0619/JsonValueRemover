import json
import sys
import os

# Check if the command line argument is provided correctly
if len(sys.argv) != 2:
    print("Please provide the path to the configuration file ending with .json as a command line argument")
    sys.exit(1)

# Get the path to the configuration file from the command line argument
config_path = sys.argv[1]

# Check if the configuration file exists
if not os.path.isfile(config_path):
    print("Configuration file does not exist")
    sys.exit(1)

# Check if the configuration file has the .json extension
if not config_path.endswith(".json"):
    print("Please provide the path to the configuration file ending with .json")
    sys.exit(1)

# Read the configuration file
with open(config_path, encoding='utf-8') as config_file:
    config = json.load(config_file)

# Recursively set all values to an empty string
def remove_values(data):
    if isinstance(data, dict):
        return {key: remove_values(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [remove_values(item) for item in data]
    else:
        return ""

# Set values in the configuration file to an empty string
new_config = remove_values(config)

# Construct the new file name
dirname, basename = os.path.split(config_path)
filename, ext = os.path.splitext(basename)
new_filename = os.path.join(dirname, f"{filename}_rmvalue{ext}")

# Write the updated configuration to a new JSON file
with open(new_filename, "w", encoding='utf-8') as new_config_file:
    json.dump(new_config, new_config_file, indent=4, ensure_ascii=False)

print(f"Generated new JSON file: {new_filename}")
