




import os
import shutil

print("""

*********************************************************
           ╔══════════════════════════════════╗
           ║        FILE ORGANIZER            ║
           ╚══════════════════════════════════╝
*********************************************************

""")

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav"],
    "Python Files": [".py"],
    "Zip Files": [".zip", ".rar"],
}


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"


def get_unique_destination(destination):
    """If a file with the same name already exists at destination,
    append a number so we never overwrite or fail silently."""
    if not os.path.exists(destination):
        return destination
    base, ext = os.path.splitext(destination)
    counter = 1
    new_destination = f"{base} ({counter}){ext}"
    while os.path.exists(new_destination):
        counter += 1
        new_destination = f"{base} ({counter}){ext}"
    return new_destination


def preview_organization(source_folder):
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    if not files:
        return {}
    plan = {}
    for file in files:
        _, extension = os.path.splitext(file)
        category = get_category(extension)
        plan.setdefault(category, []).append(file)
    return plan


def organize_files(source_folder):
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    moved_count = 0

    for file in files:
        file_path = os.path.join(source_folder, file)
        _, extension = os.path.splitext(file)
        category = get_category(extension)
        category_folder = os.path.join(source_folder, category)
        create_folder(category_folder)
        destination = get_unique_destination(os.path.join(category_folder, file))

        try:
            shutil.move(file_path, destination)
            print(f"✅ Moved: {file} ---> {os.path.basename(category_folder)}/{os.path.basename(destination)}")
            moved_count += 1
        except Exception as e:
            print(f"❌ Error moving {file}: {e}")

    print("\n" + "=" * 36)
    print(f"🎉 Total files organized: {moved_count}")
    print("=" * 36)


source_folder = input("Enter your folder path: ").strip()

if not os.path.isdir(source_folder):
    print("❌ Folder not found!")
    exit()

plan = preview_organization(source_folder)

if not plan:
    print("📂 Folder is empty (or contains only subfolders)!")
    exit()

print("\n📋 Preview — files will be organized like this:")
print("-" * 36)
total_files = 0
for category, files in plan.items():
    print(f"{category}/  ({len(files)} file(s))")
    for f in files:
        print(f"   - {f}")
    total_files += len(files)
print("-" * 36)

confirm = input(f"\nMove these {total_files} file(s) now? (yes/no): ").strip().lower()
if confirm == "yes":
    organize_files(source_folder)
else:
    print("❌ Cancelled — no files were moved.")

input("\nPress Enter to exit...")





