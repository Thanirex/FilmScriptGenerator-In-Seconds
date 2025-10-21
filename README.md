# 🎬 5-Minute Cinematic Script Generator

An AI-powered screenplay generator that transforms one-line ideas into **deeply emotional, visually stunning 5-minute screenplays** using advanced cinematic storytelling principles and a sophisticated two-agent LangChain pipeline.

> *"Make us cry. Make us think. Make us remember this story forever."*

## Features

- **Emotion-First Storytelling**: Creates screenplays with profound emotional depth, complex characters, and universal human truths
- **Cinematic Mastery**: Visual metaphors, subtext-rich dialogue, symbolic imagery, and auteur-level artistry
- **Two-Agent Architecture**: Master Story Architect + Master Screenplay Craftsman working in harmony
- **Production-Ready Output**: Industry-standard formatting with evocative scene headings, poetic action lines, and layered dialogue
- **Enhanced Prompt Engineering**: Inspired by Denis Villeneuve, Damien Chazelle, and Greta Gerwig's storytelling principles
- **Interactive Streamlit UI**: Beautiful, intuitive web interface
- **Export Options**: Download scripts as .txt or .fountain format

## What Makes This Different

Unlike generic script generators, this tool focuses on:

- **Emotional Resonance**: Every story explores loss, love, regret, hope, fear, longing, or redemption
- **Character Depth**: Complex protagonists with wounds, desires, and transformation arcs
- **Visual Storytelling**: Show don't tell - through trembling hands, avoiding eye contact, worn wedding rings
- **Subtext**: What characters DON'T say matters as much as what they do
- **Cinematic Techniques**: Visual motifs, color psychology, silence as power, symbolic imagery
- **Artful Endings**: Ambiguous, haunting, cathartic - endings that linger for days

## How It Works

1. **Input**: Enter a one-line story idea
2. **Agent A - Master Story Architect**:
   - Crafts a visceral, emotionally resonant 400-600 word short story
   - Develops complex characters with universal human truths
   - Weaves in visual motifs, sensory details, and symbolic imagery
   - Provides detailed story review (protagonist, emotional core, visual palette, comparable films)
3. **Agent B - Master Screenplay Craftsman**:
   - Converts story into pristine, production-ready screenplay format
   - Uses evocative scene headings (INT. CHILDHOOD BEDROOM - GOLDEN HOUR)
   - Writes action lines like a novelist-poet
   - Crafts subtext-rich dialogue with purposeful silences
   - Employs cinematic techniques (CLOSE ON, INTERCUT, sound design)
   - Creates a gut-punch or cathedral moment finale

## Installation

