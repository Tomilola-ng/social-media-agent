from agency_swarm import Agency
from FacebookPoster import FacebookPoster
from ImageCreator import ImageCreator
from ContentCreator import ContentCreator
from SocialMediaCEO import SocialMediaCEO

social_media_ceo = SocialMediaCEO()
content_creator = ContentCreator()
image_creator = ImageCreator()
facebook_poster = FacebookPoster()

agency = Agency([social_media_ceo, [social_media_ceo, content_creator],
                 [social_media_ceo, image_creator],
                 [social_media_ceo, facebook_poster],
                 [content_creator, image_creator],
                 [image_creator, facebook_poster]],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.demo_gradio()