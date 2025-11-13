 # Filepath Structurer & FBX Exporter (Now With Logging)

 ## Overview

This tool allows you to export an fbx and save it within a structured filepath under your computer username based on the environmental variables "PROJ", "TASK", and "ASSET", which are all values decided by the user. It also includes logging and error messages to inform the user of any mistakes or issues when executing, which are output as a text file also under your username.
 ## Usage

**Step 1** - In Git Bash, set each environmental variable with the following commands: 

>export PROJ=NameOfYourProject (Ex: Midterm, MyProject, Assignment1, etc.)

>export TASK=NameOfCurrentTask (Ex: Modeling, Layout, UVUnwrapping, etc.)

>export ASSET=NameOfYourAsset (Ex: Steve, MyBox, Box1, etc.)

**Step 2** - Enter the "maya" command in Git bash to open Maya

**Step 3** - Create your asset or load it into the current maya scene

**Step 4** - When you are ready to save your asset, open the "assignment5.py" file in the Maya Script Editor

**Step 5** - Run the script by hitting the "ExecuteAll" button

**Step 6** - Check the "log.txt" file to make sure that everything has executed properly

 ```python
assignment5

PROJ          # Environmental Variable containing the name for the project that the asset is being created for, used as the name for the first folder in the filepath

TASK          # Environmental Variable describing the current task being performed with the asset, used as the name for the second folder in the filepath

ASSET         # Environmental Variable containing the name for the asset, used as the name for the last folder in the filepath as well as the filename for the exported asset
 ```