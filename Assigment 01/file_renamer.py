import os

folder_path = input("Enter folder path: ")
prefix = input("Enter new prefix (e.g., 'photo_'): ")

count = 1
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        extension = filename.split(".")[-1]
        new_name = f"{prefix}{count}.{extension}"
        os.rename(
            os.path.join(folder_path, filename),
            os.path.join(folder_path, new_name)
        )
        count += 1

print(f"Renamed {count-1} files")