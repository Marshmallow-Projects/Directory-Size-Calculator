import os

# -----------------------------------------------------------------------
# Directory Size Calculator by Marshmallow.Projects 
# Calculates the total size of all files in a directory and its subdirectories.
# A program to monitor disk usage or check how much space your files take up.
#
# Developed and maintained by Marshmallow.Projects
# Website: https://github.com/Marshmallow-Projects
# -----------------------------------------------------------------------

def calculate_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def human_readable_size(size_in_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024

# Program start
directory = r'\your\directory'  # Change to your desired directory
size = calculate_directory_size(directory)

print("""
========================================
Directory Size Calculator
Powered by Marshmallow.Projects
========================================
""")

print(f"[Marshmallow.Projects] Total size of '{directory}': {human_readable_size(size)}")
