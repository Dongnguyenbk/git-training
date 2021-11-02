from typing import Any, Tuple
from PIL import Image

def create_thumbnail(image: Any, size: Tuple[int, int]):
	return image.thumbnail(size)