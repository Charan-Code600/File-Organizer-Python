


import os
import shutil

SOURCE_FOLDER = input("Enter your folder path: ")

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

def organize_files():
    if not os.path.exists(SOURCE_FOLDER):
        print("❌ Folder not found!")
        return

    files = os.listdir(SOURCE_FOLDER)

    if len(files) == 0:
        print("📂 Folder is empty!")
        return

    moved_count = 0

    for file in files:
        file_path = os.path.join(SOURCE_FOLDER, file)

        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(file)
        category = get_category(extension)
        category_folder = os.path.join(SOURCE_FOLDER, category)
        create_folder(category_folder)
        destination = os.path.join(category_folder, file)

        try:
            shutil.move(file_path, destination)
            print(f"✅ Moved: {file} ---> {category}/")
            moved_count += 1
        except Exception as e:
            print(f"❌ Error moving {file}: {e}")

    print("\n==============================")
    print(f"🎉 Total files organized: {moved_count}")
    print("==============================")

if __name__ == "__main__":
    organize_files()
    input("\nPress Enter to exit...")
