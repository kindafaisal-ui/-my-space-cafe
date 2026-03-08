from knowledge_base import KnowledgeBase
from prompt_templates import (
    get_instagram_caption_prompt,
    get_opening_campaign_prompt,
    get_brand_story_prompt,
    get_tiktok_hook_prompt,
    get_content_brief_prompt,
    get_iteration_prompt,
)
from llm_integration import generate_content


class ContentPipeline:

    def __init__(self, primary_path: str, secondary_path: str, provider: str = "openai"):
        print("=" * 50)
        print("STAGE 1: DOCUMENT — Loading Knowledge Bases")
        print("=" * 50)
        self.kb = KnowledgeBase(primary_path, secondary_path)
        self.provider = provider
        self.primary_context = self.kb.get_primary_context()
        self.secondary_context = self.kb.get_secondary_context()

    def monitor(self) -> dict:
        print("\n" + "=" * 50)
        print("STAGE 2: MONITOR — Content Strategy Brief")
        print("=" * 50)
        prompt = get_content_brief_prompt(
            self.primary_context, self.secondary_context,
            content_type="Instagram content for café grand opening"
        )
        brief = generate_content(prompt)
        print("\n📋 Content Brief:\n" + "-" * 40)
        print(brief)
        return {"brief": brief}

    def create_instagram_caption(self, topic: str) -> str:
        print("\n" + "=" * 50)
        print(f"PUBLISH — Instagram Caption: {topic}")
        print("=" * 50)
        prompt = get_instagram_caption_prompt(
            self.primary_context, self.secondary_context, topic=topic
        )
        content = generate_content(prompt)
        print("\n📸 Caption:\n" + "-" * 40)
        print(content)
        return content

    def create_opening_campaign(self) -> str:
        print("\n" + "=" * 50)
        print("PUBLISH — Grand Opening Campaign")
        print("=" * 50)
        prompt = get_opening_campaign_prompt(self.primary_context, self.secondary_context)
        content = generate_content(prompt, max_tokens=2000)
        print("\n🚀 Campaign:\n" + "-" * 40)
        print(content)
        return content

    def create_brand_story(self) -> str:
        print("\n" + "=" * 50)
        print("PUBLISH — Brand Story")
        print("=" * 50)
        prompt = get_brand_story_prompt(self.primary_context, self.secondary_context)
        content = generate_content(prompt)
        print("\n📖 Brand Story:\n" + "-" * 40)
        print(content)
        return content

    def create_tiktok_concept(self, angle: str) -> str:
        print("\n" + "=" * 50)
        print(f"PUBLISH — TikTok Concept")
        print("=" * 50)
        prompt = get_tiktok_hook_prompt(
            self.primary_context, self.secondary_context, angle=angle
        )
        content = generate_content(prompt)
        print("\n🎬 TikTok:\n" + "-" * 40)
        print(content)
        return content

    def iterate(self, original_content: str, feedback: str) -> str:
        print("\n" + "=" * 50)
        print("STAGE 5: ITERATE — Refining Content")
        print("=" * 50)
        prompt = get_iteration_prompt(original_content, feedback, self.primary_context)
        improved = generate_content(prompt)
        print("\n🔄 Improved:\n" + "-" * 40)
        print(improved)
        return improved
