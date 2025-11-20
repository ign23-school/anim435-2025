 # Filepath Structurer & FBX Exporter (Now With Logging and Metadata)

 ## Overview

This tool allows you to export an fbx and save it within a structured filepath under your computer username based on the environmental variables "PROJ", "TASK", and "ASSET", which are all values decided by the user. 

It also includes logging and error messages to inform the user of any mistakes or issues when executing, as well as metadata to inform the user of valuable info such as the export time and the name/filepath of the maya scene the asset was exported from. The logging and the metadata are output as text files titled "assignment6_log.txt" and "(NameOfYourAsset)_metadata.json" respectively.
 ## Usage

**Step 1** - In Git Bash, set each environmental variable with the following commands: 

>export PROJ=NameOfYourProject (Ex: Midterm, MyProject, Assignment1, etc.)

>export TASK=NameOfCurrentTask (Ex: Modeling, Layout, UVUnwrapping, etc.)

>export ASSET=NameOfYourAsset (Ex: Steve, MyBox, Box1, etc.)

**Step 2** - Enter the "maya" command in Git bash to open Maya

**Step 3** - Create your asset or load it into the current maya scene

**Step 4** - When you are ready to save your asset, open the "assignment6.py" file in the Maya Script Editor

**Step 5** - Run the script by hitting the "ExecuteAll" button

**Step 6** - Check the "assignment6_log.txt" file to make sure that everything has executed properly, it can be found under your Username folder

**Step 7** - Check the "(NameOfYourAsset)_metadata.json" file to find info about the export time, Maya filepath, and enivronmental variables used in export, it can be found in the same folder as your exported asset

 ```python
assignment6

PROJ          # Environmental Variable containing the name for the project that the asset is being created for, used as the name for the first folder in the filepath

TASK          # Environmental Variable describing the current task being performed with the asset, used as the name for the second folder in the filepath

ASSET         # Environmental Variable containing the name for the asset, used as the name for the last folder in the filepath as well as the filename for the exported asset
 ```