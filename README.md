```
    .        +           .          _..._          .           +        .
         ┌─────────┐   *          .' .::::.          *   ┌─────────┐
    *    │ 33      │       .     :  ::::::::     .       │      31 │    *
         │   KEY   │             :  ::::::::             │   SUN   │
    .    │      8♦ │    +        '. '::::::'  .    +     │ A♦      │    .
         └─────────┘       .       `'-..-'`       .      └─────────┘

  ██╗     ███████╗███╗   ██╗ ██████╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗██████╗
  ██║     ██╔════╝████╗  ██║██╔═══██╗██╔══██╗████╗ ████║██╔══██╗████╗  ██║██╔══██╗
  ██║     █████╗  ██╔██╗ ██║██║   ██║██████╔╝██╔████╔██║███████║██╔██╗ ██║██║  ██║
  ██║     ██╔══╝  ██║╚██╗██║██║   ██║██╔══██╗██║╚██╔╝██║██╔══██║██║╚██╗██║██║  ██║
  ███████╗███████╗██║ ╚████║╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║██████╔╝
  ╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝

                     ─────────  W   I   T   C   H  ─────────
                 thirty-six cards · one honest witch · no incense
    .        +           .          *               .           +        .
```

## ⬇️ Download

### **[Download lenormand-witch.zip](https://github.com/Jingquank/lenormand-witch/releases/latest/download/lenormand-witch.zip)**

The complete skill, ready to upload. The zip holds a single `lenormand-witch/` folder with `SKILL.md` inside.

**Claude.ai / Claude desktop app**

