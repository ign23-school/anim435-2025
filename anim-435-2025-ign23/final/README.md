# Shot Setup and Camera Export Tools

## Description
These two tools demonstrate how to use **environment variables, CSV data, and Maya Python scripting** to automate shot-based workflows inside Maya.

Together, the scripts perform the following tasks:

### Script 1 - Shot Setup (`final_shot_setup.py`)
1. Reads information from a **CSV** file
2. Uses the **SHOT** environment variable to pick the active shot
3. Sets Maya's **timeline** based on the CSV (start_frame - end_frame)
4. Creates a camera named from the CSV:
```bash
CAM_<slate>
```

### Script 2 - Camera Export (`final_export_cam_fbx.py`)



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
### 1. 
### 2. 
### 3. 
### 4. 
### 5. 

