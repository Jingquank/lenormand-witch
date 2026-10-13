# Spreads

Card order from the draw command is position order: left to right, then top to bottom. The reading table page uses the same order, so the JSON `cards` array is the draw output as printed.

## 3-card line

```
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│  #NN Name     │ │  #NN Name     │ │  #NN Name     │
└───────────────┘ └───────────────┘ └───────────────┘
   1 Situation       2 Action         3 Outcome
     情境              行动              结果
```

Read: each card in position, then 1 + 2 and 2 + 3, then the line as one sentence with card 2 as the hinge. Best for "what should I do" questions.

## 5-card line

```
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│ #NN Name │ │ #NN Name │ │ #NN Name │ │ #NN Name │ │ #NN Name │
└──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘
 1 Distant    2 Recent     3 Core       4 Near       5 Direction
   cause        cause                     future
 远因          近因          核心          近期          走向
```

Read: card 3 is the heart of the matter. 1 and 2 are what led here; 4 and 5 are where it goes. Read the pairs 1 + 2, 2 + 3, 3 + 4, 4 + 5, then mirror 1 with 5 and 2 with 4. Best for a situation with a past and a direction.

## 9-card square

```
          ┌──────────┐ ┌──────────┐ ┌──────────┐
 Past     │ 1        │ │ 2        │ │ 3        │
 过去     └──────────┘ └──────────┘ └──────────┘
          ┌──────────┐ ┌──────────┐ ┌──────────┐
 Present  │ 4        │ │ 5 Core   │ │ 6        │
 现在     └──────────┘ └──────────┘ └──────────┘
          ┌──────────┐ ┌──────────┐ ┌──────────┐
 Future   │ 7        │ │ 8        │ │ 9        │
 未来     └──────────┘ └──────────┘ └──────────┘
```

Rows: past (1 to 3), present (4 to 6), future (7 to 9). Columns: left (1, 4, 7) is the inner side, what the querent thinks and feels; middle (2, 5, 8) is the axis of the matter; right (3, 6, 9) is the outer side, other people and circumstances. Card 5 is the core.

Read in this order: card 5; the three rows; the middle column; the diagonals 1 + 5 + 9 and 3 + 5 + 7 when they add something; the four corners 1, 3, 7, 9 as the frame. Twelve adjacent pairs exist: 1-2, 2-3, 4-5, 5-6, 7-8, 8-9 across and 1-4, 4-7, 2-5, 5-8, 3-6, 6-9 down. Best for "why" questions and situations with several moving parts.

## Grand Tableau (9 × 4)

```
 Row 1   1  2  3  4  5  6  7  8  9
 Row 2  10 11 12 13 14 15 16 17 18
 Row 3  19 20 21 22 23 24 25 26 27
 Row 4  28 29 30 31 32 33 34 35 36
```

In chat, render the grid with card numbers in each position, mark the significator with `*`, then list `pos → #NN Name` below it. The reading table page draws the full grid.

### Pass 1: Houses

Position N is the house of card N. The card that lands in a house is read through that house's theme.

| Pos | House | Theme |
| --- | --- | --- |
| 1 | Rider | news, what is arriving |
| 2 | Clover | luck, short chances |
| 3 | Ship | travel, distance, transitions |
| 4 | House | home, family, foundation |
| 5 | Tree | health, growth |
| 6 | Clouds | confusion, what is unclear |
| 7 | Snake | complications, rivals, desire |
| 8 | Coffin | endings, what must close |
| 9 | Bouquet | gifts, pleasure, invitations |
| 10 | Scythe | sudden decisions, cuts |
| 11 | Whip | conflict, repetition, exercise |
| 12 | Birds | conversation, nerves |
| 13 | Child | beginnings, children |
| 14 | Fox | work, self-interest, caution |
| 15 | Bear | power, money reserves, protection |
| 16 | Stars | hope, direction |
| 17 | Stork | change, moves |
| 18 | Dog | friends, loyalty |
| 19 | Tower | institutions, solitude |
| 20 | Garden | public life, society |
| 21 | Mountain | obstacles |
| 22 | Paths | choices |
| 23 | Mice | losses, stress |
| 24 | Heart | love |
| 25 | Ring | commitments, contracts |
| 26 | Book | secrets, study |
| 27 | Letter | documents, messages |
| 28 | Man | the querent or the main man |
| 29 | Woman | the querent or the main woman |
| 30 | Lily | peace, maturity, intimacy |
| 31 | Sun | success, energy |
| 32 | Moon | recognition, emotion |
| 33 | Key | solutions, certainty |
| 34 | Fish | money, business |
| 35 | Anchor | stability, long-term work |
| 36 | Cross | burden, fate |

