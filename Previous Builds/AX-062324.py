import os
import py7zr
import zipfile
from concurrent.futures import ThreadPoolExecutor
import time


def extract_archive(filename, base_folder):
    try:
        if filename.endswith(".7z"):
            with py7zr.SevenZipFile(
                os.path.join(base_folder, filename), "r"
            ) as archive:
                archive.extractall(path=base_folder)

        elif filename.endswith(".zip"):
            with zipfile.ZipFile(os.path.join(base_folder, filename), "r") as archive:
                archive.extractall(path=base_folder)

        print(f"| + | Extracted - {filename}")

    except Exception as e:
        print(f"| ! | Error extracting {filename}: {e}")


def wait_for_extraction(files_to_extract, base_folder):
    extracted_files = 0
    while extracted_files < len(files_to_extract):
        time.sleep(1)
        extracted_files = len(
            [f for f in os.listdir(base_folder) if f not in files_to_extract]
        )


def print_list_of_folders(folders):
    print("----------------------------------")
    print("Select a folder:")
    for i, folder in enumerate(folders):
        print(f"{i+1}. {folder}")


def main():
    while True:
        # Get a list of folders in the current directory
        folders = [f for f in os.listdir(".") if os.path.isdir(f)]

        print_list_of_folders(folders)

        # Get the user's selection
        while True:
            try:
                selection = int(input("Enter the number of your choice: "))
                if selection <= len(folders) and 1 <= selection:
                    break
                else:
                    print("----------------------------------")
                    print("Invalid selection. Please try again.")
                    # Display folders again to aid in selection
                    print_list_of_folders(folders)
            except ValueError:
                print("----------------------------------")
                print("Invalid input. Please enter a number.")

        # Change the current directory to the selected folder
        base_folder = os.path.abspath(folders[selection - 1])
        os.chdir(base_folder)

        # Loop through all files in the base folder
        files_to_extract = [
            filename
            for filename in os.listdir(base_folder)
            if filename.endswith((".7z", ".zip"))
        ]

        if not files_to_extract:
            print("| ! | No archive files found to extract")
            continue

        # Create a ThreadPoolExecutor with 5 threads (adjust as needed)
        with ThreadPoolExecutor(max_workers=5) as executor:
        # Submit extraction tasks
            executor.map(lambda filename: extract_archive(filename, base_folder), files_to_extract)

            # Wait for all extraction tasks to complete
            executor.shutdown(wait=True)

        # Wait for extraction completion
        wait_for_extraction(files_to_extract, base_folder)

        for filename in os.listdir(base_folder):
            if filename.endswith((".7z", ".zip", ".txt")):
                try:
                    os.remove(os.path.join(base_folder, filename))
                    print(f"| X | Deleted - {filename}")
                except Exception as e:
                    print(f"| ! | Error deleting {filename}: {e}")

        # Ask user if they want to continue
        while True:
            cont = input("Do you want to go again? (y/n): ").lower()
            if cont in ["y", "n"]:
                break
            else:
                print("Invalid input. Please enter y or n.")
        if cont != "y":
            break


if __name__ == "__main__":
    main()