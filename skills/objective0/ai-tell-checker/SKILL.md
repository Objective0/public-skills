---
name: ai-tell-checker
description: "Use this skill when you want to know if writing reads as AI-generated: an honest, evidence-based report on the tells, and a rewrite that sounds like a person."
---

# AI Tell Checker

Review a piece of text for signs of AI-generated writing, report the evidence honestly, and (on request) fix it.

The single most important thing to understand: **no style sign proves anything on its own.** Statistical detectors (GPTZero, Turnitin, etc.) flag formal human writing, non-native English, and even the U.S. Constitution; word lists date quickly as models change. What actually works is what Wikipedia's AI-cleanup editors learned over thousands of reviews: signs **compound**. One em dash is punctuation; em dashes plus "delve" plus a tailing participial clause plus a "not just X, but Y" in the same three paragraphs is a pattern. Report accordingly, and never present a style-only verdict as certainty.

## Workflow

### 1. Get the text and pick the rule set

Take the text from the conversation or read the file the user points at.

Always read **`references/generic-signs.md`**: the catalogue (drawn from Wikipedia's "Signs of AI writing" and detector research) of artifacts, style tells, weak signals, signs of human writing, and what not to flag.

If the person or their company has its own writing rules (a style guide, banned words, a house voice), ask for them and apply them on top. House rules win where they differ: some generic tells may be deliberate house voice.

### 2. Sweep line by line

Read the whole text once for sense, then sweep it against the catalogue. Work in three evidence tiers, strongest first:

- **Tier 1: near-definitive artifacts.** Leftover chatbot machinery: `utm_source=chatgpt.com` in URLs, `citeturn0search0` / `oaicite` / `[cite: n]` reference debris, placeholder text ("[Your Name]"), knowledge-cutoff disclaimers ("as of my last update"), chat scaffolding ("Certainly!", "I hope this helps"), Markdown artifacts in a non-Markdown medium. Any one of these is essentially proof.
- **Tier 2: compounding style tells.** The banned sentence shapes (rhetorical "it's not X, it's Y" relabels, staccato fragments, negative parallelisms, tailing participial clauses, drama-punch short sentences, narrator signposting), AI vocabulary density, significance inflation ("stands as a testament", "pivotal"), promotional puffery, vague attribution ("experts argue"), copulative avoidance ("serves as" for "is"), rule-of-three overuse, formulaic em dashes, elegant variation, title-case headings, bold overuse, "In conclusion" summaries. Individually weak; count the co-occurrences.
- **Tier 3: weak signals and substance checks.** Uniform sentence rhythm, suspiciously even paragraph lengths, generic examples where a human would have a specific one. Where the text cites sources or facts, spot-check them: fabricated or non-resolving citations, wrong-page book references, and confident specifics that do not verify are among the strongest tells of all, and they are substance, not style.

Also collect **signs of human writing** (plain "is/has" constructions, hedges, superlatives, wordiness, specific lived detail, explainable choices): these count as evidence in the other direction and belong in the report.

### 3. Report

Use this exact structure:

```
## Verdict: [Reads human | Mixed signals | Strong AI signal] (confidence: low/medium/high)

One-sentence summary of why.

### Near-definitive artifacts (Tier 1)
- "quoted line": what it is  [or "None found."]

### Compounding style tells (Tier 2): N distinct tells, M instances
- "quoted line": pattern name, why it reads as AI
...

### Weak signals and substance checks (Tier 3)
- ...

### Signs of human writing
- "quoted line": why it reads human  [or "None found."]

### Caveats
- [Only the caveats that apply: formal register, non-native author, house style overlap, era-dependence...]
```

Quote every finding verbatim: the user should never have to search for what you mean. Calibrate the verdict on tier logic: any Tier 1 hit → Strong AI signal (high confidence). Several distinct Tier 2 tells co-occurring in a short span → Strong or Mixed depending on density and counter-evidence. Tier 2 tells that are isolated, or explainable by the caveats → Mixed or Reads human with the caveat stated. Never escalate confidence past what the evidence supports, and say plainly when the honest answer is "cannot tell from style alone."

### 4. Fix (only if asked)

When the user wants the text improved, rewrite the flagged passages and show the result (as an edited file if the input was a file, otherwise in the reply):

- **Reconstruct, never token-swap.** Swapping "delve" for "look at" or a dash for a full stop leaves the same machine rhythm; the ickiness is structural. Rebuild the sentence: fold punches into the sentence they decorate with "but"/"and", replace relabels by saying the point straight, cut signposting and start with the substance.
- **Cut rather than decorate.** Most AI padding (significance inflation, tailing clauses, summaries) improves the text by deletion, not replacement.
- **Preserve the author's actual claims and voice.** Fix the telling, not the argument. Never invent specifics to make it "sound human": if a generic example needs a real one, leave a `[REAL EXAMPLE NEEDED: ...]` marker.
- If there are house rules, follow them for what replaces what, and never cut words they protect.

List each change with its reason so the user can accept or reject individually when the edit is substantial.

## What never to do

- Never flag on grammar quality, formality, or "sounds bland" alone: the do-not-flag list in `references/generic-signs.md` exists because these have near-zero evidential value and high false-positive cost (formal and non-native writers get wrongly accused this way).
- Never launder a statistical detector score as evidence. If the user asks about GPTZero-style tools, explain their false-positive record instead.
- Never claim certainty about authorship of someone else's text. The verdict describes what the text reads like, not who wrote it: say so if the stakes are accusatory (a student, an employee, a vendor).

## What good looks like

A good report quotes every finding word for word, sorts it into the right tier, credits the signs of human writing, and gives a verdict no stronger than the evidence: "Mixed signals (medium): four distinct style tells in two paragraphs, but specific numbers and a named customer read human." A good rewrite rebuilds the flagged sentences, keeps the author's claims and voice, and marks `[REAL EXAMPLE NEEDED]` rather than inventing one.

A weak report calls text AI because it is formal, polished or "sounds bland", quotes a detector score as proof, or swaps single words and leaves the machine rhythm in place.
