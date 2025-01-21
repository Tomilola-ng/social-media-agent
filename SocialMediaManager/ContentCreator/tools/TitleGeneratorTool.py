from agency_swarm.tools import BaseTool
from pydantic import Field
from transformers import pipeline

class TitleGeneratorTool(BaseTool):
    """
    A tool to generate creative and engaging titles for Facebook posts using Natural Language Processing techniques.
    It takes into account the context and theme of the post to produce relevant and captivating titles.
    """

    post_content: str = Field(
        ..., description="The content of the Facebook post for which a title needs to be generated."
    )

    def run(self):
        """
        Generates a creative and engaging title for the given Facebook post content.
        """
        # Initialize the text generation pipeline with a pre-trained model
        generator = pipeline('text-generation', model='gpt2')

        # Generate a title based on the post content
        generated_titles = generator(self.post_content, max_length=15, num_return_sequences=1)

        # Extract the generated title
        title = generated_titles[0]['generated_text'].strip()

        return title

# Example usage:
# tool = TitleGeneratorTool(post_content="Exciting new features in our latest product update!")
# print(tool.run())