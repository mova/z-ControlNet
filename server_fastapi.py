from fastapi import FastAPI
from io import BytesIO
from PIL import Image
import base64
from inference import gen_img_from_prompt
import numpy as np
from pydantic import BaseModel

# The output of a request must be text, so we convert the array
# to an image and then decode the image to base64
def numpy_to_b64(image_array: np.ndarray, format="PNG") -> bytes:
    img = Image.fromarray(image_array)
    # Create an in-memory byte stream to store the image
    img_byte_io = BytesIO()
    img.save(img_byte_io, format=format)
    # Encode the byte stream to base64 string
    return base64.b64encode(img_byte_io.getvalue()).decode()

# Specify the structure of the input request for validation
class GenerateRequest(BaseModel):
    prompt: str

app = FastAPI()

# Define an endpoint to generate the images from a given prompt
@app.post("/generate")
async def generate_image(request: GenerateRequest):
    images = gen_img_from_prompt(prompt=request.prompt)
    return {f"image{i}": numpy_to_b64(img) for i, img in enumerate(images)}


# Define a root endpoint 
@app.get("/")
def home():
    return {"message": "Welcome to the Image Generator API"}
