import os
import py7zr
import zipfile
from concurrent.futures import ThreadPoolExecutor
import yaml
import time
import rarfile
import gzip
import tarfile


def extract_archive(filename):
    try:
        if filename.endswith(".7z") and config["extract_7z_archives"]:
            with py7zr.SevenZipFile(
                os.path.join(base_folder, filename), "r"
            ) as archive:
                archive.extractall(path=base_folder)
            print(f"| + | Extracted - {filename}")
            
            
        elif filename.endswith(".zip") and config["extract_zip_archives"]:
            with zipfile.ZipFile(os.path.join(base_folder, filename), "r") as archive:
                archive.extractall(path=base_folder)
            print(f"| + | Extracted - {filename}")
            
            
        elif filename.endswith(".rar") and config["extract_rar_archives"]:
            with rarfile.RarFile(os.path.join(base_folder, filename)) as archive:
                archive.extractall(path=base_folder)
            print(f"| + | Extracted - {filename}")
        
        elif filename.endswith(".gz") and config["extract_gz_archives"]:
            with gzip.GzipFile(os.path.join(base_folder, filename)) as gzipfile:
                with open(
                    os.path.join(base_folder, os.path.basename(filename[:-3])), "wb"
                ) as file:
                    file.write(gzipfile.read())
            print(f"| + | Extracted - {filename}")

        elif filename.endswith(".tar") and config["extract_tar_archives"]:
            with tarfile.TarFile(os.path.join(base_folder, filename)) as tf:
                tf.extractall(
                    base_folder,
                    members=[
                        member
                        for member in tf.getmembers()
                        if not os.path.exists(os.path.join(base_folder, member.name))
                    ],
                )
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


def delete_file_function(base_folder, filename):
    try:
        os.remove(os.path.join(base_folder, filename))
        print(f"| X | Deleted - {filename}")
    except Exception as e:
        print(f"| ! | Error deleting {filename}: {e}")


if __name__ == "__main__":
    # Load the YAML file
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # Get a list of folders in the current directory
    folders = [f for f in os.listdir(".") if os.path.isdir(f)]

    # Print the list of folders
    print("Select a folder:")
    for i, folder in enumerate(folders):
        print(f"{i+1}. {folder}")

    # Get the user's selection
    selection = int(input("Enter the number of your choice: "))

    # Change the current directory to the selected folder
    base_folder = os.path.abspath(folders[selection - 1])
    os.chdir(base_folder)

    # Loop through all files in the base folder
    files_to_extract = [
        filename
        for filename in os.listdir(base_folder)
        if (filename.endswith(".7z") and config["extract_7z_archives"])
        or (filename.endswith(".zip") and config["extract_zip_archives"])
        or (filename.endswith(".rar") and config["extract_rar_archives"])
        or (filename.endswith(".tar") and config["extract_tar_archives"])
        or (filename.endswith(".gz") and config["extract_gz_archives"])
    ]

    if not files_to_extract:
        print("| ! | No archive files found matching your settings")

    # Create a ThreadPoolExecutor with 5 threads (adjust as needed)
    with ThreadPoolExecutor(max_workers=config["max_workers"]) as executor:
        # Submit extraction tasks
        executor.map(extract_archive, files_to_extract)

        # Wait for all extraction tasks
        executor.shutdown(wait=True)

        # Wait for extraction completion
        wait_for_extraction(files_to_extract, base_folder)

    # Deletion options 
    if config["delete_7z_archives"]:
        for filename in os.listdir(base_folder):
            if filename.endswith(".7z"):
                delete_file_function(base_folder, filename)

    if config["delete_zip_archives"]:
        for filename in os.listdir(base_folder):
            if filename.endswith(".zip"):
                delete_file_function(base_folder, filename)
                
    if config["delete_rar_archives"]:
        for filename in os.listdir(base_folder):
            if filename.endswith(".rar"):
                delete_file_function(base_folder, filename)
                
    if config["delete_tar_archives"]:
        for filename in os.listdir(base_folder):
            if filename.endswith(".tar"):
                delete_file_function(base_folder, filename)
                
    if config["delete_gz_archives"]:
        for filename in os.listdir(base_folder):
            if filename.endswith(".gz"):
                delete_file_function(base_folder, filename)

    if config["delete_txt_files"]:
        for filename in os.listdir(base_folder):
            if filename.endswith(".txt"):
                delete_file_function(base_folder, filename)
