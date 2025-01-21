from agency_swarm.agents import Agent


class FacebookPoster(Agent):
    def __init__(self):
        super().__init__(
            name="FacebookPoster",
            description="This agent is responsible for posting the generated content and images on Facebook for the SocialMediaManager agency. It utilizes the Facebook Graph API to ensure seamless posting of content to reach the target audience.",
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
