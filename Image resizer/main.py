import os
from PIL import Image

image = Image.open('sunset.jpg')
print(f"Original size : {image.size}") # 5464x3640

sunset_resized = image.resize((400, 400))
sunset_resized.save('sunset_400.jpeg')