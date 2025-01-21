from agency_swarm.agents import Agent


class SocialMediaCEO(Agent):
    def __init__(self):
        super().__init__(
            name="SocialMediaCEO",
            description="This agent oversees the overall operations of the SocialMediaManager agency, coordinates between agents, and ensures the agency's goals are met. It does not require specific tools or APIs but is responsible for coordinating the use of other agents' tools.",
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
