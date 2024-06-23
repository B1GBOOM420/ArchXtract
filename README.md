<img src="https://imgur.com/a/2rYi4TY" alt="ArchXtract Logo" style="float: right;">

# ArchXtract
### A Command Line Tool for Emulation Enthusiasts
#### Written by Fred B | B1GOOM

**What is ArchXtract?**
ArchXtract is a command line tool designed to expedite the processing of downloaded games for emulation. As an avid emulation enthusiast, I created this tool to simplify the tedious process of extracting and organizing game files.

**Why Contribute?**
ArchXtract is a side project that I am passionate about, and I believe it has the potential to benefit the emulation community. However, as a solo developer, I face limitations in terms of time and expertise. By contributing to ArchXtract, you can help:

* Improve the tool's functionality and performance
* Add support for more game formats and systems
* Enhance the user experience
* Share your knowledge and expertise with the community

**How Does it Work?**
ArchXtract is designed to process game files in the following directory structure:
```
+-- Root Dir
--- ArchXtract.py
|
+-- GameCube
| |
| +-- game.7z
| +-- game.7z
| +-- game.7z
|
+-- N64
| |
| +-- game.7z
| +-- game.7z
| +-- game.7z
|
+-- ECT
  +-- any
  +-- zip/7z
  +-- archive

```

The tool automates the extraction and organization of game files, making it easier to manage and run your emulated games.

**Code Overview**
The code is written in Python and uses the following libraries:

* `os` for file system operations
* `py7zr` for 7z archive extraction
* `zipfile` for zip archive extraction
* `concurrent.futures` for multithreading

The script works as follows:

1. It lists the folders in the current directory and prompts the user to select one.
2. It changes the current directory to the selected folder.
3. It loops through all files in the base folder and extracts 7z and zip archives using multithreading.
4. It waits for all extraction tasks to complete.
5. It deletes the extracted archives and any txt files.
6. It asks the user if they want to continue.

**Contributing Guidelines**
If you're interested in contributing, please:

* Fork the repository
* Create a new branch for your feature or fix
* Submit a pull request with a clear description of your changes

**Thank You**
I appreciate your interest in ArchXtract, and I look forward to collaborating with you to make this tool a valuable resource for the emulation community.
