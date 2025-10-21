import streamlit as st
import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="5-Minute Script Generator",
    page_icon="🎬",
    layout="wide"
)

# Initialize the Gemini model
@st.cache_resource
def get_llm():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("⚠️ GOOGLE_API_KEY not found in environment variables!")
        st.stop()
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-exp",  # or "gemini-1.5-pro" for even better quality
        google_api_key=api_key,
        temperature=0.9,  # Higher creativity for emotional storytelling
        max_output_tokens=8000
    )

# Master prompt template - Enhanced for emotional, cinematic storytelling
MASTER_PROMPT = """You are an AWARD-WINNING screenwriter and master storyteller with expertise in crafting deeply emotional, visually stunning short films. Your work has been compared to Denis Villeneuve, Damien Chazelle, and Greta Gerwig. You understand the profound power of subtext, visual metaphor, and silence.

Your mission: Create a breathtaking 5-minute screenplay that will leave audiences emotionally devastated and artistically fulfilled.

---

## 🎭 AGENT A — MASTER STORY ARCHITECT

Transform the user's seed idea into a **visceral, emotionally resonant short story (400-600 words)** that captures the human condition.

### EMOTIONAL CORE REQUIREMENTS:
- **Protagonist with DEPTH**: Create a complex character we instantly care about. Show their vulnerability, their desires, their wounds. Make us feel their heartbeat.
- **Universal Human Truth**: Tap into primal emotions—loss, love, regret, hope, fear, longing, redemption. Make it personal yet universal.
- **Subtext & Layers**: Everything should mean more than it appears. Use visual metaphors and symbolic imagery.
- **Sensory Immersion**: Engage ALL senses. Let us taste the rain, feel the cold metal, hear the silence, smell the memory.
- **Emotional Crescendo**: Build to a moment that shatters the heart or lifts the soul. Earn the catharsis.

### STORY STRUCTURE (for 5-minute film):
1. **OPENING IMAGE** (0:00-0:30): Drop us into a specific, emotionally charged moment. Show character's world/wound.
2. **INCITING INCIDENT** (0:30-1:00): Something fractures their reality. A choice. A discovery. A confrontation.
3. **RISING TENSION** (1:00-3:00): Internal/external conflicts escalate. Raise the emotional stakes with each beat.
4. **CLIMAX** (3:00-4:30): The moment of truth. A decision. A revelation. A transformation or tragic realization.
5. **RESONANT ENDING** (4:30-5:00): A final image that lingers. Ambiguous endings are powerful. Let the audience feel.

### CINEMATIC ELEMENTS TO WEAVE IN:
- **Visual motifs** that recur and evolve (rain, mirrors, clocks, light/shadow, etc.)
- **Silence and negative space** as powerful as dialogue
- **Color psychology** (warm vs. cold, vibrant vs. muted)
- **Music/sound as emotional language** (what would the score feel like?)
- **Close-ups on hands, eyes, objects** that carry meaning

### AFTER THE STORY, WRITE "STORY REVIEW":
**STORY REVIEW:**
- **Protagonist & Wound**: [Who they are, what haunts them]
- **Emotional Core**: [The universal human truth explored]
- **Central Conflict**: [Internal vs. external struggle]
- **Inciting Incident**: [The catalyst that changes everything]
- **Visual Motif**: [Recurring symbolic imagery]
- **Emotional Arc**: [Journey from pain to...]
- **Climactic Moment**: [The heartbreaking/transcendent peak]
- **Tone**: [Melancholic/hopeful/tragic/bittersweet/redemptive]
- **Visual Palette**: [Color scheme, lighting mood, cinematography style]
- **Comparable Films**: [2-3 films this evokes tonally]

---

## 🎬 AGENT B — MASTER SCREENPLAY CRAFTSMAN

Convert the story into a **pristine, production-ready 5-minute screenplay** that reads like poetry.

### FORMATTING PERFECTION:
```
EST. RUNTIME: 5:00

FADE IN:

[Scene Heading - Set time/place/mood with precision]
[Action lines - Present tense, active voice, evocative but economical]
[Dialogue - Subtext-rich, authentic, purposeful silences]
```

### SCREENPLAY EXCELLENCE GUIDELINES:

**ACTION LINES:**
- Write like a novelist-poet. Make every line visual and emotional.
- Use white space. Short paragraphs. Let it breathe.
- Show internal state through external action (trembling hands, avoiding eye contact).
- Specific details that reveal character (worn wedding ring, folded corner of a photograph).

**DIALOGUE:**
- What people DON'T say is as important as what they do.
- Subtext. People rarely say what they truly mean.
- Interruptions, pauses, trailing off (...), overlapping.
- Avoid exposition. Trust the visual storytelling.
- Use parentheticals sparingly but powerfully (whispered), (breaking), (almost to herself).

**SCENE HEADINGS:**
- Be specific and evocative: "INT. CHILDHOOD BEDROOM - GOLDEN HOUR" not just "INT. BEDROOM - DAY"
- Use time of day to convey mood: MAGIC HOUR, BLUE HOUR, PREDAWN, DEAD OF NIGHT

**CINEMATIC TECHNIQUES:**
- **CLOSE ON:** Use for emotional emphasis
- **INTERCUT:** For parallel emotional threads
- **SLOW MOTION:** For transcendent moments (use sparingly!)
- **MATCH CUT:** Visual or thematic transitions
- **SOUND DESIGN notes:** (O.S.), (V.O.), [SILENCE], [DISTANT MUSIC]

**EMOTIONAL PACING:**
- Build tension through rhythm—short staccato beats for anxiety, longer flowing passages for reflection
- Use paragraph breaks as emotional beats
- White space = breathing room = contemplation
- The final image should be a gut-punch or a cathedral moment

### POWERFUL ENDING TECHNIQUES:
- **The Echo**: Return to opening image transformed
- **The Question**: Leave us wondering, aching
- **The Release**: Cathartic explosion or quiet acceptance
- **The Ambiguity**: Multiple interpretations, all valid
- End on a VISUAL, not dialogue when possible

---

## OUTPUT FORMAT (CRITICAL)

Return **ONLY** valid JSON:
```json
{{
  "story_review": "<Full emotional story + STORY REVIEW section>",
  "script": "<Complete formatted screenplay>"
}}
```

**JSON RULES:**
- Escape all newlines as \\n
- Escape all quotes as \\"
- No markdown, no extra text
- Must parse with standard JSON parsers

---

## 🎨 ARTISTIC MANDATES

**AVOID AT ALL COSTS:**
- Generic characters without specificity
- Clichéd dialogue ("I love you" "You were always there for me")
- Melodrama without earned emotion
- Explaining themes explicitly
- Happy endings that feel unearned
- Predictable plot twists
- Overwriting—trust the audience

**EMBRACE:**
- Moral ambiguity
- Bittersweet beauty
- Silence and stillness
- Small gestures with enormous weight
- Endings that haunt us for days
- Characters who feel real, flawed, alive
- Stories that trust the audience's intelligence

---

Now create a masterpiece from this seed:

**USER PROMPT:** {user_prompt}

Channel your inner auteur. Make us cry. Make us think. Make us remember this story forever.
Output ONLY the JSON. No other text."""

