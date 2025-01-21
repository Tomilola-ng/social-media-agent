from agency_swarm.tools import BaseTool
from pydantic import Field
import requests
import os

# Assuming you have an environment variable for the Facebook access token
access_token = os.getenv("FACEBOOK_ACCESS_TOKEN")
page_id = os.getenv("FACEBOOK_PAGE_ID")
api_endpoint = f"https://graph.facebook.com/{page_id}/photos"

class FacebookPostTool(BaseTool):
    """
    A tool to post content and images on Facebook using the Facebook Graph API.
    It takes input parameters such as the post content, image URL, and any additional metadata required for posting.
    """

    post_content: str = Field(
        ..., description="The content of the Facebook post."
    )
    image_url: str = Field(
        ..., description="The URL of the image to be included in the post."
    )

    def run(self):
        """
        Posts content and an image to Facebook using the Graph API.
        """
        data = {
            "url": self.image_url,
            "caption": self.post_content,
            "access_token": access_token
        }

        response = requests.post(api_endpoint, data=data)

        if response.status_code == 200:
            return "Post successfully published on Facebook."
        else:
            return f"Error: {response.status_code} - {response.text}"

# Example usage:
# tool = FacebookPostTool(
#     post_content="Check out this amazing view!",
#     image_url="https://example.com/path/to/image.jpg"
# )
# print(tool.run())