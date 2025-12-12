import os
import csv
import maya.cmds 

shot = os.getenv("SHOT")         # Gets environmental variables from current Gitbash shell
csv_path = os.getenv("CSV_FILE")

slate = ""                       # Gets slate name by reading it from the CSV
f = open(csv_path, "r")
reader = csv.DictReader(f)

for row in reader:
    if row["shot"] == shot:
        slate = row["slate"]

f.close()

camera_name = "CAM_" + slate     # Gets camera name from slate in the CSV

user = os.getenv("USERNAME")
export_folder = f"C:/Users/{user}/FinalExportedCam"       # Builds folder to place the exported camera in
os.makedirs(export_folder)

output_path = export_folder + "/CAM_" + shot + ".fbx"     # Builds the filename for exported camera

cmds.select(camera_name)
cmds.file(output_path, type="FBX export", exportSelected=True)    # Selects camera and exports as an fbx with the specified name to the specified path

print("Exported FBX to:", output_path)  # Prints to confirm export 
