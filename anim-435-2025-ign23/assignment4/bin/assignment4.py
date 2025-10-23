import os
import maya.cmds as cmds

asset = os.getenv("ASSET")

cmds.polyCube(name=asset)
