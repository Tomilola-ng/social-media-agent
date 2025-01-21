from agency_swarm.agents import Agent


class ImageCreator(Agent):
    def __init__(self):
        super().__init__(
            name="ImageCreator",
            description="This agent is responsible for creating images that match each Facebook post using the DALL-E 3 API. It ensures that the images are visually appealing and align with the content generated by the ContentCreator for the SocialMediaManager agency.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )

    def response_validator(self, message):
        return message
