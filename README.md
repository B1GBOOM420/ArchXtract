<img src="https://drive.google.com/file/d/1hz4_v3gEtYWlFS8sxDMKth2cxG5gu3uF/view?usp=sharing" alt="ArchXtract Logo" align="right">

# ArchXtract
### A Command Line Tool for Extracting Multiple Archives At Once
---
#### Written by Fred B | B1GBOOM - 2024


**What is ArchXtract?**
ArchXtract is a command line tool designed to expedite the processing of downloaded games for emulation. As an avid emulation enthusiast, I created this tool to simplify the tedious process of extracting and organizing game files.

**The script works as follows:**
1. It lists the folders in the current directory and prompts the user to select one.
2. It loops through all files in the selected folder and extracts 7z and zip archives using multithreading.
3. It waits for all extraction tasks to be completed.
4. It deletes the extracted archives and any txt files.
5. It asks the user if they want to continue.

**Code Overview**
The code is written in Python and uses the following libraries:

* `os` for file system operations
* `py7zr` for 7z archive extraction
* `zipfile` for zip archive extraction
* `concurrent.futures` for multithreading

**How Does it Work?**
ArchXtract is designed to process archive files in the following directory structure:
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

---

**Why Contribute?**
ArchXtract is a side project that I am passionate about, and it has the potential to benefit the emulation community. However, as a solo developer, I face limitations in terms of time and expertise. By contributing to ArchXtract, you can help:

* Improve the tool's functionality and performance
* Add support for more game formats and systems
* Enhance the user experience
* Share your knowledge and expertise with the community

**Contributing Guidelines**
If you're interested in contributing, please:

* Fork the repository
* Create a new branch for your feature or fix
* Submit a pull request with a clear description of your changes

**Thank You**
I appreciate your interest in ArchXtract and look forward to collaborating with you to make this tool a valuable resource for the emulation community.