### Prerequisites
- Python 3.10 or higher
- Google AI API key ([Get one FREE here](https://aistudio.google.com/apikey))

### Setup

1. **Navigate to project directory**
   ```bash
   cd D:/Python\ Codes/Filmscriptgen
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   or with uv:
   ```bash
   uv pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your Google AI API key:
   ```
   GOOGLE_API_KEY=your_actual_google_api_key_here
   ```

## Usage

### Run the Streamlit App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Using the App

1. Enter your one-line story idea in the text area
2. Click "Generate Screenplay"
3. Wait for the AI agents to create your masterpiece (typically 30-90 seconds)
4. View the results in two tabs:
   - **Story & Review**: The emotionally rich story with detailed creative analysis
   - **Screenplay**: The beautifully formatted 5-minute script
5. Download your screenplay as .txt or .fountain

### Example Prompts

- "A lonely AI technician discovers a robot developing emotions inside a scrapyard."
- "A retired magician must save his estranged daughter from a sinister online cult."
- "Two strangers stuck in an elevator realize they were lovers in a past life."
- "A time-traveling journalist accidentally prevents her own birth."
- "An astronaut returns to Earth to find everyone has forgotten language."
- "A hospice nurse hears the same song in every patient's final moments."
- "A deaf composer writes their final symphony as they lose the memory of sound."

## Project Structure

```
Filmscriptgen/
├── app.py              # Main Streamlit application with enhanced prompts
├── main.py             # Original entry point (legacy)
├── .env.example        # Environment variable template
├── .gitignore          # Git ignore rules
├── pyproject.toml      # Project dependencies
├── requirements.txt    # Pip requirements
└── README.md           # This file
```

## Technical Details

### Technologies Used
- **Streamlit**: Web interface
- **LangChain**: Agent orchestration and prompt management
- **Google Gemini 2.0 Flash**: State-of-the-art creative AI (with optional Gemini 1.5 Pro for even higher quality)
- **Python-dotenv**: Environment variable management

### Agent Pipeline

The system uses a single Gemini invocation with a comprehensive master prompt that simulates two distinct expert agents:

**Agent A - Master Story Architect**
- Transforms seed idea into visceral, emotionally resonant 400-600 word story
- Focuses on universal human truths, complex characters, visual metaphors
- Structures story for 5-minute film pacing (opening image → inciting incident → climax → resonant ending)
- Provides detailed creative review including emotional core, visual palette, and comparable films

**Agent B - Master Screenplay Craftsman**
- Converts story into pristine, production-ready screenplay format
- Uses evocative scene headings that set mood (MAGIC HOUR, BLUE HOUR, PREDAWN)
- Writes poetic action lines with white space and emotional beats
- Crafts subtext-rich dialogue with purposeful pauses and silences
- Employs cinematic techniques (CLOSE ON, INTERCUT, sound design notes)
- Creates powerful endings using techniques like The Echo, The Question, The Release, The Ambiguity

### Output Format

The system returns JSON with two keys:
```json
{
  "story_review": "Full emotional story + detailed STORY REVIEW section",
  "script": "Formatted screenplay with EST. RUNTIME: 5:00 and cinematic formatting"
}
```

## Customization

### Adjust AI Parameters

Edit `app.py` (lines 25-30) to modify:
```python
ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",  # or "gemini-1.5-pro" for even better quality
    temperature=0.9,  # Higher creativity for emotional storytelling (0.0-1.0)
    max_output_tokens=8000
)
```

Available Gemini models:
- `gemini-2.0-flash-exp` - Fast, creative, excellent quality (recommended)
- `gemini-1.5-pro` - Premium quality, slower but more nuanced
- `gemini-1.5-flash` - Fastest responses, good quality

### Modify Storytelling Style

Edit the `MASTER_PROMPT` in `app.py` to:
- Adjust emotional intensity and themes
- Change story length (currently 400-600 words)
- Modify screenplay formatting preferences
- Add genre-specific instructions (noir, sci-fi, romance)
- Adjust tone guidelines (more hopeful vs. more tragic)

The prompt is meticulously crafted with sections on:
- Emotional core requirements
- Cinematic elements (visual motifs, color psychology)
- Screenplay excellence guidelines
- Powerful ending techniques
- Artistic mandates (what to avoid/embrace)

## Troubleshooting

### "GOOGLE_API_KEY not found"
- Ensure `.env` file exists in project root
- Get your FREE API key from https://aistudio.google.com/apikey
- Make sure the key is properly set in `.env` file

### "Failed to parse JSON response"
- The app includes robust JSON parsing with fallback extraction
- If this occurs, the raw response will be displayed for debugging
- Try regenerating or simplifying your prompt

### Generation time
- Typically 30-90 seconds for complete emotional screenplay
- Gemini 2.0 Flash is optimized for creative tasks
- Complex emotional narratives may take longer but are worth the wait

### Script feels too generic
- The enhanced prompt should produce deeply emotional content
- If not, try more specific/emotional seed ideas
- Consider adjusting temperature to 0.95 for maximum creativity
- Or switch to `gemini-1.5-pro` for premium quality

## Cinematic Storytelling Principles

This generator is built on professional screenwriting techniques:

**Emotional Architecture**
- Every story explores a universal human truth
- Characters have wounds, desires, and transformation arcs
- Subtext layers meaning beneath the surface

**Visual Language**
- Show internal state through external action
- Use recurring visual motifs (rain, mirrors, light/shadow)
- Employ color psychology and symbolic imagery

**Dialogue Craft**
- What people DON'T say matters most
- Use interruptions, pauses, trailing off
- Trust the visual storytelling - less is more

**Cinematic Pacing**
- Build emotional crescendos
- Use white space and silence as power
- End on visuals, not dialogue when possible

## Contributing

Feel free to open issues or submit pull requests for:
- Enhanced prompt engineering
- New storytelling techniques
- Genre-specific templates
- Additional export formats
- Bug fixes and improvements

## License

MIT License - feel free to use this project for any purpose.

## Acknowledgments

- Powered by [Google Gemini](https://deepmind.google/technologies/gemini/) - State-of-the-art creative AI
- Built with [LangChain](https://www.langchain.com/)
- UI by [Streamlit](https://streamlit.io/)

Inspired by the cinematic storytelling of Denis Villeneuve, Damien Chazelle, Greta Gerwig, Christopher Nolan, and other master filmmakers.

---

**Happy Screenwriting! May your stories move hearts and change minds.** 🎬
