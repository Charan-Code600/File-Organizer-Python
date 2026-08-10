




# 📁 File Organizer

A Python tool that automatically sorts files in a folder into category subfolders (Images, Videos, Documents, Music, Python Files, Zip Files, Others) — with a preview before anything moves, and safe handling of duplicate filenames.

## Features

- 📋 Shows a full preview of what will move where, *before* touching any files
- ✅ Nothing is moved until you explicitly confirm with `yes`
- 🗂️ Automatically sorts files by extension into categories:
  - **Images** — .jpg, .jpeg, .png, .gif, .webp
  - **Videos** — .mp4, .mkv, .avi, .mov
  - **Documents** — .pdf, .docx, .txt, .pptx, .xlsx
  - **Music** — .mp3, .wav
  - **Python Files** — .py
  - **Zip Files** — .zip, .rar
  - **Others** — anything that doesn't match the above (including files with no extension)
- 🔄 Safe collision handling — if a file with the same name already exists in the destination folder, the new one is automatically renamed (e.g. `photo (1).jpg`) instead of overwriting or silently failing
- 📂 Only organizes files in the top level of the given folder — existing subfolders are left untouched
- ❌ Handles invalid folder paths and empty folders gracefully

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

```bash
python file_organizer.py
```

## How to Use

1. Run the program and enter the full path of the folder you want to organize.
2. A preview is shown, grouping every file by the category it would move into.
3. Review the preview carefully.
4. Type `yes` to move the files, or `no` to cancel — nothing is touched unless you confirm.
5. Category folders (like `Documents/`, `Images/`) are created automatically inside the folder you gave, and files are moved into them.
6. If a file with the same name already exists in a category folder, your file is saved with a number added to its name instead of overwriting the existing one.

## Technologies Used

- Python
- os module
- shutil module

## Author

Charan Aade | Python Developer






