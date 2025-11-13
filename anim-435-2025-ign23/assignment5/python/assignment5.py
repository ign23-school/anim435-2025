import os
import logging
import maya.cmds

user = os.getenv("USERNAME")
project = os.getenv("PROJ")
task = os.getenv("TASK")
asset = os.getenv("ASSET")

folder = f"C:/Users/{user}/{project}/{task}/{asset}"

if not os.path.exists(folder):
    os.makedirs(folder)
    folder_exists = False
else:
    folder_exists = True

output_path = os.path.join(folder, asset + ".fbx")


log_file = f"C:/Users/{user}/log.txt"
logger = logging.getLogger("FBXExportLogger")
logger.setLevel(logging.INFO)

handler = logging.FileHandler(log_file)
formatter = logging.Formatter("[%(asctime)s][%(filename)s][%(levelname)s] %(msg)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Starting FBX export script")


if not user or not project or not task or not asset:
    logger.error("One or more environmental variables are missing! Please restart shell and re-enter variables.")
else:
    logger.info(f"All environmental variables loaded successfully. USERNAME={user}")


if folder_exists:
    logger.error("Folder already exists! Export may overwrite existing files.")
else:
    logger.info("Folder created successfully")


if os.path.exists(output_path):
    logger.warning(f"FBX file already exists and may be overwritten: {output_path}")
else:
    logger.info(f"FBX will be saved to: {output_path}")


if not cmds.pluginInfo("fbxmaya", query=True, loaded=True):
    logger.error("FBX plugin is not loaded! Please load 'fbxmaya' before exporting.")
else:
    cmds.select(all=True)
    logger.info("All objects selected for export")
    cmds.file(output_path, type="FBX export", exportSelected=True)
    logger.info(f"Successfully exported FBX to: {output_path}")


print("Exported FBX to:", output_path)
print(f"Log saved to: {log_file}")
