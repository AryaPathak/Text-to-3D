import os
import requests
from PIL import Image
from io import BytesIO

# Constants
TEXT_TO_IMAGE_APP_ID = "f0997a01-d6d3-a5fe-53d8-561300318557"
OPENFABRIC_BASE_URL = "https://runtime.openfabric.network"

def generate_image(prompt: str) -> str:
    # Construct request payload using known schema (or fetched dynamically if preferred)
    payload = {
        "inputs": {
            "prompt": prompt
        }
    }

    # Send POST request to Openfabric runtime
    response = requests.post(
        f"{OPENFABRIC_BASE_URL}/v1/invoke/{TEXT_TO_IMAGE_APP_ID}",
        json=payload
    )
    response.raise_for_status()
    result = response.json()

    # Handle the output (assuming it's a base64-encoded image or direct URL)
    image_data = result.get("outputs", {}).get("image")
    if not image_data:
        raise ValueError("No image data returned from Openfabric.")

    # Decode and save the image
    image = Image.open(BytesIO(requests.get(image_data).content))
    path = "data/images/generated_image.png"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    image.save(path)
    return path
