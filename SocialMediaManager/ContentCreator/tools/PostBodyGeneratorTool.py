from agency_swarm.tools import BaseTool
from pydantic import Field
from transformers import pipeline

class PostBodyGeneratorTool(BaseTool):
    """
    A tool to generate engaging and creative body content for Facebook posts using Natural Language Processing techniques.
    It considers the context and theme of the post to produce relevant and captivating content.
    """

    post_theme: str = Field(
        ..., description="The theme or context of the Facebook post for which body content needs to be generated."
    )

    def run(self):
        """
        Generates engaging and creative body content for the given Facebook post theme.
        """
        # Initialize the text generation pipeline with a pre-trained model
        generator = pipeline('text-generation', model='gpt2')

        # Generate body content based on the post theme
        generated_content = generator(self.post_theme, max_length=100, num_return_sequences=1)

        # Extract the generated content
        body_content = generated_content[0]['generated_text'].strip()

        return body_content

# Example usage:
# tool = PostBodyGeneratorTool(post_theme="Exploring the benefits of sustainable living.")
# print(tool.run())