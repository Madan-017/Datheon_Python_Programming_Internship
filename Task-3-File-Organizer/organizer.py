
import os
import shutil
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

# File extension categories
FILE_CATEGORIES = {
    "Documents": [
        ".pdf", ".doc", ".docx", ".txt", ".rtf",
        ".xls", ".xlsx", ".ppt", ".pptx", ".csv"
    ],
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp",
        ".svg", ".webp", ".tiff", ".ico"
    ],
    "Videos": [
        ".mp4", ".mkv", ".mov", ".avi", ".wmv",
        ".flv", ".webm", ".mpeg"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"
    ],
    "Code": [
        ".py", ".js", ".html", ".css", ".java",
        ".cpp", ".c", ".cs", ".php", ".json",
        ".xml", ".sql", ".ipynb"
    ]
}


def get_category(file_extension):
    """Return the category for a file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category

    return "Others"


def get_unique_path(destination):
    """Generate a new filename if the destination already exists."""
    if not destination.exists():
        return destination

    folder = destination.parent
    filename = destination.stem
    extension = destination.suffix
    counter = 1

    while True:
        new_destination = folder / f"{filename} ({counter}){extension}"

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_files(folder_path):
    """Organize files into category folders."""

    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        logging.error("The specified folder does not exist.")
        return

    moved = 0
    skipped = 0
    failed = 0

    # Inspect entries in the selected directory
    try:
        entries = list(os.scandir(folder))
    except PermissionError:
        logging.error("Permission denied: Cannot access this folder.")
        return

    for entry in entries:

        # Skip folders and symbolic links
        if not entry.is_file(follow_symlinks=False):
            skipped += 1
            continue

        source = Path(entry.path)

        # Identify category using file extension
        category = get_category(source.suffix)

        destination_folder = folder / category
        destination = destination_folder / source.name

        try:
            # Create category folder when required
            destination_folder.mkdir(exist_ok=True)

            # Prevent overwriting existing files
            destination = get_unique_path(destination)

            # Move file safely
            shutil.move(str(source), str(destination))

            logging.info(
                f"Moved: {source.name} -> {category}/{destination.name}"
            )

            moved += 1

        except PermissionError:
            logging.warning(f"Permission denied: {source.name}")
            failed += 1

        except FileExistsError:
            logging.warning(f"File already exists: {source.name}")
            failed += 1

        except OSError as error:
            logging.error(f"Could not move {source.name}: {error}")
            failed += 1

    # Display execution summary
    print("\n========== ORGANIZATION SUMMARY ==========")
    print(f"Files moved successfully : {moved}")
    print(f"Items skipped            : {skipped}")
    print(f"Files failed to move     : {failed}")
    print("===========================================")


if __name__ == "__main__":

    print("AUTOMATED FILE ORGANIZER")
    print("------------------------")

    folder_path = input("Enter the folder path to organize: ").strip()
    folder_path = folder_path.strip('"')

    print(f"\nSelected folder: {folder_path}")
    confirmation = input("Do you want to organize this folder? (yes/no): ")

    if confirmation.lower() == "yes":
        organize_files(folder_path)
    else:
        print("Operation cancelled. No files were moved.")
