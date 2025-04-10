"""
List of sample data files for testing purposes.
"""
import os

# Sample data files
# All Sample data files for testing purposes

def find_files_with_extension(directory):
    matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".asd"):
                matching_files.append(os.path.join(root, file))
    return matching_files

all_asd_data_files = find_files_with_extension('.')