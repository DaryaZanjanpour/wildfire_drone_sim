filepath = r"C:\Users\User\wildfire_drone_sim\sim_sections\01_app_setup_and_configuration.py"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Add models path to panda3d after app is created
old = "app = ShowBase()  #create 3D program window and sets up the engine"
new = """app = ShowBase()  #create 3D program window and sets up the engine
app.getModelPath().prependDirectory(str(PROJECT_ROOT))
app.getModelPath().prependDirectory(str(PROJECT_ROOT / "models"))"""

if old in content:
    content = content.replace(old, new)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Patched successfully!")
else:
    print("Already patched or pattern not found")
