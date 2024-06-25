<img src="ArchXtract.png" alt="ArchXtract Logo" style="float: right;">

# ArchXtract
### A Command Line Tool for Extracting Multiple Archives At Once
---
#### Written by Fred B | B1GBOOM - 2024


**What is ArchXtract?**
ArchXtract is a command line tool designed to expedite the processing of downloaded games for emulation. As an avid emulation enthusiast, I created this tool to simplify the tedious process of extracting and organizing game files.

**The script currently works as such:**
1. Select you options in the config.yaml and save
2. It lists the folders in the current directory and prompts the user to select one.
3. It loops through all files in the selected folder and extracts only the archive types you specified in the settings, using multithreading.
4. It waits for all extraction tasks to be completed.
5. It deletes any files you have specified in the settings

**Code Overview**
The code is written in Python and uses the following libraries:

* `os` for file system operations
* `py7zr` for 7z archive extraction
* `zipfile` for zip archive extraction
* `concurrent.futures` for multithreading
* `pyYAML` for config file

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

**Have Suggestions?**
Please feel free to open an issue - and I would be happy to hear you out and see what we can make happen, even if you don't want to commit code directly.

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
