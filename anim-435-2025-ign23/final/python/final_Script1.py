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

    # ALL OF BELOW IS THE RESULT OF MAYA BEING INCREDIBLY DIFFICULT AND NEVER NAMING THINGS CORRECTLY

    cam_name = f"CAM_{slate_name}_cam"
    shape_name = f"{cam_name}Shape"

    # Delete transform + shape nodes if ANY exist
    to_delete = cmds.ls(f"{cam_name}*", long=True)
    to_delete += cmds.ls(f"{shape_name}*", long=True)
    to_delete = list(set(to_delete))

    if to_delete:
        print("Deleting nodes:", to_delete)
        cmds.delete(to_delete)

    # Create camera with temporary name
    temp_cam, temp_shape = cmds.camera()

    # Rename the transform FIRST
    final_cam = cmds.rename(temp_cam, cam_name)

    # Now safely find its shape
    shape = cmds.listRelatives(final_cam, shapes=True, fullPath=True)[0]

    # Rename the shape
    final_shape = cmds.rename(shape, shape_name)

    print("Camera created:", final_cam)
    print("Camera shape:", final_shape)

    print("Setup complete for", shot_name)

# Run script
if __name__ == "__main__":
    main()