Do not read all 36 houses. Read the houses that matter for the question (Heart and Ring for love, Fish and Fox for work and money, Tree for health), the house the significator stands in, and any house where a heavy card lands on a matching theme (Coffin in the house of Heart, Mice in the house of Fish).

### Pass 2: Significator and distance

Significator choices: Man (28) for a male querent, Woman (29) for a female querent, Child (13) for a young person or a question about one, Heart (24) for a love question, Ring (25) for a commitment question.

- **Position.** Upper rows: what is conscious, visible, already in play. Lower rows: what is under the surface, unconscious, still forming. Left of the significator: past and what is leaving. Right: future and what is coming.
- **Neighbors.** The eight cards touching the significator (up, down, left, right, and the four diagonals) are the querent's immediate situation. Read them as pairs with the significator.
- **Distance.** Cards one step away affect the querent directly. Cards two steps away are in view. Cards three or more steps away are in the background; a heavy card far away is a threat that is not yet near.
- **Second person.** If both Man and Woman are on the table, the distance between them and what lies between them is the state of that relationship.

### Pass 3: Corners, center, diagonals

- **Corners:** positions 1, 9, 28, 36 frame the whole reading: the situation's limits.
- **Center:** the block around positions 13, 14, 15, 22, 23, 24 is the core of the matter.
- **Diagonals:** from the significator, follow each of the four diagonals to the edge of the grid. Up-left: what shaped the querent. Up-right: what the querent aims at. Down-left: what is being left behind under the surface. Down-right: what is building beneath and ahead. Read each diagonal as a sentence.

### Pass 4: Mirrors

- **Vertical mirrors (18 pairs):** row 1 with row 4 and row 2 with row 3, in the same column: 1↔28, 2↔29, 3↔30, 4↔31, 5↔32, 6↔33, 7↔34, 8↔35, 9↔36, 10↔19, 11↔20, 12↔21, 13↔22, 14↔23, 15↔24, 16↔25, 17↔26, 18↔27.
- **Horizontal mirrors (16 pairs):** within a row, column 1 with 9, 2 with 8, 3 with 7, 4 with 6; column 5 has no partner.

A mirror pair is a hidden link: two areas of life that answer each other. Read the mirrors of the significator first, then any mirror pair that holds two heavy cards or two cards about the question.

### Knighting (on request only)

Knighting follows the chess knight's move from the significator: two steps in one direction and one step to the side. The cards reached that way are indirect influences. Offer it with the structured tool; never apply it unasked.

### Facings

A card whose figure faces a direction looks toward the cards on that side. What a card faces is where its energy goes; what it turns away from is behind it.

In the Green Glyphs deck: Rider, Fox, Bear, Stork and Dog face right. Ship sails right. Man and Woman are drawn front-on, so read their neighbors on both sides with equal weight and use position (left past, right future) alone.

### Pass 5: Synthesis

Three to five sentences. State the answer to the question, name the heaviest card near the significator and what it means for the querent, and name the strongest support on the table.

## Custom number of cards

For any other count, lay the cards in one line and read it as an extended 5-card line: the middle card is the core, the left half is what led here, the right half is where it goes. The reading table page supports only 3, 5, 9 and 36 cards; give other counts in chat.
