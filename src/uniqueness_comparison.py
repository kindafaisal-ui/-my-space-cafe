import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from llm_integration import generate_content
from knowledge_base import KnowledgeBase
from prompt_templates import get_instagram_caption_prompt, get_tiktok_hook_prompt

GENERIC_PROMPTS = {
    "instagram_opening":   "Write an Instagram caption for a café that is opening soon.",
    "instagram_community": "Write an Instagram caption for a café about community and belonging.",
    "tiktok_concept":      "Write a TikTok video concept for a café targeting young people.",
}

def run_comparison():
    print("\n🔬 UNIQUENESS COMPARISON — My Space vs Generic AI")
    print("=" * 60)

    kb = KnowledgeBase(
        primary_path="../knowledge_base/primary",
        secondary_path="../knowledge_base/secondary"
    )
    pc = kb.get_primary_context()
    sc = kb.get_secondary_context()

    our_prompts = {
        "instagram_opening":   get_instagram_caption_prompt(pc, sc, "Pre-launch teaser — café opening soon"),
        "instagram_community": get_instagram_caption_prompt(pc, sc, "Community and belonging for young people"),
        "tiktok_concept":      get_tiktok_hook_prompt(pc, sc, "Why My Space is NOT just another coffee shop"),
    }

    results = {}
    for key in GENERIC_PROMPTS:
        print(f"\n📊 Testing: {key}")
        print("  Generating GENERIC...")
        results[key] = {"generic": generate_content(GENERIC_PROMPTS[key])}
        print("  Generating OURS...")
        results[key]["ours"] = generate_content(our_prompts[key])

    report = build_report(results)
    os.makedirs("../outputs", exist_ok=True)
    with open("../outputs/uniqueness_comparison.txt", "w", encoding="utf-8") as f:
        f.write(report)
    print("\n✅ Saved → outputs/uniqueness_comparison.txt")
    print(report)

def build_report(results):
    report = """
╔══════════════════════════════════════════════════════╗
║     UNIQUENESS COMPARISON — MY SPACE CAFÉ            ║
║     Generic Prompt  vs  Our Knowledge-Based System   ║
╚══════════════════════════════════════════════════════╝
"""
    labels = {
        "instagram_opening":   "TEST 1: Instagram — Opening Soon",
        "instagram_community": "TEST 2: Instagram — Community & Belonging",
        "tiktok_concept":      "TEST 3: TikTok Video Concept",
    }
    for key, label in labels.items():
        report += f"""
{'━'*56}
{label}
{'━'*56}

❌ GENERIC (plain ChatGPT prompt):
{results[key]['generic']}

✅ OUR SYSTEM (knowledge base injected):
{results[key]['ours']}
"""
    report += """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHY OURS IS DIFFERENT:
1. Uses real brand name & tagline (My Space Café)
2. Speaks to specific personas (Sara, Adam — 18-30)
3. References real market data (Starbucks decline, Gen Z trends)
4. Enforces brand voice rules (no hashtags, no corporate phrases)
5. Identity-focused not features-focused
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Same AI model. Completely different output.
The difference = knowledge base + prompt engineering.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    return report

if __name__ == "__main__":
    run_comparison()
