from agency_swarm.tools import BaseTool
from pydantic import Field
import requests
import os

# Use the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")
api_endpoint = "https://api.openai.com/v1/images/generations"

class ImageGenerationTool(BaseTool):
    """
    A tool to generate images using the DALL-E 3 API that match the theme and message of each Facebook post.
    It takes input parameters such as the theme or description of the image to be generated and returns the generated image.
    """

    image_description: str = Field(
        ..., description="The theme or description of the image to be generated."
    )

    def run(self):
        """
        Generates an image based on the provided description using the DALL-E 3 API.
        """
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "prompt": self.image_description,
            "n": 1,  # Number of images to generate
            "size": "1024x1024"  # Size of the generated image
        }

        response = requests.post(api_endpoint, headers=headers, json=data)

        if response.status_code == 200:
            image_url = response.json()['data'][0]['url']
            return image_url
        else:
            return f"Error: {response.status_code} - {response.text}"

# Example usage:
# tool = ImageGenerationTool(image_description="A serene landscape with mountains and a river at sunset.")
# print(tool.run())