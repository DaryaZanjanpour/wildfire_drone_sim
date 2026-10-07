import re

filepath = r"C:\Users\User\wildfire_drone_sim\sim_sections\01_app_setup_and_configuration.py"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Fix apply_repeating_texture to use Panda3D Filename object
old = "    texture = app.loader.loadTexture(asset_path(texture_path))"
new = """    from panda3d.core import Filename
    texture = app.loader.loadTexture(Filename.fromOsSpecific(asset_path(texture_path)))"""

if old in content:
    content = content.replace(old, new)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Patched successfully!")
else:
    print("Pattern not found - may already be patched or code changed")
    print("Looking for similar lines...")
    for i, line in enumerate(content.split("\n")):
        if "loadTexture" in line and "asset_path" in line:
            print(f"Line {i}: {line}")
