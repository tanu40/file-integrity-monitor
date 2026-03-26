import hashlib
import os
import json

# Folder to monitor
TARGET_DIR = "../target_folder"
BASELINE_FILE = "../baseline/baseline.json"


# 🔹 Function to generate file hash
def get_file_hash(filepath):
    hasher = hashlib.sha256()

    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()


# 🔹 Create baseline
def create_baseline():
    file_hashes = {}

    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            path = os.path.join(root, file)
            file_hashes[path] = get_file_hash(path)

    with open(BASELINE_FILE, "w") as f:
        json.dump(file_hashes, f, indent=4)

    print("✅ Baseline created successfully!")


# 🔹 Check integrity
def check_integrity():
    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)

    current_files = {}

    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            path = os.path.join(root, file)
            current_files[path] = get_file_hash(path)

    # 🔍 Check for deleted and modified files
    for file, old_hash in baseline.items():
        if file not in current_files:
            print(f"[DELETED] {file}")
        elif current_files[file] != old_hash:
            print(f"[MODIFIED] {file}")

    # 🔍 Check for new files
    for file in current_files:
        if file not in baseline:
            print(f"[NEW FILE] {file}")


# 🔹 Main menu
if __name__ == "__main__":
    print("1. Create Baseline")
    print("2. Check Integrity")

    choice = input("Enter choice: ")

    if choice == "1":
        create_baseline()
    elif choice == "2":
        check_integrity()
    else:
        print("Invalid choice")