1. Turn on code execution: **Settings → Capabilities → Code execution and file creation**. Skills don't run without it. (Team/Enterprise: an owner enables it in organization settings.)
2. Go to **Customize → Skills** ([claude.ai/customize/skills](https://claude.ai/customize/skills)), click **+** → **Create skill** → **Upload a skill**, and choose `lenormand-witch.zip`. Don't unzip it first.
3. Make sure the skill is toggled on, then ask for a reading: *"Draw three cards for me."*

**Claude Code**

```bash
unzip lenormand-witch.zip -d ~/.claude/skills/
```

This gives you `~/.claude/skills/lenormand-witch/SKILL.md`. Start a new session and the skill loads automatically.

# Lenormand Witch

An agent skill that performs **Lenormand cartomancy readings** in the voice of a grounded, tired, matter-of-fact witch (modeled on Misty from *Cyberpunk 2077*, though she never says so). No incense, no "the universe is guiding you". She deals real random cards, reads them honestly, pushes back on questions the cards can't answer, and puts every reading on a bilingual, animated **reading table** web page.

> The cards are a method, not a faith. Thirty-six images and honest randomness give your associations a structure to work on. They can show a dynamic, a cause, a pressure, a path. They can't give you a lottery number.

---

## Contents

- [Features](#features)
- [Installation](#installation)
- [Usage examples](#usage-examples)
- [File structure](#file-structure)
- [The render script](#the-render-script)
- [Reading JSON at a glance](#reading-json-at-a-glance)
- [Notes and limitations](#notes-and-limitations)

---

## Features

**Real draws.** Cards are dealt with Python's `secrets.SystemRandom`, without replacement. The agent is told never to invent cards; if the command can't run, the reading stops.

**Four spreads, plus custom counts.**

| Spread | Cards | Best for |
| --- | --- | --- |
| 3-card line | 3 | "What should I do about…" |
| 5-card line | 5 | A situation with a past and a direction |
| 9-card square | 9 | "Why…" questions with several moving parts |
| Grand Tableau (9 × 4) | 36 | The full picture: houses, significator, corners, diagonals, mirrors, optional knighting |
| Custom | any | Read as an extended line (chat only) |

**Question shaping.** Yes/no, timing, lottery-number, password and "what is he thinking" questions get reshaped into ones the cards can actually answer ("What is standing between me and passing?" instead of "Will I pass?"). Some questions are always reshaped; others are reshaped once and then read as asked if you insist.

**A consistent voice.** Composed, written register. Short sentences. Honest about Coffin, Scythe, Mice and the rest; when heavy news lands she gets quieter, not louder. Dry humor only when the table is actually absurd. Detailed Do/Don't examples in English and Chinese live in `SKILL.md`.

**Bilingual.** Replies match the querent's language per message (Chinese in, Chinese out; English in, English out). The reading page carries both languages and a toggle.

**Photo readings.** Send a photo of cards on a table and the photo *is* the reading: the agent identifies cards and layout (cropping and zooming wide shots if needed) and interprets them without re-dealing.

**Safety rails.** Medical, legal, financial and mental-health questions get a one-line "not a substitute for a professional" note. Mentions of crisis or self-harm make the agent briefly break character and point to real help first.

**Reading table page.** A self-contained HTML page (Green Glyphs Lenormand deck, LT Superior Serif font, all embedded) that shuffles, deals face down, flips the cards in order and then reveals the written reading. Viewers can:

- open any card for a focused view (meaning, position reading, reading of each adjacent pair)
- click inline card chips in the text
- switch between Chinese and English
- switch between light and dark mode
- export the whole reading as a PNG

Each section of the reading carries an honest **fortune grade**: 大吉 · 中吉 · 小吉 · 吉 · 末吉 · 凶 · 大凶.

---

## Installation

The skill is a plain folder with a `SKILL.md` at its root, following the Agent Skills format. The only runtime dependency is **Python 3** (standard library only) for drawing cards and rendering the page.

### Claude Code

Personal skill (available in every project):

```bash
git clone https://github.com/Jingquank/lenormand-witch.git ~/.claude/skills/lenormand-witch
```

Project skill (shared with everyone on the repo):

```bash
git clone https://github.com/Jingquank/lenormand-witch.git .claude/skills/lenormand-witch
```

Restart Claude Code (or start a new session). The skill triggers automatically on things like "draw three cards", "发牌", or a photo of a spread. You can check that it loaded by asking *"What skills are available?"*.

### Claude.ai / Claude desktop app

1. [Download the prebuilt zip](https://github.com/Jingquank/lenormand-witch/releases/latest/download/lenormand-witch.zip), or zip the folder yourself so that `lenormand-witch/SKILL.md` is inside the archive:
   ```bash
   cd .. && zip -r lenormand-witch.zip lenormand-witch -x 'lenormand-witch/.git/*' 'lenormand-witch/README.md'
   ```
2. Turn on **Settings → Capabilities → Code execution and file creation**, then go to **Customize → Skills**, click **+** → **Create skill** → **Upload a skill**, upload the zip and enable it.

This is the environment the skill was written for: it writes the page to `/mnt/user-data/outputs/` and publishes it with the Artifact tool.

### Other agents

Any agent that supports the `SKILL.md` convention can load the folder from its skills directory; see that agent's documentation for the exact location.

For an agent without skill support:

1. Put the contents of `SKILL.md` (minus the YAML front matter) into the system prompt or a rules file.
2. Make `cards.md`, `spreads.md` and `references/reading-table.md` readable by the agent, or paste them in as context.
3. Give it a shell with Python 3 so it can run the draw command and `scripts/render_reading.py`.

Without a shell, the agent cannot draw cards honestly and the skill tells it to stop rather than improvise. Photo readings still work if the model can see images.

---

## Usage examples

**Direct deal, no question**

```
> 发牌，九宫格
```

The witch draws 9 cards, lays them out in ASCII, writes a general-outlook reading to the page and replies with the layout, a synthesis paragraph and the page link.

**A question that needs reshaping**

```
> Will I pass my driving test?
```

```
The cards can't answer "will I pass". They work by association and metaphor;
they can show what is moving in a situation and why, and they can't hand down
a yes or a no. We can look at it from a different angle.

  ( ) What is standing between me and passing
  ( ) How should I prepare from here
  ( ) Keep the original question
```

After you pick, she recommends a spread, deals and reads.

**A three-card line**

```
> Three cards on my new job.
```

```
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│  #14 Fox      │ │  #35 Anchor   │ │  #31 Sun      │
└───────────────┘ └───────────────┘ └───────────────┘
   Situation         Action           Outcome
```

> The Fox in the situation position is the work itself, and a reminder to check the people around it. Fox and Anchor together read as a job you stay in for safety. The Sun closes the line. Staying put pays off here.

**Grand Tableau**

```
> Do a Grand Tableau about my relationship.
```

She asks for a significator (Man / Woman / Child / Heart / Ring / skip), deals all 36, and reads all five passes (houses, significator and neighbors, corners and diagonals, mirrors, synthesis) in one turn. Knighting is offered, never applied unasked.

**Photo reading**

Send a photo of a spread, with or without text. She identifies the cards and the layout and reads what is on the table; she doesn't draw new cards.

**Single-card lookup**

```
> What does the Mice card mean?
```

A plain answer from `cards.md`; no spread built around it.

---

## File structure

```
lenormand-witch/
├── SKILL.md                          # The skill: persona, rules, question shaping,
│                                     #   workflow (draw → lay out → interpret → render),
│                                     #   Grand Tableau summary, photo handling, voice guide
├── cards.md                          # The 36 cards: EN/ZH names, playing-card inserts,
│                                     #   polarity, meanings, combination principles,
│                                     #   ordered-pair examples
├── spreads.md                        # ASCII layouts and position meanings for every spread;
│                                     #   full Grand Tableau method (houses, significator,
│                                     #   distance, corners, diagonals, mirrors, knighting, facings)
├── references/
│   └── reading-table.md              # Reading page workflow, JSON schema, card chips,
│                                     #   sections per spread, fortune grading, writing rules
├── assets/
│   ├── reading-table.template.html   # Self-contained page (~2.2 MB: deck art, design tokens,
│   │                                 #   embedded font). Contains the __READING_DATA__ placeholder.
│   └── example-square9.json          # A complete, valid 9-card reading to copy from
└── scripts/
    └── render_reading.py             # Validates a reading JSON and fills the template
```

---

## The render script

`scripts/render_reading.py` turns a reading JSON into a standalone HTML page. It uses only the Python standard library.

```bash
python3 scripts/render_reading.py <reading.json> [output.html]
```

| Argument | Meaning |
| --- | --- |
| `reading.json` | The reading, in the schema below. Required. |
| `output.html` | Where to write the page. Optional; defaults to `/mnt/user-data/outputs/lenormand-table.html` (the Claude.ai sandbox path). Outside Claude.ai, pass your own path. |

Try it with the bundled example:

```bash
python3 scripts/render_reading.py assets/example-square9.json ./lenormand-table.html
# ok: lenormand-table.html (2.21 MB)
```

Open the resulting file in any browser. It works offline.

**What it checks**

Errors (exit code `1`, nothing is written):

- `spread` is not one of `line3`, `line5`, `square9`, `gt`
- the number of cards doesn't match the spread (3, 5, 9, 36)
- a card id is outside 1–36, or appears twice
- in a Grand Tableau, the `significator` isn't one of the dealt cards
- a `pairs` key isn't two orthogonally adjacent positions (`a-b`, 0-based, `a < b`)
- a section's `fortune` isn't one of 大吉 中吉 小吉 吉 末吉 凶 大凶 (romaji forms like `daikichi` are also accepted)
- a `{{id}}` chip token isn't a valid card number

Warnings (printed, page still written):

- adjacent pairs with no text (the page falls back to keywords; expected in a Grand Tableau, so not reported there)
- a text field with only one of `zh` / `en`
- a chip for a card that isn't on the table
- en/em dashes or `--` in text (the style guide asks for periods, commas, colons or parentheses)
- a `significator` on a non-GT spread, or an empty `reading`

Exit code `2` means no input file was given; the usage text is printed.

The script injects the JSON into the template's `__READING_DATA__` placeholder, escaping `</` so the reading can't break out of its `<script>` tag. Never edit the template by hand for a reading; only the JSON changes.

---

## Reading JSON at a glance

```json
{
  "spread": "line3",
  "question": {"zh": "新工作", "en": "My new job"},
  "date": "2026-10-13",
  "significator": null,
  "positions": null,
  "cards": [
    {"id": 14, "note": {"zh": "…", "en": "…"}},
    {"id": 35, "note": {"zh": "…", "en": "…"}},
    {"id": 31, "note": {"zh": "…", "en": "…"}}
  ],
  "pairs": {
    "0-1": {"zh": "…", "en": "…"},
    "1-2": {"zh": "…", "en": "…"}
  },
  "reading": [
    {"label": {"zh": "综合", "en": "Synthesis"}, "fortune": "小吉",
     "text": {"zh": "{{14}}……", "en": "The {{14}} …"}}
  ]
}
```

- Every text field is a string or `{"zh": …, "en": …}`; write both.
- `{{id}}` inside text renders as a clickable card chip (thumbnail, localized name, playing-card insert). Don't also write the card name next to it.
- `pairs` keys are 0-based adjacent positions; the earlier card is the subject, the later one modifies it.
- `positions` overrides the default labels (line3: 情境 行动 结果 / Situation Action Outcome; line5: 远因 近因 核心 近期 走向; square9: past / present / future rows with a core; GT: row, column and house).
- A blank line inside `text` starts a new paragraph.

The full schema, section order for each spread and the fortune-grading table are in [`references/reading-table.md`](references/reading-table.md). [`assets/example-square9.json`](assets/example-square9.json) is a complete example.

---

## Notes and limitations

- **Built for Claude.ai first.** The default output path (`/mnt/user-data/outputs/`), the working file (`/home/claude/reading.json`), the Artifact-tool publishing step and the pinned page URL in `references/reading-table.md` all assume the Claude.ai sandbox. In Claude Code or elsewhere, write the JSON wherever you like, pass an explicit output path and open the HTML locally. If no publishing tool exists, the skill gives the full reading in chat instead.
- **Structured questions.** Spread choice, significator choice and reshape options use the environment's question tool (`AskUserQuestion` in Claude Code, `ask_user_input_v0` in the Claude app). Agents without one fall back to listing options in prose.
- **The page supports 3, 5, 9 and 36 cards.** Custom counts and 8 × 4 + 4 Grand Tableaux are read in chat only.
- **Entertainment and reflection.** This is a structured way to think about a situation, not a source of facts. It isn't medical, legal, financial or psychological advice, and the skill says so when the question calls for it.

## Credits

- Card art: Green Glyphs Lenormand deck (embedded in the template).
- Typeface: LT Superior Serif, SIL Open Font License 1.1 (embedded in the template).
- Voice inspired by Misty from *Cyberpunk 2077* (CD PROJEKT RED). This is an unofficial fan project, not affiliated with or endorsed by CD PROJEKT RED.
