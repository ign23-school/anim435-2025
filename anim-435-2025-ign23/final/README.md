# Shot Setup and Camera Export Tools

## Description
These two tools demonstrate how to use **environment variables, CSV data, and Maya Python scripting** to automate shot-based workflows inside Maya.

Together, the scripts perform the following tasks:

### Script 1 - Shot Setup (`final_Script1.py`)
1. Reads information from a **CSV** file
2. Uses the **SHOT** environment variable to pick the active shot
3. Sets Maya's **timeline** based on the CSV (start_frame - end_frame)
4. Creates a camera named from the CSV:
```bash
CAM_<slate>
```

### Script 2 - Camera Export (`final_Script2.py`)

1. Uses the same **SHOT** and CSV file to find the matching slate
2. Looks for the camera created by the first script
3. Exports that camera as an **FBX** using the naming convention:
```bash
CAM_<shot>.fbx
```
4. Saves the FBX into a folder named:
```bash
C:/Users/<username>/FinalExportedCam/
```

## Required Environment Variables

Before launching Maya, set the following in **Git Bash**:
```bash
export SHOT=shot0020
export CSV_FILE="/c/Users/<username>/Desktop/shots.csv"
```
Maya **must be launched from the same Git Bash window** for these variables to be detected.

For example:
```bash
/c/Program\ Files/Autodesk/Maya2025/bin/maya.exe &
```

## How to Run
### 1. Prepare CSV file
It must be comma separated
```bash
shot,start_frame,end_frame,slate
shot0010,1001,1030,sc010_tk004_11032024
shot0020,1001,1054,sc010_tk005_11032024
shot0030,1001,1025,sc011_tk002_11042024
```
### 2. Prepare Environmental Variables in Gitbash, then open Maya from same Gitbash shell
```bash
export SHOT=shot0020
export CSV_FILE="{Filepath for your CSV}"
maya
```
### 3. Open script 1 in Maya's script editor and run it

Check the console for confirmation print statements to check for errors and make sure code was executed properly!

### 4. Open script 2 in Maya's script editor and run it

Check the console for confirmation print statements to check for errors and make sure code was executed properly!

### 5. Check for the exported camera fbx in the following folder
```bash
C:/Users/<username>/FinalExportedCam/
```