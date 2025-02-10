import os
import time

# Define the directory to start from
directory_path = "Z:\\"  # Use raw string to avoid escape character issues

# Define the output file path
output_file_path = "modified_files.txt"  # Replace with desired output file path

# Define the time period (7 days ago)
seven_days_ago = time.time() - 7 * 24 * 60 * 60  # 7 days in seconds

# List to store file paths and their modification times
files_info = []

# Walk through the directory and its subdirectories
for root, dirs, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(root, file)
        # Get the last modified time of the file
        last_modified_time = os.path.getmtime(file_path)

        # If the file was modified in the last 7 days, add to the list
        if last_modified_time > seven_days_ago:
            files_info.append((file_path, last_modified_time))

# Sort the list of files by the last modified time in descending order
files_info.sort(key=lambda x: x[1], reverse=True)

# Open the output file in write mode
with open(output_file_path, 'w') as output_file:
    # Write the file paths to the output file
    for file_path, _ in files_info:
        output_file.write(file_path + "\n")

print(f"File paths written to {output_file_path}")
