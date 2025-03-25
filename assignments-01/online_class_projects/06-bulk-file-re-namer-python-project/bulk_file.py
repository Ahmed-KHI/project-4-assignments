import os

def bulk_rename(folder_path, prefix):
    try:
        files = os.listdir(folder_path)

        for index, file in enumerate(files):
            old_path = os.path.join(folder_path, file)
            if os.path.isfile(old_path):  # Ensure it's a file, not a folder
                file_extension = os.path.splitext(file)[1]  # Get file extension
                new_name = f"{prefix}_{index + 1}{file_extension}"  # Rename format
                new_path = os.path.join(folder_path, new_name)
                os.rename(old_path, new_path)

        print("✅ All files renamed successfully!")

    except Exception as e:
        print(f"⚠️ Error: {e}")

# Example Usage
folder_path = input("Enter folder path: ")
prefix = input("Enter prefix for renaming: ")
bulk_rename(folder_path, prefix)