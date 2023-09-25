import os
import shutil

def backup_and_compress(directory_path, backup_name):
    """
    Backs up and compresses the specified directory.

    Args:
    - directory_path (str): Path to the directory to be backed up.
    - backup_name (str): Name of the backup file (without extension).

    Returns:
    - str: Path to the backup file.
    """
    # Ensure the directory exists
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        return

    # Create a zip archive
    shutil.make_archive(backup_name, 'zip', directory_path)
    print(f"Backup completed: {backup_name}.zip")

    return f"{backup_name}.zip"

def main():
    directory_to_backup = "/path/to/directory"  # Replace with the path to your directory
    backup_name = "backup_directory"  # Name for the backup file

    backup_and_compress(directory_to_backup, backup_name)

if __name__ == "__main__":
    main()
