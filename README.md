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

# Lenormand Witch

An agent skill that performs **Lenormand cartomancy readings** in the voice of a grounded, tired, matter-of-fact witch (modeled on Misty from *Cyberpunk 2077*, though she never says so). No incense, no "the universe is guiding you". She deals real random cards, reads them honestly, pushes back on questions the cards can't answer, and puts every reading on a bilingual, animated **reading table** web page.

> The cards are a method, not a faith. Thirty-six images and honest randomness give your associations a structure to work on. They can show a dynamic, a cause, a pressure, a path. They can't give you a lottery number.

---

## Contents

- [Install](#install)
- [Features](#features)
- [Usage examples](#usage-examples)
- [File structure](#file-structure)
- [The render script](#the-render-script)
- [Reading JSON at a glance](#reading-json-at-a-glance)
- [Notes and limitations](#notes-and-limitations)
- [Publishing a new version](#publishing-a-new-version)

---

## Install

Click your app to open its steps.

<details>
<summary><b>Grok Bot · Muse · Dots</b>: paste one prompt</summary>

**1.** Copy this and send it in the chat:

```text
Install the Lenormand Witch skill from https://github.com/Jingquank/lenormand-witch

Download the whole repository and save it in your skill library as "lenormand-witch". Keep every file and folder; the skill needs all of them.
Use this skill whenever I ask for a Lenormand reading or ask you to draw cards, and remember it for future conversations.
When you're done, list the files you saved.
```

**2.** Say: **"Draw three cards for me."**

If your agent can't download files, open [SKILL.md](https://raw.githubusercontent.com/Jingquank/lenormand-witch/main/SKILL.md), copy all of it into the chat, and add: *"Use this skill whenever I ask for a Lenormand reading, and remember it for future conversations."*

</details>

<details>
<summary><b>Claude.ai · ChatGPT</b>: download a zip and upload it</summary>

**1.** Download **[lenormand-witch.zip](https://github.com/Jingquank/lenormand-witch/releases/latest/download/lenormand-witch.zip)**. Keep it zipped.

**2.** Upload it.

- **Claude.ai** (and the Claude desktop app)
  1. **Settings → Capabilities**: turn on **Code execution and file creation**.
  2. **Customize → Skills → + → Upload a skill**: choose the zip.
- **ChatGPT**
  1. Sidebar → **Skills** (in some workspaces: **Plugins → Skills**).
  2. **+ → Upload from your computer**: choose the zip.

**3.** Open a new chat and say: **"Draw three cards for me."**

<details>
<summary>No Skills page in ChatGPT? Make a custom GPT instead.</summary>

1. Download the [repository zip](https://github.com/Jingquank/lenormand-witch/archive/refs/heads/main.zip) and unzip it.
2. ChatGPT → **GPTs → Create → Configure**.
3. **Instructions:** paste this.

   ```text
   You are the Lenormand witch defined in SKILL.md, one of your knowledge files.
   Before your first reply, read SKILL.md, cards.md and spreads.md from /mnt/data with Python, then follow SKILL.md exactly.
   All skill files sit flat in /mnt/data. Treat /mnt/data as <skill-dir>.
   Draw cards only with the Python command in SKILL.md Step 2. Never invent cards.
   Build the reading page with: python3 /mnt/data/render_reading.py /mnt/data/reading.json
   Then give the user a download link to /mnt/data/lenormand-table.html.
   ```

4. **Knowledge:** upload `SKILL.md`, `cards.md`, `spreads.md`, `references/reading-table.md`, `assets/example-square9.json`, `assets/reading-table.template.html`, `scripts/render_reading.py`.
5. **Capabilities:** turn on **Code Interpreter & Data Analysis**, then click **Create**.

</details>

</details>

<details>
<summary><b>Claude Code · Codex · Cursor</b>: paste one prompt</summary>

**1.** Copy this and send it in the chat:

```text
Install the agent skill from https://github.com/Jingquank/lenormand-witch

Clone it into your skills folder as "lenormand-witch", so SKILL.md sits directly inside:
  Claude Code:  ~/.claude/skills/lenormand-witch
  Codex:        ~/.agents/skills/lenormand-witch
  Cursor:       ~/.cursor/skills/lenormand-witch
  Other agents: your own skills folder
Then check that python3 (or python) runs, and tell me if I need to restart you.
```

**2.** Restart the app (or open a new chat) and say: **"Draw three cards for me."**

<details>
<summary>Prefer the terminal?</summary>

```bash
# Claude Code
git clone https://github.com/Jingquank/lenormand-witch.git ~/.claude/skills/lenormand-witch

# Codex
git clone https://github.com/Jingquank/lenormand-witch.git ~/.agents/skills/lenormand-witch

# Cursor
git clone https://github.com/Jingquank/lenormand-witch.git ~/.cursor/skills/lenormand-witch
```

In Claude Code you can also run `/plugin install lenormand-witch --marketplace Jingquank/lenormand-witch`.

</details>

</details>

### Did it work?

After **"Draw three cards for me."** the witch runs a short Python command, shows three cards and gives you the reading page. If she names cards without running anything, the skill didn't load: restart the app and try again.

**Updating:** send the same prompt again (or upload the new zip) and ask to replace the old copy.

---

## Features

**Real draws.** Cards are dealt with Python's `secrets.SystemRandom`, without replacement. The agent is told never to invent cards; if the command can't run, the witch asks you to deal from your own deck and reads the cards you send.

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

Each section of the reading carries an honest **fortune grade** on the seven-step omikuji scale: great blessing · middle blessing · small blessing · blessing · future blessing · curse · great curse.

---

## Usage examples

**Direct deal, no question**

```
> Deal the cards, 9-card square.
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
├── .claude-plugin/
│   └── marketplace.json              # Lets Claude Code install the folder as a plugin
├── .github/workflows/
│   └── release-zip.yml               # Builds lenormand-witch.zip for each published release
├── SKILL.md                          # The skill: persona, rules, per-host paths and delivery,
│                                     #   question shaping, workflow (draw → lay out →
│                                     #   interpret → render), Grand Tableau summary,
│                                     #   photo handling, voice guide
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
python3 scripts/render_reading.py <reading.json> [output.html] [--open]
```

| Argument | Meaning |
| --- | --- |
| `reading.json` | The reading, in the schema below. Required. |
| `output.html` | Where to write the page. Optional. Without it, the script picks the host default: `/mnt/user-data/outputs/lenormand-table.html` on Claude.ai, `/mnt/data/lenormand-table.html` on ChatGPT, and `lenormand-witch/lenormand-table.html` inside the system temp folder everywhere else. |
| `--open` | Open the page in the default browser after writing it (local machines). |

The script looks for the template in `assets/` next to `scripts/`, and also in its own folder, so a flat copy of the files (as in a custom GPT's knowledge) works too. It prints the full path it wrote.

Try it with the bundled example:

```bash
python3 scripts/render_reading.py assets/example-square9.json ./lenormand-table.html --open
# ok: /path/to/lenormand-table.html (2.21 MB)
```

The page works offline in any browser.

**What it checks**

Errors (exit code `1`, nothing is written):

- `spread` is not one of `line3`, `line5`, `square9`, `gt`
- the number of cards doesn't match the spread (3, 5, 9, 36)
- a card id is outside 1 to 36, or appears twice
- in a Grand Tableau, the `significator` isn't one of the dealt cards
- a `pairs` key isn't two orthogonally adjacent positions (`a-b`, 0-based, `a < b`)
- a section's `fortune` isn't one of the seven grades: `daikichi`, `chukichi`, `shokichi`, `kichi`, `suekichi`, `kyo`, `daikyo` (the kanji forms are also accepted)
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
  "question": {"zh": "…", "en": "My new job"},
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
    {"label": {"zh": "…", "en": "Synthesis"}, "fortune": "shokichi",
     "text": {"zh": "{{14}}……", "en": "The {{14}} …"}}
  ]
}
```

- Every text field is a string or `{"zh": …, "en": …}`; write both.
- `{{id}}` inside text renders as a clickable card chip (thumbnail, localized name, playing-card insert). Don't also write the card name next to it.
- `pairs` keys are 0-based adjacent positions; the earlier card is the subject, the later one modifies it.
- `positions` overrides the default labels (line3: Situation, Action, Outcome; line5: Distant cause, Recent cause, Core, Near future, Direction; square9: past / present / future rows with a core; GT: row, column and house).
- A blank line inside `text` starts a new paragraph.

The full schema, section order for each spread and the fortune-grading table are in [`references/reading-table.md`](references/reading-table.md). [`assets/example-square9.json`](assets/example-square9.json) is a complete example.

---

## Notes and limitations

- **Each host delivers the page its own way.** `SKILL.md` has a table of hosts (Claude apps, ChatGPT, coding agents, personal agents) with the working file, the page path and the delivery for each: an Artifact on Claude.ai, a download link in ChatGPT, a browser tab for local agents, a file sent by a personal agent. The pinned page URL in `references/reading-table.md` belongs to the skill's author; for anyone else the update is refused and the witch publishes a new page. If a host can't build or share the page, the full reading goes in chat.
- **Honest draws need Python.** Without a way to run code, the witch asks you to deal from your own deck and reads the cards you send.
- **Structured questions.** Spread choice, significator choice and reshape options use the environment's question tool (`AskUserQuestion` in Claude Code, `ask_user_input_v0` in the Claude app). Agents without one fall back to a short numbered list.
- **The page supports 3, 5, 9 and 36 cards.** Custom counts and 8 × 4 + 4 Grand Tableaux are read in chat only.
- **Entertainment and reflection.** This is a structured way to think about a situation, not a source of facts. It isn't medical, legal, financial or psychological advice, and the skill says so when the question calls for it.

## Publishing a new version

Merge your changes into `main`. Then either publish a release on GitHub (**Releases → Draft a new release**, new tag such as `v1.2.0`, **Publish release**), or open **Actions → Release zip → Run workflow** and enter the new tag. The workflow (`.github/workflows/release-zip.yml`) builds `lenormand-witch.zip`, checks it and attaches it to the release. The zip link in [Install](#install) always serves the newest release.

## Credits

- Card art: Green Glyphs Lenormand deck (embedded in the template).
- Typeface: LT Superior Serif, SIL Open Font License 1.1 (embedded in the template).
- Voice inspired by Misty from *Cyberpunk 2077* (CD PROJEKT RED). This is an unofficial fan project, not affiliated with or endorsed by CD PROJEKT RED.
