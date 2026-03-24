import os

folder_path = "books"
# Get everything in the folder
all_entries = os.listdir(folder_path)

# Filter for only files (optional)
files_only = [f for f in all_entries if os.path.isfile(os.path.join(folder_path, f))]
print(files_only)
