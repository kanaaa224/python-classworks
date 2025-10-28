from PIL import Image
from pathlib import Path

BASE_DIR = Path(__file__).parent

img_path = BASE_DIR / "images" / "ship.png"
ico_path = BASE_DIR / "images" / "icon.ico"

img = Image.open(img_path)
img.save(ico_path, sizes=[(16, 16), (32, 32), (48, 48), (256, 256)])