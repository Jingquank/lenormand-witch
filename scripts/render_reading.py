#!/usr/bin/env python3
"""Validate a reading JSON file and render it into the reading table template.

Usage:
    python3 render_reading.py reading.json [output.html]

Default output: /mnt/user-data/outputs/lenormand-table.html
Exit code 1 on schema errors (nothing is written). Warnings are printed and do not block.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "assets" / "reading-table.template.html"
PLACEHOLDER = "__READING_DATA__"
DEFAULT_OUT = Path("/mnt/user-data/outputs/lenormand-table.html")

SPREADS = {"line3": (3, 3), "line5": (5, 5), "square9": (9, 3), "gt": (36, 9)}
FORTUNES = {"大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶",
            "daikichi", "chukichi", "shokichi", "kichi", "suekichi", "kyo", "daikyo"}
TOKEN = re.compile(r"\{\{\s*(\d{1,2})\s*\}\}")


def neighbors(kind, i):
    n, cols = SPREADS[kind]
    if kind in ("line3", "line5"):
        return [j for j in (i - 1, i + 1) if 0 <= j < n]
    rows = n // cols
    r, c = divmod(i, cols)
    out = []
    for dr, dc in ((-1, 0), (0, -1), (0, 1), (1, 0)):
        rr, cc = r + dr, c + dc
        if 0 <= rr < rows and 0 <= cc < cols:
            out.append(rr * cols + cc)
    return out


def texts(v):
    """Yield (lang, string) for a text field that is a string or {zh, en}."""
    if v is None:
        return
    if isinstance(v, str):
        yield ("both", v)
    elif isinstance(v, dict):
        for k in ("zh", "en"):
            if k in v and isinstance(v[k], str):
                yield (k, v[k])


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUT
    data = json.loads(src.read_text(encoding="utf-8"))
    errors, warns = [], []

    kind = data.get("spread")
    if kind not in SPREADS:
        errors.append(f"spread must be one of {list(SPREADS)}, got {kind!r}")
        kind = None

    cards = data.get("cards") or []
    ids = [c.get("id") for c in cards if isinstance(c, dict)]
    if kind:
        n = SPREADS[kind][0]
        if len(cards) != n:
            errors.append(f"{kind} needs {n} cards, got {len(cards)}")
    if any(not isinstance(i, int) or not 1 <= i <= 36 for i in ids):
        errors.append("every card id must be an integer 1 to 36")
    if len(set(ids)) != len(ids):
        errors.append("card ids must be unique (draw without replacement)")

    sig = data.get("significator")
    if sig is not None:
        if kind != "gt":
            warns.append("significator is only shown for gt; it will be ignored")
        elif sig not in ids:
            errors.append("significator must be one of the dealt card ids")

    if kind:
        valid_pairs = {f"{min(i, j)}-{max(i, j)}" for i in range(len(cards)) for j in neighbors(kind, i)}
        for key in (data.get("pairs") or {}):
            if key not in valid_pairs:
                errors.append(f"pairs key {key!r} is not two adjacent positions (a-b, a<b, 0-based)")
        missing = valid_pairs - set((data.get("pairs") or {}).keys())
        if missing and kind != "gt":
            warns.append(f"{len(missing)} adjacent pair(s) have no text; the page shows a keyword fallback: {sorted(missing)}")

    for k, bk in enumerate(data.get("reading") or []):
        f = bk.get("fortune")
        if f is not None and str(f).strip() not in FORTUNES:
            errors.append(f"reading[{k}].fortune {f!r} is not one of 大吉 中吉 小吉 吉 末吉 凶 大凶")
    if not data.get("reading"):
        warns.append("reading is empty; the page will show cards only")

    # every text field: language coverage and card tokens
    fields = [("question", data.get("question"))]
    fields += [(f"cards[{i}].note", c.get("note")) for i, c in enumerate(cards) if isinstance(c, dict)]
    fields += [(f"pairs[{k}]", v) for k, v in (data.get("pairs") or {}).items()]
    for k, bk in enumerate(data.get("reading") or []):
        fields += [(f"reading[{k}].label", bk.get("label")), (f"reading[{k}].text", bk.get("text"))]
    for name, v in fields:
        if isinstance(v, dict) and not ({"zh", "en"} <= set(v)):
            warns.append(f"{name} is missing {'zh' if 'zh' not in v else 'en'}; the other language is used")
        for _, s in texts(v):
            for m in TOKEN.finditer(s):
                tid = int(m.group(1))
                if not 1 <= tid <= 36:
                    errors.append(f"{name}: token {m.group(0)} is not a card id")
                elif tid not in ids:
                    warns.append(f"{name}: {m.group(0)} is not on the table; it renders as a static chip")
            if re.search(r"[\u2013\u2014]|--|——", s):
                warns.append(f"{name}: contains a dash; replace it with a period, comma, colon or parentheses")

    for w in warns:
        print("warning:", w)
    if errors:
        for e in errors:
            print("error:", e)
        sys.exit(1)

    blob = json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8")
    if PLACEHOLDER not in html:
        print("error: template placeholder missing")
        sys.exit(1)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html.replace(PLACEHOLDER, blob), encoding="utf-8")
    print(f"ok: {out} ({out.stat().st_size / 1e6:.2f} MB)")


if __name__ == "__main__":
    main()
