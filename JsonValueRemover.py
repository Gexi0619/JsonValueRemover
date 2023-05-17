import os
import json
import sys

# Get the path and name of the old JSON file
old_file_path = os.path.abspath(sys.argv[1])
old_file_name = os.path.basename(old_file_path)

# Parse the command-line arguments to get the new file name (if provided)
if len(sys.argv) > 2:
    new_file_path = os.path.abspath(sys.argv[2])
else:
    # Construct the default new file name
    new_file_name = f"{os.path.splitext(old_file_name)[0]}_valueless.json"
    new_file_path = os.path.join(os.path.dirname(old_file_path), new_file_name)

# Read the configuration file
with open(old_file_path) as config_file:
    config = json.load(config_file)

# Recursively remove all values and set them to an empty string
def remove_values(data):
    if isinstance(data, dict):
        return {key: remove_values(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [remove_values(item) for item in data]
    else:
        return ""

# Set the values in the configuration file to an empty string
config = remove_values(config)

# Write the updated configuration to the new file
with open(new_file_path, "w") as new_file:
    json.dump(config, new_file, indent=4)

print(f"New JSON file '{new_file_path}' has been generated successfully.")
