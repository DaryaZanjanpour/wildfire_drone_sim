from PIL import Image
import os

grass_dir = r"C:\Users\User\wildfire_drone_sim\models\Grass"
grass2_dir = r"C:\Users\User\wildfire_drone_sim\models\Grass2"

os.makedirs(grass_dir, exist_ok=True)
os.makedirs(grass2_dir, exist_ok=True)

# Re-save Grass1.jpg as clean RGB
path1 = os.path.join(grass_dir, "Grass1.jpg")
try:
    img = Image.open(path1).convert("RGB")
    img.save(path1, "JPEG", quality=95)
    print(f"Re-saved {path1}")
except Exception as e:
    print(f"Could not open {path1}, creating placeholder: {e}")
    img = Image.new("RGB", (512, 512), color=(34, 139, 34))
    img.save(path1, "JPEG")
    print(f"Created placeholder {path1}")

# Re-save Grass2.jpg
path2 = os.path.join(grass_dir, "Grass2.jpg")
try:
    img = Image.open(path2).convert("RGB")
    img.save(path2, "JPEG", quality=95)
    print(f"Re-saved {path2}")
except Exception as e:
    img = Image.new("RGB", (512, 512), color=(34, 120, 34))
    img.save(path2, "JPEG")
    print(f"Created placeholder {path2}")

# Also fix Grass2 folder
path3 = os.path.join(grass2_dir, "Grass2.jpg")
try:
    img = Image.open(path3).convert("RGB")
    img.save(path3, "JPEG", quality=95)
    print(f"Re-saved {path3}")
except Exception as e:
    img = Image.new("RGB", (512, 512), color=(34, 120, 34))
    img.save(path3, "JPEG")
    print(f"Created placeholder {path3}")

print("All done!")
