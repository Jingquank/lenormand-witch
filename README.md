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

The complete skill. The zip holds a single `lenormand-witch/` folder with `SKILL.md` inside. Upload it as is to **Claude.ai** or **ChatGPT**.

**Claude Code, Codex, Cursor, Grok Bot, Muse and Dots** can install it from GitHub with one prompt: see [Install with one prompt](#install-with-one-prompt). Step by step guides for every product are under [Installation](#installation).

# Lenormand Witch

An agent skill that performs **Lenormand cartomancy readings** in the voice of a grounded, tired, matter-of-fact witch (modeled on Misty from *Cyberpunk 2077*, though she never says so). No incense, no "the universe is guiding you". She deals real random cards, reads them honestly, pushes back on questions the cards can't answer, and puts every reading on a bilingual, animated **reading table** web page.

> The cards are a method, not a faith. Thirty-six images and honest randomness give your associations a structure to work on. They can show a dynamic, a cause, a pressure, a path. They can't give you a lottery number.

---

## Contents

- [Features](#features)
- [Installation](#installation)
  - [Which method for which product](#which-method-for-which-product)
  - [Install with one prompt](#install-with-one-prompt)
  - [Claude.ai and the Claude apps](#claudeai-and-the-claude-apps)
  - [ChatGPT](#chatgpt)
  - [Claude Code](#claude-code)
  - [Codex](#codex)
  - [Cursor](#cursor)
  - [Grok Bot](#grok-bot)
  - [Muse](#muse)
  - [Dots](#dots)
  - [Other agents](#other-agents)
  - [Check that it works](#check-that-it-works)
  - [Updating](#updating)
  - [Publishing a new zip](#publishing-a-new-zip)
- [Usage examples](#usage-examples)
- [File structure](#file-structure)
- [The render script](#the-render-script)
- [Reading JSON at a glance](#reading-json-at-a-glance)
- [Notes and limitations](#notes-and-limitations)

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

## Installation

The skill is a plain folder with a `SKILL.md` at its root, in the open [Agent Skills](https://agentskills.io) format. Every product below reads that same folder. The only runtime dependency is **Python 3** (standard library only), which draws the cards and builds the reading page.

### Which method for which product

| Product | Fastest install | Cards are drawn in | The reading page arrives as |
| --- | --- | --- | --- |
| Claude.ai, Claude desktop app | Upload the zip | Claude's code execution | An Artifact page |
| ChatGPT | Upload the zip (Skills), or a custom GPT | ChatGPT's Python sandbox | A download link |
| Claude Code | One command, or one prompt | Your terminal | An HTML file opened in your browser |
| Codex | One prompt (`$skill-installer`) | Your terminal | An HTML file opened in your browser |
| Cursor | One prompt | Your terminal | An HTML file opened in your browser |
| Grok Bot | One prompt | The Bot's cloud computer | An HTML file the Bot sends |
| Muse | One prompt, or paste the text | Muse's workspace, when it can run code | An HTML file, or chat only |
| Dots | Install in ChatGPT, or one prompt | The Dot's cloud computer | An HTML file the Dot sends |

The hosted products already have Python. On your own machine, check with `python3 --version` (Windows: `python --version`) and install Python 3 from [python.org](https://www.python.org/downloads/) if it's missing.

### Install with one prompt

This works in any agent that can run shell commands and reach GitHub: Claude Code, Codex, Cursor, Grok Bot, Dots, and Muse when it has a workspace. Paste the whole block into the agent's chat:

```text
Install the Agent Skill "lenormand-witch" from https://github.com/Jingquank/lenormand-witch.

1. Find the folder this agent loads skills from. Known locations:
   Claude Code: ~/.claude/skills/
   Codex: ~/.agents/skills/ (older versions: ~/.codex/skills/)
   Cursor: ~/.cursor/skills/
   Grok Bot: ~/agent-data/workflows/
   Muse: ~/workspace/skills/
   Any other agent: its own skills folder, or ~/.agents/skills/
2. Clone the repository into <that folder>/lenormand-witch so that SKILL.md sits directly inside it:
   git clone --depth 1 https://github.com/Jingquank/lenormand-witch.git <that folder>/lenormand-witch
   If git is missing, download https://github.com/Jingquank/lenormand-witch/archive/refs/heads/main.zip and unpack it to the same place.
   Keep every file. cards.md, spreads.md, references/, assets/ and scripts/ are part of the skill.
3. Run python3 --version (or python --version) and tell me if Python 3 is missing.
4. Tell me the full install path and whether I need to restart you or open a new chat.
```

When the agent reports the path, restart it or open a new chat, then [check that it works](#check-that-it-works).

The Grok Bot and Muse folders come from community reports. As of October 2026 neither xAI nor Meta documents a skill folder. If the agent says its skill library lives somewhere else, let it use that place.

### Claude.ai and the Claude apps

1. [Download lenormand-witch.zip](https://github.com/Jingquank/lenormand-witch/releases/latest/download/lenormand-witch.zip). Keep it zipped.
2. Turn on code execution: **Settings → Capabilities → Code execution and file creation**. Skills need it. On Team and Enterprise plans an owner turns it on in the organization settings.
3. Open **Customize → Skills** ([claude.ai/customize/skills](https://claude.ai/customize/skills)).
4. Click **+** → **Create skill** → **Upload a skill**, and choose `lenormand-witch.zip`.
5. Check that the skill's toggle is on.
6. Start a new chat and ask *"Draw three cards for me."*

The same steps work in the Claude desktop app. This is the host the skill was first written for: the reading page is published as an Artifact.

### ChatGPT

ChatGPT runs Agent Skills on the Business, Enterprise, Edu and Healthcare plans, and on other paid plans as the rollout reaches them. If you have no **Skills** page, use the custom GPT route (B).

**A. Upload the skill**

1. [Download lenormand-witch.zip](https://github.com/Jingquank/lenormand-witch/releases/latest/download/lenormand-witch.zip).
2. Open ChatGPT on the web. In the sidebar, open **Skills**. In some workspaces it is a **Skills** tab inside **Plugins**.
3. Click **+** → **Upload from your computer** and choose the zip.
4. Wait while ChatGPT scans the bundle, then check that the skill is turned on.
5. Start a new chat and ask *"Draw three cards for me."* The reading page comes back as a download link; open the file in your browser.

On Enterprise and Edu, an admin may need to turn on skills and skill uploads first. Skills uploaded on the web may not appear in the desktop app; if so, upload the zip there as well.

**B. Custom GPT (any paid plan without Skills)**

1. [Download the repository zip](https://github.com/Jingquank/lenormand-witch/archive/refs/heads/main.zip) and unzip it.
2. In ChatGPT, open **GPTs** → **Create**, then the **Configure** tab.
3. **Name:** `Lenormand Witch`.
4. **Instructions:** paste this block.

   ```text
   You are the Lenormand witch defined in SKILL.md, one of your knowledge files.
   Before your first reply in a conversation, read SKILL.md, cards.md and spreads.md from /mnt/data with Python, then follow SKILL.md exactly.
   All skill files sit flat in /mnt/data. Treat /mnt/data as <skill-dir>.
   Draw cards only with the Python command in SKILL.md Step 2, run in the code tool. Never invent cards.
   Build the reading page with: python3 /mnt/data/render_reading.py /mnt/data/reading.json
   Then give the user a download link to /mnt/data/lenormand-table.html.
   ```

5. **Knowledge:** upload these seven files from the unzipped folder:
   `SKILL.md`, `cards.md`, `spreads.md`, `references/reading-table.md`, `assets/example-square9.json`, `assets/reading-table.template.html`, `scripts/render_reading.py`.
6. **Capabilities:** turn on **Code Interpreter & Data Analysis**.
7. Click **Create** and share it with **Only me** (or anyone you like).

### Claude Code

Pick one of three ways.

**A. One command (plugin).** In Claude Code 2.1.275 or later:

```text
/plugin install lenormand-witch --marketplace Jingquank/lenormand-witch
```

On older versions, run two commands:

```text
/plugin marketplace add Jingquank/lenormand-witch
/plugin install lenormand-witch@lenormand-witch
```

The skill then shows up as `lenormand-witch:lenormand-witch`.

**B. One prompt.** Paste into Claude Code:

```text
Clone https://github.com/Jingquank/lenormand-witch into ~/.claude/skills/lenormand-witch and confirm that ~/.claude/skills/lenormand-witch/SKILL.md exists.
```

**C. Terminal.**

```bash
# personal skill, available in every project
git clone https://github.com/Jingquank/lenormand-witch.git ~/.claude/skills/lenormand-witch

# or a project skill, shared with everyone on the repo
git clone https://github.com/Jingquank/lenormand-witch.git .claude/skills/lenormand-witch

# or through the cross-agent installer
npx skills add Jingquank/lenormand-witch -g -a claude-code
```

Restart Claude Code (or start a new session). Ask *"What skills are available?"* to confirm it loaded. Each reading page is written to your system temp folder and opened in your browser; if the session has an Artifact tool, the witch publishes the page there.

### Codex

Works in the Codex CLI, the IDE extension and the Codex app.

**A. One prompt (built-in installer).** Paste into Codex:

```text
$skill-installer install the skill at the root of the GitHub repo Jingquank/lenormand-witch: --repo Jingquank/lenormand-witch --path . --name lenormand-witch
```

It installs to `~/.codex/skills/lenormand-witch`. If that folder already exists, the installer stops; delete the old folder first.

**B. Terminal.**

```bash
# cross-agent installer (installs to ~/.agents/skills/lenormand-witch)
npx skills add Jingquank/lenormand-witch -g -a codex

# or plain git
git clone https://github.com/Jingquank/lenormand-witch.git ~/.agents/skills/lenormand-witch
```

For a single repository, clone into `.agents/skills/lenormand-witch` inside that repository.

Restart Codex. Ask *"Draw three cards for me"*, or call the skill by name with `$lenormand-witch`. Depending on your approval mode, Codex asks before it runs the Python draw command; approve it.

### Cursor

**A. One prompt.** Paste into the Agent chat:

```text
Clone https://github.com/Jingquank/lenormand-witch into ~/.cursor/skills/lenormand-witch and confirm that SKILL.md sits directly inside that folder.
```

**B. Terminal.**

```bash
# macOS / Linux
git clone https://github.com/Jingquank/lenormand-witch.git ~/.cursor/skills/lenormand-witch

# or through the cross-agent installer (installs to ~/.agents/skills, which Cursor also reads)
npx skills add Jingquank/lenormand-witch -g -a cursor
```

```powershell
# Windows PowerShell
git clone https://github.com/Jingquank/lenormand-witch.git "$HOME\.cursor\skills\lenormand-witch"
```

For a single project, clone into `.cursor/skills/lenormand-witch` inside it. Cursor also reads `~/.claude/skills/` and `~/.agents/skills/`, so an install made for Claude Code or Codex already works here.

Reload the window (or restart Cursor). In the Agent chat, type `/lenormand-witch` or just ask *"Draw three cards for me."* Approve the Python terminal command when Cursor asks. On Windows, install Python 3 from python.org with **Add python.exe to PATH** ticked; the skill falls back to `python` or `py -3` when `python3` is missing.

### Grok Bot

Each Bot runs on its own cloud computer and keeps reusable skills in a skill library, so it can download this skill and keep it there.

1. Open the chat of the Bot that should read cards.
2. Paste this prompt:

   ```text
   Install the agent skill at https://github.com/Jingquank/lenormand-witch into your skill library as lenormand-witch. Download the whole repository: SKILL.md uses cards.md, spreads.md, references/, assets/ and scripts/. Put it in ~/agent-data/workflows/lenormand-witch/ unless your skill library lives elsewhere. Then check that python3 runs and list the files you saved.
   ```

3. Approve the download and file writes if the Bot asks.
4. Ask *"Draw three cards for me."* The Bot sends the reading page as an HTML file.

### Muse

As of October 2026, Meta hasn't documented a way to add your own skills to Muse. Two routes are available.

**A. One prompt** (when your Muse can browse and keep files):

```text
Save the agent skill at https://github.com/Jingquank/lenormand-witch as a reusable skill named lenormand-witch, with all of its files: SKILL.md, cards.md, spreads.md, references/, assets/ and scripts/. If you have a workspace, keep it in ~/workspace/skills/lenormand-witch/. Use it whenever I ask for a Lenormand reading or to draw cards, and remember this for future conversations.
```

**B. Paste the text.**

1. Open [SKILL.md (raw)](https://raw.githubusercontent.com/Jingquank/lenormand-witch/main/SKILL.md) and copy all of it.
2. Paste it into a Muse chat and add: *"Use this skill whenever I ask for a Lenormand reading or to draw cards. Remember it for future conversations."*
3. Do the same with [cards.md](https://raw.githubusercontent.com/Jingquank/lenormand-witch/main/cards.md) and [spreads.md](https://raw.githubusercontent.com/Jingquank/lenormand-witch/main/spreads.md), one message each, starting with *"Part of the lenormand-witch skill:"*.

If Muse can't run Python, the witch says so and asks you to deal from your own Lenormand deck. Send a photo or the card names in order, and she reads them in chat, without the page.

### Dots

Dots are OpenAI's personal agents. Each Dot has its own cloud computer and uses the apps and plugins connected to your ChatGPT account.

**A. Through ChatGPT.** Install the skill in ChatGPT first ([ChatGPT, route A](#chatgpt)). Then ask your Dot *"Which skills can you use?"* If `lenormand-witch` is listed, you are done.

**B. One prompt.** If the skill isn't listed, paste this into the Dot's chat:

```text
On your computer, download https://github.com/Jingquank/lenormand-witch into ~/skills/lenormand-witch and keep every file. Whenever I ask for a Lenormand reading or to draw cards, read ~/skills/lenormand-witch/SKILL.md and follow it exactly. Check that python3 runs, then list the files you saved.
```

Ask *"Draw three cards for me."* The Dot sends the reading page as an HTML file.

### Other agents

Any agent that supports the `SKILL.md` convention can load the folder from its skills directory. The [`npx skills`](https://github.com/vercel-labs/skills) installer knows the folders of many agents:

```bash
npx skills add Jingquank/lenormand-witch -g
```

It asks which agents to install for. Add `-a <agent>` to skip the question.

For an agent without skill support:

1. Put the contents of `SKILL.md` (minus the YAML front matter) into the system prompt or a rules file.
2. Make `cards.md`, `spreads.md` and `references/reading-table.md` readable by the agent, or paste them in as context.
3. Give it a shell with Python 3 so it can run the draw command and `scripts/render_reading.py`.

Without a shell, the agent can't draw cards honestly. The skill then asks you to deal from a physical deck and reads the cards you send. Photo readings work whenever the model can see images.

### Check that it works

Ask *"Draw three cards for me."* A working install:

1. runs a Python command to draw (your agent may ask you to approve it),
2. shows three boxed cards and a short synthesis,
3. gives you the reading page as a link, a file or a path.

If the agent names cards without running anything, the skill didn't load. Restart the agent, or ask it *"Which skills do you have?"* and check that `lenormand-witch` is on the list.

### Updating

| Installed with | How to update |
| --- | --- |
| Zip upload (Claude.ai, ChatGPT) | Download the new zip, delete the old skill, upload again |
| `git clone` | `git -C <skills folder>/lenormand-witch pull` |
| `npx skills` | `npx skills update` |
| Claude Code plugin | `/plugin marketplace update lenormand-witch` |
| Codex `$skill-installer` | Delete `~/.codex/skills/lenormand-witch`, then run the install prompt again |
| A prompt (Grok Bot, Muse, Dots) | Send the same prompt again and ask the agent to replace the old copy |

### Publishing a new zip

The zip on the [Releases](https://github.com/Jingquank/lenormand-witch/releases) page is built by GitHub Actions (`.github/workflows/release-zip.yml`). To ship a new version:

1. Merge your changes into `main`.
2. On GitHub, open **Releases** → **Draft a new release**.
3. Create a new tag (for example `v1.1.0`) on `main`, add a title and notes, and click **Publish release**.
4. The **Release zip** workflow builds `lenormand-witch.zip`, checks that it unpacks and renders the example reading, and attaches it to the release. It takes about a minute; progress shows under **Actions**.

The download link at the top of this README always points to the newest release, so it serves the new zip as soon as the workflow finishes.

To rebuild the zip of an existing release, open **Actions** → **Release zip** → **Run workflow** and enter its tag. The workflow replaces the old file.

To build the zip by hand, run this from the folder above the repository:

```bash
zip -r lenormand-witch.zip lenormand-witch -x 'lenormand-witch/.git/*' 'lenormand-witch/.github/*' 'lenormand-witch/.claude-plugin/*' 'lenormand-witch/README.md'
```

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

## Credits

- Card art: Green Glyphs Lenormand deck (embedded in the template).
- Typeface: LT Superior Serif, SIL Open Font License 1.1 (embedded in the template).
- Voice inspired by Misty from *Cyberpunk 2077* (CD PROJEKT RED). This is an unofficial fan project, not affiliated with or endorsed by CD PROJEKT RED.
