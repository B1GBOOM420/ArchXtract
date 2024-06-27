import os
import py7zr
import zipfile
from concurrent.futures import ThreadPoolExecutor

def extract_archive(filename):
    try:
        if filename.endswith(".7z"):
            with py7zr.SevenZipFile(os.path.join(base_folder, filename), "r") as archive:
                archive.extractall(path=base_folder)
        elif filename.endswith(".zip"):
            with zipfile.ZipFile(os.path.join(base_folder, filename), "r") as archive:
                archive.extractall(path=base_folder)
        print(f"| + | Extracted - {filename}")
    except Exception as e:
        print(f"| ! | Error extracting {filename}: {e}")


if __name__ == "__main__":
    # Get a list of folders in the current directory
    folders = [f for f in os.listdir('.') if os.path.isdir(f)]

    # Print the list of folders
    print("Select a folder:")
    for i, folder in enumerate(folders):
        print(f"{i+1}. {folder}")

    # Get the user's selection
    selection = int(input("Enter the number of your choice: "))

    # Change the current directory to the selected folder
    base_folder = os.path.abspath(folders[selection-1])
    os.chdir(base_folder)

    # Loop through all files in the base folder
    files_to_extract = [filename for filename in os.listdir(base_folder) if filename.endswith((".7z", ".zip"))]

    if not files_to_extract:
        print("| ! | No archive files found to extract")
    

    # Create a ThreadPoolExecutor with 5 threads (adjust as needed)
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Submit extraction tasks
        executor.map(extract_archive, files_to_extract)

        # Wait for all extraction tasks to complete
        executor.shutdown(wait=True)

    for filename in os.listdir(base_folder):
        if filename.endswith((".7z", ".zip", ".txt")):
            try:
                os.remove(os.path.join(base_folder, filename))
                print(f"| X | Deleted - {filename}")
            except Exception as e:
                print(f"| ! | Error deleting {filename}: {e}")