"""
main.py
-------
AI Content Creator — My Space Café
Run this to generate all brand content through the full pipeline.

Usage:
    cd src
    python main.py
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from content_pipeline import ContentPipeline


def save_output(filename: str, content: str):
    os.makedirs("../outputs", exist_ok=True)
    filepath = f"../outputs/{filename}"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  💾 Saved → outputs/{filename}")


def main():
    print("\n☕  MY SPACE CAFÉ — AI Content Creator")
    print("=" * 50)

    # ── Configuration ──────────────────────────────────
    PRIMARY_KB   = "../knowledge_base/primary"
    SECONDARY_KB = "../knowledge_base/secondary"
    PROVIDER     = "openai"          # using OpenAI API
    # ───────────────────────────────────────────────────

    # Initialize pipeline — loads all knowledge base docs
    pipeline = ContentPipeline(PRIMARY_KB, SECONDARY_KB, provider=PROVIDER)

    # ── STAGE 2: MONITOR ────────────────────────────────
    brief = pipeline.monitor()
    save_output("content_brief.txt", brief["brief"])

    # ── STAGE 3-4: PUBLISH ──────────────────────────────

    # Instagram captions
    caption_prelaunch = pipeline.create_instagram_caption(
        topic="Pre-launch teaser — My Space Café is coming soon"
    )
    caption_opening = pipeline.create_instagram_caption(
        topic="Opening day — doors open for the first time"
    )
    save_output("instagram_captions.txt",
        f"=== PRE-LAUNCH CAPTION ===\n{caption_prelaunch}\n\n"
        f"=== OPENING DAY CAPTION ===\n{caption_opening}"
    )

    # Brand story
    brand_story = pipeline.create_brand_story()
    save_output("brand_story.txt", brand_story)

    # TikTok concept
    tiktok = pipeline.create_tiktok_concept(
        angle="Why My Space is NOT just another coffee shop"
    )
    save_output("tiktok_concept.txt", tiktok)

    # Full grand opening campaign
    campaign = pipeline.create_opening_campaign()
    save_output("opening_campaign.txt", campaign)

    # ── STAGE 5: ITERATE ────────────────────────────────
    improved = pipeline.iterate(
        original_content=caption_opening,
        feedback="Make it more energetic. Mention the people in the room — not just the space. Keep under 120 words."
    )
    save_output("caption_improved.txt", improved)

    print("\n" + "=" * 50)
    print("✅  ALL CONTENT GENERATED!")
    print("📁  Check the /outputs folder for all files.")
    print("=" * 50)
    print("\nNext step: run uniqueness_comparison.py for your presentation proof.")
    print("    python uniqueness_comparison.py")


if __name__ == "__main__":
    main()
