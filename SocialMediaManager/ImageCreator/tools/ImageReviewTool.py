from agency_swarm.tools import BaseTool
from pydantic import Field
from PIL import Image, ImageEnhance
import requests
from io import BytesIO

class ImageReviewTool(BaseTool):
    """
    A tool to review and refine generated images to ensure they meet quality standards and are visually appealing.
    It takes an image URL as input and returns a refined image or feedback on the image quality.
    """

    image_url: str = Field(
        ..., description="The URL of the image to be reviewed and refined."
    )

    def run(self):
        """
        Reviews and refines the image from the provided URL.
        """
        try:
            # Download the image from the URL
            response = requests.get(self.image_url)
            response.raise_for_status()  # Raise an error for bad responses

            # Open the image
            image = Image.open(BytesIO(response.content))

            # Perform basic quality checks
            if image.size[0] < 500 or image.size[1] < 500:
                return "Image is too small. Minimum size is 500x500 pixels."

            # Enhance the image (e.g., increase brightness and contrast)
            enhancer = ImageEnhance.Brightness(image)
            image = enhancer.enhance(1.2)  # Increase brightness by 20%

            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(1.2)  # Increase contrast by 20%

            # Save the refined image to a BytesIO object
            output = BytesIO()
            image.save(output, format='JPEG')
            output.seek(0)

            # Return the refined image as a byte stream
            return output

        except requests.exceptions.RequestException as e:
            return f"Error downloading image: {e}"
        except Exception as e:
            return f"Error processing image: {e}"

# Example usage:
# tool = ImageReviewTool(image_url="https://example.com/path/to/image.jpg")
# refined_image = tool.run()
# if isinstance(refined_image, BytesIO):
#     with open("refined_image.jpg", "wb") as f:
#         f.write(refined_image.read())
# else:
#     print(refined_image)