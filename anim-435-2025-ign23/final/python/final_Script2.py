import os
import csv
import maya.cmds 

shot = os.getenv("SHOT")
csv_path = os.getenv("CSV_FILE")

slate = ""
f = open(csv_path, "r")
reader = csv.DictReader(f)
for row in reader:
    if row["shot"] == shot:
        slate = row["slate"]
f.close()

camera_name = "CAM_" + slate

if not cmds.objExists(camera_name):
    print("ERROR: Camera does not exist:", camera_name)
    return

user = os.getenv("USERNAME")
export_folder = f"C:/Users/{user}/FinalExportedCam"
os.makedirs(export_folder, exist_ok=
