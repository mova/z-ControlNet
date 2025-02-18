import gradio as gr
import requests
import base64
import io
from PIL import Image
import numpy as np

# Convert base64 string to PIL Image
def decode_base64(image):
    image_bytes = base64.b64decode(image)
    image_stream = io.BytesIO(image_bytes)
    image = Image.open(image_stream)
    return image

# Queue the fastapi with the give prompt
def generate_image(prompt):
    response = requests.post("http://127.0.0.1:8000/generate", json={"prompt": prompt})
    return decode_base64(response.json()["image0"])

# Create the gradio interface
iface = gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(label="Enter Prompt"),
    outputs=gr.Image(label="Generated Image"),
    title="Demo for Business Unit - Synthetic Image Generator",
    description="Enter a prompt and generate an image using ControlNet.",
)

# Launch the interface
# Password for a minimum of security, to be changed
iface.launch(server_name="0.0.0.0", server_port=7860, auth=("admin", "zeissdemo"))
