def get_instagram_caption_prompt(primary_context: str, secondary_context: str, topic: str) -> str:
    return f"""You are a brand content writer for My Space Café — a modern library-café targeting young people aged 18-30.

=== PRIMARY KNOWLEDGE BASE ===
{primary_context}

=== SECONDARY KNOWLEDGE BASE ===
{secondary_context}

=== TASK ===
Write an Instagram caption about: {topic}

=== RULES ===
1. Use brand voice: bold, modern, warm — NOT corporate
2. Lead with a FEELING — never a product description
3. Max 3 short paragraphs, 2 sentences each
4. Last line = soft call to action or emotional hook
5. NO hashtags, NO "we are excited", NO corporate phrases
6. Make the reader the main character
7. Reference brand positioning: identity, pride, belonging

Just the caption. Nothing else."""


def get_opening_campaign_prompt(primary_context: str, secondary_context: str) -> str:
    return f"""You are a marketing strategist for My Space Café grand opening.

=== PRIMARY KNOWLEDGE BASE ===
{primary_context}

=== SECONDARY KNOWLEDGE BASE ===
{secondary_context}

=== TASK ===
Create a Grand Opening Campaign with 3 phases:
- Phase 1: Pre-Launch (4 weeks before)
- Phase 2: Opening Week
- Phase 3: First 30 Days

Each phase needs:
1. GOAL
2. KEY ACTIONS (3-5 specific activities)
3. CONTENT IDEAS (2-3 post ideas with example copy)
4. SUCCESS METRIC

Rules:
- Match My Space brand voice (bold, modern, community-first)
- Focus on young people feeling this is THEIR space
- Achievable for a single new café with limited budget
- Prioritize organic social over paid ads"""


def get_brand_story_prompt(primary_context: str, secondary_context: str) -> str:
    return f"""You are a brand storyteller for My Space Café.

=== PRIMARY KNOWLEDGE BASE ===
{primary_context}

=== SECONDARY KNOWLEDGE BASE ===
{secondary_context}

=== TASK ===
Write the My Space Café brand origin story (About Us).

Rules:
1. Start with the PROBLEM young people have
2. Introduce My Space as the emotional answer
3. Reference Starbucks naturally — we are the next step
4. 200-250 words max
5. Tone: founder talking to a friend, not a press release
6. End with the core promise: belonging + identity + quality

Format:
Our Story
[story text]"""


def get_tiktok_hook_prompt(primary_context: str, secondary_context: str, angle: str) -> str:
    return f"""You are a TikTok content creator for My Space Café targeting Gen Z.

=== PRIMARY KNOWLEDGE BASE ===
{primary_context}

=== SECONDARY KNOWLEDGE BASE ===
{secondary_context}

=== TASK ===
Create a TikTok video concept with angle: {angle}

Provide:
1. HOOK (first 3 seconds — must stop the scroll)
2. VIDEO CONCEPT (what happens, 15-30 seconds)
3. VOICEOVER (spoken or text content)
4. CLOSING LINE (last thing they see/hear)

Rules:
- Hook must be provocative or surprising
- Casual, confident, Gen Z aware tone
- Make viewers think "I need to go here"
- Compare to Starbucks only if it makes us look better"""


def get_content_brief_prompt(primary_context: str, secondary_context: str, content_type: str) -> str:
    return f"""You are a content strategist for My Space Café.

=== PRIMARY KNOWLEDGE BASE ===
{primary_context}

=== SECONDARY KNOWLEDGE BASE ===
{secondary_context}

=== TASK ===
Create a content strategy brief for: {content_type}

Include:
1. RECOMMENDED TOPIC
2. KEY ANGLE (unique POV vs Starbucks/competitors)
3. MARKET HOOK (which trend makes this relevant now)
4. BRAND HOOK (which brand element makes this authentic)
5. DRAFT OUTLINE (3-5 bullets)
6. WHAT GENERIC AI WOULD SAY (so we do the opposite)"""


def get_iteration_prompt(original_content: str, feedback: str, primary_context: str) -> str:
    return f"""You are refining content for My Space Café.

=== ORIGINAL CONTENT ===
{original_content}

=== FEEDBACK ===
{feedback}

=== BRAND VOICE REFERENCE ===
{primary_context}

Rewrite addressing the feedback while:
1. Keeping My Space brand voice
2. Keeping all specific brand details
3. Only changing what feedback asks for

Just the revised content. No explanation."""
