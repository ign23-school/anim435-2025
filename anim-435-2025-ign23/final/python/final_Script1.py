import os
import csv
import maya.cmds as cmds

def main():
    csv_path = os.getenv("CSV_FILE")
    shot_name = os.getenv("SHOT")

    # Check environment variables
    if not csv_path or not os.path.isfile(csv_path):
        print("ERROR: CSV_FILE environment variable is missing or invalid.")
        return

    if not shot_name:
        print("ERROR: SHOT environment variable not set.")
        return

    # Read CSV
    csv_file = open(csv_path, "r")
    reader = csv.DictReader(csv_file)

    selected_row = None

    for row in reader:
        if row["shot"] == shot_name:
            selected_row = row

    csv_file.close()


    if not selected_row:
        print("ERROR: Shot not found in CSV:", shot_name)
        return

    # Extract values
    start_frame = int(selected_row["start_frame"])
    end_frame = int(selected_row["end_frame"])
    slate_name = selected_row["slate"]

    # Set Maya timeline
    cmds.playbackOptions(min=start_frame, max=end_frame)
    cmds.currentTime(start_frame)

    print("Timeline set to:", start_frame, "-", end_frame)

    # Camera name
    cam_name = f"CAM_{slate_name}"

    # Check if camera already exists
    if cmds.objExists(cam_name):
        print("Camera already exists:", cam_name)
    else:
        cam, camShape = cmds.camera(name=cam_name)
        print("Camera created:", cam_name)

    print("Setup complete for", shot_name)

# Run script
if __name__ == "__main__":
    main()
