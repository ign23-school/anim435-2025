import os
import logging
import maya.cmds
import json
import datetime

user = os.getenv("USERNAME")

log_file = f"C:/Users/{user}/assignment6_log.txt"
logger = logging.getLogger("FBXExportLogger")
logger.setLevel(logging.INFO)

if logger.hasHandlers():
    logger.handlers.clear()

handler = logging.FileHandler(log_file)
formatter = logging.Formatter("[%(asctime)s][%(filename)s][%(levelname)s] %(msg)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Starting FBX export script")

project = os.getenv("PROJ")
task = os.getenv("TASK")
asset = os.getenv("ASSET")

if not user or not project or not task or not asset:
    logger.error("One or more environmental variables are missing! Please restart shell and re-enter variables.")
else:
    logger.info(f"All environmental variables loaded successfully. USERNAME={user}")

    folder = f"C:/Users/{user}/{project}/{task}/{asset}"
    if not os.path.exists(folder):
        os.makedirs(folder)
        logger.info("Folder created successfully")
    else:
        logger.error("Folder already exists! Export may overwrite existing files.")

    output_path = os.path.join(folder, asset + ".fbx")

    if os.path.exists(output_path):
        logger.warning(f"FBX file already exists and may be overwritten: {output_path}")
    else:
        logger.info(f"FBX will be saved to: {output_path}")


    metadata_path = os.path.join(folder, asset + "_metadata.json")

    scene_metadata = {
        "username": user,
        "project": project,
        "task": task,
        "asset": asset,
        "maya_scene": maya.cmds.file(q=True, sn=True),
        "export_time": str(datetime.datetime.now())
    }

    f = open(metadata_path, 'w')
    json.dump(scene_metadata, f)
    f.close()

    logger.info(f"Metadata saved to: {metadata_path}")

    if not maya.cmds.pluginInfo("fbxmaya", query=True, loaded=True):
        logger.error("FBX plugin is not loaded! Please load 'fbxmaya' before exporting.")
    else:
        maya.cmds.select(all=True)
        logger.info("All objects selected for export")
        maya.cmds.file(output_path, type="FBX export", exportSelected=True)
        logger.info(f"Successfully exported FBX to: {output_path}")

logger.info(f"Log saved to: {log_file}")
print(f"Log saved to: {log_file}")
