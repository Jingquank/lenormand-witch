# Reading table artifact

Every reading is displayed on a hosted page built from `assets/reading-table.template.html`. The page is display only: it has no draw, flip or question controls. The agent supplies all content through one JSON block; the page shuffles, deals face down, flips every card in order, then reveals the written reading. A viewer can open any card into a focused view (card meaning, the position reading, and the reading of each adjacent pair), switch Chinese and English, switch light and dark mode, and export the whole reading as a PNG.

The template embeds the Green Glyphs Lenormand faces, the Misty design system tokens, and LT Superior Serif (SIL OFL 1.1). Never edit the template by hand for a reading; only the JSON changes.

## Workflow

1. Draw with the command in SKILL.md Step 2. Card order from the command is position order.
2. Write the reading JSON to `/home/claude/reading.json` (schema below). Write every text field in both languages.
3. Render: `python3 <skill-dir>/scripts/render_reading.py /home/claude/reading.json`. It validates the JSON and writes `/mnt/user-data/outputs/lenormand-table.html`. Fix every `error:` line and rerun; read every `warning:` line and fix it unless it is intended.
4. Publish with the Artifact tool, action `publish`, `file_path` `/mnt/user-data/outputs/lenormand-table.html`, `favicon` 🌘, `title` "雷诺曼牌阵".
   - The querent wants one page updated for every reading. Pass the page's link as `url` to update it in place. The current page: `https://claude.ai/artifact/AzDvT8r2HU1CR9VontCdUT`.
   - When updating, omit `capabilities` so the stored declaration carries forward.
   - If the update is refused (the link is not the querent's, or the page no longer exists), publish without `url` and with `capabilities: {"downloads": true}`, then tell the querent the new link once.
   - A new reading replaces the old one on the page. Earlier readings survive only as exported images.
5. In chat: the ASCII layout in a code block, the synthesis paragraph, and the page link. The full position, pair and section text lives on the page; do not paste it into chat a second time.

A follow-up drill-down on cards already on the table is answered in chat. Re-render and republish only when the querent asks for the page to change, or when a new draw happens.

## Schema

Every text field takes either a string (shown in both languages) or `{"zh": "...", "en": "..."}`. Always write both.

```json
{
  "spread": "line3 | line5 | square9 | gt",
  "question": {"zh": "总体状况", "en": "General outlook"},
  "date": "YYYY-MM-DD",
  "significator": 28,
  "positions": null,
  "cards": [{"id": 32, "note": {"zh": "...", "en": "..."}}],
  "pairs": {"0-1": {"zh": "...", "en": "..."}},
  "reading": [{"label": {"zh": "过去", "en": "Past"}, "fortune": "中吉", "text": {"zh": "...", "en": "..."}}]
}
```

- `spread`: 3, 5, 9 or 36 cards. `cards` length must match.
- `question`: the question as settled after reshaping. Empty means general outlook.
- `date`: the date of the draw.
- `significator`: gt only; the card id chosen as significator (28 Man, 29 Woman, 24 Heart, 25 Ring, 13 Child), or null.
- `positions`: optional label overrides; leave null to use the defaults (line3: 情境 行动 结果; line5: 远因 近因 核心 近期 走向; square9: rows 过去 现在 未来, center 核心; gt: row and column plus house).
- `cards[i].note`: the reading of that card in that position, one to three sentences. This is what the focused view shows under "本位解读 / In this position".
- `pairs`: keys are `a-b` with 0-based positions and a < b, for positions that touch orthogonally. Lines: each neighbor. square9: the 12 edges. gt: write pairs for the significator's neighbors and any pair the reading leans on; the page falls back to a keyword line for the rest. Read the pair in position order: the earlier card is the subject, the later card modifies it.
- `reading`: the full reading in sections, in the order the method uses (see below). A blank line inside `text` starts a new paragraph.
- `fortune`: optional per section; see grading.

### Card chips

Inside any text, write `{{id}}` (for example `{{23}}`) wherever a card is named. The page renders a chip with the card thumbnail, the localized name and the playing card insert (老鼠 7♣ / Mice 7♣). Clicking a chip opens that card's focused view. Use a chip for every mention of a card that is on the table, including in notes and pairs. Do not also write the card name next to the token.

In English, write the article outside the token when grammar needs one: `The {{23}} sit in the core.`

## Sections per spread

- line3 and line5: one section per position or a single "位置 / Positions" section, then "组合 / Pairs" if a pair needs more than the pair text, then "综合 / Synthesis".
- square9: 过去 / Past, 现在 / Present, 未来 / Future (rows), 中列 / Middle column, then 综合 / Synthesis. Add 对角 / Diagonals only when they change the answer.
- gt: the five passes from SKILL.md, one section each: 宫位 / Houses, 指示牌 / Significator, 四角与对角 / Corners and diagonals, 镜像 / Mirrors, 综合 / Synthesis.

The synthesis section states the answer to the question. The crisis or sensitive-topic sentence from SKILL.md, when it applies, goes at the end of the synthesis text.

## Fortune grading

Grade each section from the cards it covers and how they combine, on this scale (English labels are rendered by the page):

| Grade | Use when |
| --- | --- |
| 大吉 | Positive cards dominate and the key position holds Sun, Key, Clover or Stars without a heavy neighbor |
| 中吉 | Mostly positive with one neutral card; no negative card |
| 小吉 | Positive and negative cards present; the positive side carries the outcome |
| 吉 | Neutral cards dominate and the direction is favorable |
| 末吉 | The section is difficult now and the later or outcome position turns favorable |
| 凶 | A negative card holds the key position, or negatives outnumber positives |
| 大凶 | Two or more heavy cards (Coffin, Scythe, Mountain, Cross, Mice, Snake) touch in the key position, with nothing to dilute them |

Grade the reading honestly. A section with Coffin at its center does not become 小吉 because the querent asked hopefully. Leave `fortune` out for a section that has no cards of its own (for example a method note).

## Writing

The page text follows the Voice section of SKILL.md in both languages. Chinese text follows the querent's writing rules: written register, no dashes, no contrastive negation ("不是X，而是Y"), no adjectives or adverbs, two-character verbs. English text is a faithful translation of the Chinese: the same sentences, the same order and the same verdict. It uses "hon" where the Chinese uses 亲爱的求问者.

## Example

`assets/example-square9.json` is a complete nine-card reading with notes, all 12 pairs, five graded sections, chips and both languages. Use it as the shape to copy.
