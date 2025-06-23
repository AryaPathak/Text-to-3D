import os
import requests
from PIL import Image
from io import BytesIO

IMAGE_TO_3D_APP_ID = "69543f29-4d41-4afc-7f29-3d51591f11eb"
OPENFABRIC_BASE_URL = "https://runtime.openfabric.network"

def convert_to_3d(image_path: str) -> str:
    # Read image bytes
    with open(image_path, "rb") as f:
        files = {
            "image": f
        }

        # POST to Openfabric runtime
        response = requests.post(
            f"{OPENFABRIC_BASE_URL}/v1/invoke/{IMAGE_TO_3D_APP_ID}",
            files=files
        )
        response.raise_for_status()
        result = response.json()

    # Get output 3D image
    image_data = result.get("outputs", {}).get("image")
    if not image_data:
        raise ValueError("No 3D image returned from Openfabric.")

    # Download and save it
    image = Image.open(BytesIO(requests.get(image_data).content))
    path = "data/models/generated_3d_image.png"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    image.save(path)
    return path
