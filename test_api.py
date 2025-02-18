# %%
import requests
import json
import base64
import matplotlib.pyplot as plt
import io
from PIL import Image
import numpy as np

response = requests.post(
    "http://127.0.0.1:8000/generate", json={"prompt": "An MRI scan of a torso"}
)


def decode_base64(image):
    image_bytes = base64.b64decode(image)
    image_stream = io.BytesIO(image_bytes)
    image = Image.open(image_stream)
    return np.array(image)


# %%
for name, image in response.json().items():
    plt.imshow(decode_base64(image))
    plt.axis(False)
    plt.title(name)
    plt.show()

# %%
