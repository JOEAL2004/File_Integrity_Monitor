import json
from pathlib import Path
from hash_test import calculate_hash


BASELINE_FILE = "baseline.json"


def save_baseline(file_hashes):
    """Save file hashes to the baseline JSON file."""
    with open(BASELINE_FILE, "w") as file:
        json.dump(file_hashes, file, indent=4)


def load_baseline():
    """Load the stored baseline."""
    try:
        with open(BASELINE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Baseline file not found. Please create a baseline first.")
        return None


def scan_directory(path):
    """Scan a directory and return filename-to-hash mappings."""
    file_hashes = {}

    for item in path.iterdir():
        if item.is_file():
            file_hashes[item.name] = calculate_hash(item)

    return file_hashes


def compare_files(current_files, baseline):
    """Compare current files with the stored baseline."""
    results = {
        "unchanged": 0,
        "modified": 0,
        "new": 0,
        "deleted": 0
    }

    for filename, current_hash in current_files.items():

        if filename not in baseline:
            print(f"File {filename} is new.")
            results["new"] += 1

        elif current_hash == baseline[filename]:
            print(f"File {filename} is unchanged.")
            results["unchanged"] += 1

        else:
            print(f"File {filename} has been modified.")
            results["modified"] += 1

    for filename in baseline:
        if filename not in current_files:
            print(f"File {filename} has been deleted.")
            results["deleted"] += 1

    return results


def print_summary(results):
    """Print the integrity monitoring summary."""
    print("\n========== Security Summary ==========")
    print(f"Unchanged files: {results['unchanged']}")
    print(f"Modified files:  {results['modified']}")
    print(f"New files:       {results['new']}")
    print(f"Deleted files:   {results['deleted']}")

    if (
        results["modified"] == 0
        and results["new"] == 0
        and results["deleted"] == 0
    ):
        print("Status: No integrity changes detected.")
    else:
        print("Status: Integrity changes detected.")


def main():
    mode = input("Enter mode (create/monitor): ").lower()

    if mode not in ["create", "monitor"]:
        print("Invalid mode. Please enter 'create' or 'monitor'.")
        return

    directory = input("Enter the directory to monitor: ")
    path = Path(directory)

    if not path.exists():
        print(f"The directory {directory} does not exist.")
        return

    if not path.is_dir():
        print("Error: The specified path is not a directory.")
        return

    print(f"The directory {directory} exists.")
    print("It is a directory.")

    file_hashes = scan_directory(path)

    if mode == "create":
        save_baseline(file_hashes)
        print("Baseline created successfully.")
        return

    baseline = load_baseline()

    if baseline is None:
        return

    results = compare_files(file_hashes, baseline)
    print_summary(results)


if __name__ == "__main__":
    main()