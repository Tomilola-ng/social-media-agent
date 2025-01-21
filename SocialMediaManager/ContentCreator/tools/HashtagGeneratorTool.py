from agency_swarm.tools import BaseTool
from pydantic import Field
from transformers import pipeline

class HashtagGeneratorTool(BaseTool):
    """
    A tool to generate relevant and trending hashtags for Facebook posts using Natural Language Processing techniques.
    It analyzes the post content to suggest hashtags that enhance visibility and engagement.
    """

    post_content: str = Field(
        ..., description="The content of the Facebook post for which hashtags need to be generated."
    )

    def run(self):
        """
        Generates relevant and trending hashtags for the given Facebook post content.
        """
        # Initialize the text generation pipeline with a pre-trained model
        generator = pipeline('text-generation', model='gpt2')

        # Generate text based on the post content to suggest hashtags
        generated_text = generator(self.post_content + " #", max_length=50, num_return_sequences=1)

        # Extract hashtags from the generated text
        hashtags = [word for word in generated_text[0]['generated_text'].split() if word.startswith('#')]

        # Return a list of unique hashtags
        return list(set(hashtags))

# Example usage:
# tool = HashtagGeneratorTool(post_content="Discover the latest trends in technology and innovation.")
# print(tool.run())