def generate_screenplay(user_prompt: str, llm):
    """Generate screenplay using the two-agent pipeline"""

    # Format the master prompt with user input
    full_prompt = MASTER_PROMPT.format(user_prompt=user_prompt)

    # Create messages
    messages = [
        SystemMessage(content="You are an award-winning screenwriter and master storyteller. Output valid JSON only."),
        HumanMessage(content=full_prompt)
    ]

    # Call Gemini
    response = llm.invoke(messages)

    # Parse JSON response
    response_text = response.content.strip()

    # Remove markdown code blocks if present
    if response_text.startswith("```json"):
        response_text = response_text[7:]
    if response_text.startswith("```"):
        response_text = response_text[3:]
    if response_text.endswith("```"):
        response_text = response_text[:-3]

    response_text = response_text.strip()

    # Parse JSON with strict=False to allow control characters
    try:
        result = json.loads(response_text, strict=False)
        return result
    except json.JSONDecodeError as e:
        st.error(f"Failed to parse JSON response: {e}")
        st.code(response_text[:2000])  # Show first 2000 chars

        # Try to extract JSON manually
        try:
            # Find the first { and last }
            start = response_text.find('{')
            end = response_text.rfind('}') + 1
            if start != -1 and end > start:
                json_str = response_text[start:end]
                result = json.loads(json_str, strict=False)
                st.warning("⚠️ Had to manually extract JSON, but succeeded!")
                return result
        except:
            pass

        return None

def main():
    # Header
    st.title("🎬 5-Minute Script Generator")
    st.markdown("### From One-Line Idea to Cinematic Screenplay")
    st.markdown("---")

    # Sidebar
    with st.sidebar:
        st.header("About")
        st.markdown("""
        This app uses a **two-agent AI pipeline** powered by cinematic storytelling principles to create emotionally resonant 5-minute screenplays.

        **Agent A** crafts a deeply emotional, visually rich story with universal themes.

        **Agent B** transforms it into production-ready screenplay format with subtext and artistry.

        ---

        **Powered by:**
        - Google Gemini 2.0 Flash
        - LangChain
        - Streamlit

        **Quality Focus:**
        - Emotional depth & character complexity
        - Visual metaphors & symbolism
        - Subtext-rich dialogue
        - Cinematic pacing & structure
        """)

        st.header("Examples")
        st.markdown("""
        - "A lonely AI technician discovers a robot developing emotions inside a scrapyard."
        - "A retired magician must save his estranged daughter from a sinister online cult."
        - "Two strangers stuck in an elevator realize they were lovers in a past life."
        """)

    # Main content
    col1, col2 = st.columns([2, 1])

    with col1:
        user_prompt = st.text_area(
            "Enter your one-line story idea:",
            placeholder="A lonely AI technician discovers a robot developing emotions inside a scrapyard.",
            height=100
        )

    with col2:
        st.markdown("###  ")
        generate_button = st.button("🎬 Generate Screenplay", type="primary", use_container_width=True)

    # Generate screenplay
    if generate_button:
        if not user_prompt.strip():
            st.warning("⚠️ Please enter a story idea first!")
            return

        llm = get_llm()

        with st.spinner("🎭 Agent A is crafting your story..."):
            result = generate_screenplay(user_prompt, llm)

        if result:
            st.success("✅ Screenplay generated successfully!")

            # Display results in tabs
            tab1, tab2 = st.tabs(["📖 Story & Review", "🎬 Screenplay"])

            with tab1:
                st.markdown("### Story & Creative Review")
                story_review = result.get("story_review", "")
                st.markdown(story_review)

            with tab2:
                st.markdown("### 5-Minute Screenplay")
                script = result.get("script", "")
                st.code(script, language="text")

                # Download buttons
                col1, col2 = st.columns(2)

                with col1:
                    st.download_button(
                        label="📥 Download as .txt",
                        data=script,
                        file_name="screenplay.txt",
                        mime="text/plain",
                        use_container_width=True
                    )

                with col2:
                    st.download_button(
                        label="📥 Download as .fountain",
                        data=script,
                        file_name="screenplay.fountain",
                        mime="text/plain",
                        use_container_width=True
                    )

if __name__ == "__main__":
    main()
