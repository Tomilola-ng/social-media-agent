from agency_swarm.tools import BaseTool
from pydantic import Field
import requests
import os
from datetime import datetime, timezone

# Assuming you have an environment variable for the Facebook access token
access_token = os.getenv("FACEBOOK_ACCESS_TOKEN")
page_id = os.getenv("FACEBOOK_PAGE_ID")
api_endpoint = f"https://graph.facebook.com/{page_id}/feed"

class PostSchedulerTool(BaseTool):
    """
    A tool to schedule Facebook posts to be published at optimal times to maximize engagement.
    It takes input parameters such as the post content, image URL, and desired posting time.
    """

    post_content: str = Field(
        ..., description="The content of the Facebook post."
    )
    image_url: str = Field(
        ..., description="The URL of the image to be included in the post."
    )
    scheduled_time: datetime = Field(
        ..., description="The desired time to publish the post, in UTC."
    )

    def run(self):
        """
        Schedules a post to be published on Facebook at the specified time.
        """
        # Convert the scheduled time to a Unix timestamp
        scheduled_unix_time = int(self.scheduled_time.replace(tzinfo=timezone.utc).timestamp())

        data = {
            "message": self.post_content,
            "published": False,  # Set to False to schedule the post
            "scheduled_publish_time": scheduled_unix_time,
            "access_token": access_token
        }

        # First, upload the image to get a photo ID
        photo_upload_endpoint = f"https://graph.facebook.com/{page_id}/photos"
        photo_data = {
            "url": self.image_url,
            "published": False,  # Do not publish immediately
            "access_token": access_token
        }

        photo_response = requests.post(photo_upload_endpoint, data=photo_data)

        if photo_response.status_code == 200:
            photo_id = photo_response.json().get('id')
            data["attached_media"] = [{"media_fbid": photo_id}]
        else:
            return f"Error uploading image: {photo_response.status_code} - {photo_response.text}"

        # Schedule the post
        response = requests.post(api_endpoint, data=data)

        if response.status_code == 200:
            return "Post successfully scheduled on Facebook."
        else:
            return f"Error scheduling post: {response.status_code} - {response.text}"

# Example usage:
# tool = PostSchedulerTool(
#     post_content="Check out this amazing view!",
#     image_url="https://example.com/path/to/image.jpg",
#     scheduled_time=datetime(2023, 10, 15, 14, 0, 0)  # Example UTC time
# )
# print(tool.run())