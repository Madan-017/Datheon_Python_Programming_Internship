# Automated File Organizer

## 1. Project Overview

The Automated File Organizer is a Python-based desktop utility that automatically organizes files into separate folders based on their file extensions.

It helps users manage cluttered directories by sorting files into categories such as Documents, Images, Videos, Archives, and Code.

## 2. Problem Statement

Downloads and other directories often contain different types of files mixed together. Finding and managing these files manually takes time and creates unnecessary clutter.

This project provides an automated solution that identifies file types and moves them into appropriate category folders.

## 3. Objectives

- Automatically identify files using their extensions.
- Create category folders dynamically.
- Move files into their appropriate folders.
- Prevent accidental overwriting of existing files.
- Handle permission errors and file movement exceptions.
- Display a summary of the organization process.

## 4. Features

1. **Automatic File Detection:** Identifies file types using their extensions.
2. **Dynamic Folder Creation:** Creates category folders when required.
3. **File Categorization:** Supports Documents, Images, Videos, Archives, Code, and Others.
4. **Safe File Movement:** Uses Python's shutil module to move files.
5. **Duplicate Filename Handling:** Generates a unique filename when a destination already exists.
6. **Exception Handling:** Handles permission and file operation errors.
7. **Execution Summary:** Displays the number of files moved, skipped, and failed.

## 5. Technologies Used

- Python 3
- os module
- shutil module
- pathlib module
- logging module

## 6. Project Structure

```text
Task-3-File-Organizer/
│
├── organizer.py
└── README.md
```

## 7. How to Run the Project

1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Execute:

```bash
python organizer.py
```

5. Enter the directory path you want to organize.
6. Confirm the operation by entering `yes`.

## 8. File Categories

| Category | Supported Extensions |
|---|---|
| Documents | PDF, DOC, DOCX, TXT, XLSX, PPTX, CSV |
| Images | JPG, JPEG, PNG, GIF, BMP, SVG, WEBP |
| Videos | MP4, MKV, MOV, AVI, WMV |
| Archives | ZIP, RAR, 7Z, TAR, GZ |
| Code | PY, JS, HTML, CSS, JAVA, CPP, JSON |

Unrecognized extensions are placed in the Others folder.

## 9. Testing and Results

The application was tested using five sample files.

| Test File | Expected Category | Result |
|---|---|---|
| backup.zip | Archives | Passed |
| image.png | Images | Passed |
| notes.txt | Documents | Passed |
| program.py | Code | Passed |
| video.mp4 | Videos | Passed |

**Test Summary:**
- Files moved successfully: 5
- Items skipped: 2 existing folders
- Files failed to move: 0

## 10. Advantages

- Saves time and reduces manual effort.
- Keeps directories clean and organized.
- Automatically creates required folders.
- Prevents filename overwriting.
- Provides clear execution logs and summaries.

## 11. Limitations

- Organizes files directly inside the selected directory; it does not recursively organize files inside existing subfolders.
- Depends on file extensions for categorization.
- Requires appropriate folder permissions.
- Does not identify the actual content of files.

## 12. Conclusion

The Automated File Organizer provides a simple and efficient solution for managing cluttered directories. By using Python file-handling modules, it automatically identifies, categorizes, and moves files into appropriate folders while handling common file operation errors.