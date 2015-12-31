import requests
from PIL import Image
from io import BytesIO


def get_image_size(url):
    data = requests.get(url).content
    img = Image.open(BytesIO(data))    
    return img.size
