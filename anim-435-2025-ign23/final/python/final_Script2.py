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
cam, cam_shape = cmds.camera()
cmds.rename(cam, camera_name)

user = os.getenv("USERNAME")
export_folder = f"C:/Users/{user}/FinalExportedCam"
os.makedirs(export_folder)

output_path = export_folder + "/" + "CAM_" + shot + ".fbx"


cmds.select(camera_name)
cmds.file(output_path, type="FBX export", exportSelected=True)

print("Created camera:", camera_name)
print("Exported FBX to:", output_path)
