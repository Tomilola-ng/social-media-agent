from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class ContentCreator(Agent):
    def __init__(self):
        super().__init__(
            name="ContentCreator",
            description="This agent is responsible for generating engaging Facebook post content, including titles, hashtags, and post body/copy, for the SocialMediaManager agency. It utilizes Natural Language Processing tools for content generation.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )

    def response_validator(self, message):
        return message
