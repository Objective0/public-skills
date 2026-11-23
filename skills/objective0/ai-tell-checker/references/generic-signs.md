# Generic signs of AI writing

Derived from Wikipedia's "Signs of AI writing" (WikiProject AI Cleanup, thousands of reviewed drafts) plus published detector research. Era note: these lists are model-dependent and shifting: "delve" peaked in 2023–24 and has largely vanished; newer models suppress em dashes. Treat the vocabulary lists as strong for 2023–2025-era text and weakening after; the sentence *shapes* and *artifacts* age much better than the word lists.

## Tier 1: near-definitive artifacts

Any one of these is essentially proof of chatbot involvement (in the sourcing or the prose):

- **Tracking parameters**: `utm_source=chatgpt.com`, `utm_source=openai`, `utm_source=copilot.com`, `referrer=grok.com` on links.
- **Reference debris**: `citeturn0search0` / `turn0image0`, `:contentReference[oaicite:N]{index=N}`, `oai_citation`, `[cite: 17]`, `【85†L261-269】`, `[attached_file:1]`, `[web:1]`, `grok_card` / `grok_render_citation_card_json`, `:::writing{variant=...}` markers, trailing `({"attribution":{"attributableIndex":...}})` JSON.
- **Chat scaffolding**: "Certainly!", "Of course!", "I hope this helps", "Would you like me to...", "let me know if...", "Here's a template for...", "You're absolutely right!"
- **Knowledge-cutoff language**: "as of my last knowledge update", "up to my last training update", "while specific details are limited in the provided sources", "based on available information".
- **Prompt refusal remnants**: "As an AI language model...", "I cannot offer medical advice, but..."
- **Placeholder text**: "[Your Name]", "[Describe the specific section...]", `INSERT_SOURCE_URL`, dates like `2025-XX-XX`.
- **Markdown in a non-Markdown medium**: `**bold**`, `##` headings, `---` rules pasted into a surface that renders none of it: especially Markdown mixed with the medium's own broken markup. (Markdown alone in a developer/Notion/Obsidian context is normal: check the medium.)

## Tier 2: compounding style tells

Individually weak; several distinct tells co-occurring in a short span is the strongest style evidence there is. Count distinct tells, not just instances.

### Sentence shapes

- **Rhetorical "it's not X, it's Y" relabel**: Y is just a grander word for X ("This isn't a newsletter, it's a movement"). A true categorical distinction ("A startup is not a business") is legitimate writing; the tell is the same-thing relabel.
- **Staccato fragment reframe**: "Not delivery velocity. Rate of learning."
- **Negative parallelisms**: "not just X, but also Y"; "no X, no Y, just Z"; "not a mirror but a portal".
- **Tailing participial clause**: a "-ing" clause tacked on the sentence end to add unearned significance: "...creating a lively community within its borders", "...highlighting its enduring importance", "...ensuring long-term success".
- **Drama-punch short sentence**: a 2–5 word sentence after a longer one that only negates or amplifies it: "It almost never is." / "They are not." One is rhythm; a pattern is the tell.
- **Narrator signposting**: sentences that announce the next sentence: "Here is where it gets interesting:", "This is worth pausing on...", "Let's be clear:". Test: delete it; if nothing is lost, it was a signpost.
- **Rule-of-three overuse**: adjective-adjective-adjective or three parallel phrases used to make thin analysis look complete; also triple bulleted **Bold header:** lists.
- **Copulative avoidance**: "serves as", "stands as", "marks", "represents", "boasts", "features", "refers to" doing the job of plain "is/has". Human writing uses far more bare is/has.
- **Elegant variation**: strained synonym cycling to avoid repeating a word (constraints/confines/norms in one passage). Caveat: taught behavior for some non-native writers.

### Vocabulary (density matters, not any single word)

Core list: delve, tapestry, testament (to), underscore, pivotal, crucial, robust, seamless, holistic, foster, garner, bolstered, meticulous(ly), intricate/intricacies, interplay, landscape (abstract), realm, vibrant, boasts, showcase, elevate, leverage, myriad, plethora, nuanced, multifaceted, "navigate" (metaphor), unpack, "deep dive" (verb), game-changer, "it is worth noting", "needless to say", "that being said", "at the end of the day", "in today's fast-paced world", sentence-initial "Additionally," / "Moreover," / "Furthermore,".

### Content-level tells

- **Significance inflation**: arbitrary details puffed into legacy: "stands as a testament", "a pivotal moment", "marking a key turning point", "setting the stage for", "evolving landscape", "indelible mark", "reflects broader trends". Root cause: models regress specifics to the generic-important mean.
- **Promotional puffery**: travel-brochure tone in neutral prose: "nestled in the heart of", "vibrant", "rich cultural heritage", "breathtaking", "renowned", "commitment to excellence", "diverse array".
- **Vague attribution**: "experts argue", "industry reports", "observers have cited", "widely regarded" with no or one actual source.
- **Formulaic furniture**: "In conclusion" / "In summary" / "Overall" closers; "Challenges and Future Outlook" sections ending in vague positivity ("continues to thrive"); "it's important to note/remember" didactic disclaimers.
- **Structural habits**: Title Case On Every Heading; bolding every key term; small gratuitous tables; emoji-decorated headers/bullets; formulaic em dashes doing "punched-up" clause emphasis several times per page.

## Tier 3: weak signals and substance checks

- Uniform sentence length and rhythm (low burstiness); suspiciously even paragraph sizes; every section the same shape.
- Generic examples where a person with real experience would have a specific one; no lived detail, numbers, or names anywhere.
- **Substance checks (do these when sources/facts are present: strongest non-artifact evidence):**
  - Citations that do not resolve, or resolve to unrelated content; DOIs pointing at different papers; ISBN checksum failures.
  - Book references with no page number, or page numbers that do not contain the claim.
  - Several dead links in one piece, never archived anywhere (they likely never existed).
  - Confident specifics that fail a spot-check.

## Signs of human writing (credit these)

- Plain copulatives and simple phrasing: "there is a", "it has a", wrote/used/tried/died rather than authored/utilized/attempted/passed away.
- Superlatives and definite claims ("the best", "the only", "was the first"): models hedge these away.
- Hedges and intensifiers ("very", "perhaps", "tends to"), wordy constructions ("in order to", "the fact that").
- Specific lived detail: real numbers, named people, particular scenes, opinions with an edge.
- Imperfections that make sense: a typo'd URL whose correct target the author can name, inconsistent formatting from manual editing.
- Text predating December 2022.

## Do NOT flag on these (near-zero evidence, high false-positive cost)

- Perfect grammar or spelling.
- Formal, academic, or "fancy" register as such: only the specific tells above count. Formal human writing has low burstiness too; detectors flag the U.S. Constitution.
- Transition words in isolation.
- "Sounds bland/robotic" gut feel: non-expert humans detect AI text at near chance.
- Curly quotes alone (Word and iOS produce them), correct markup, letter-like structure alone.
- Non-native English patterns: non-native speakers are the main victims of false accusations (detector false-positive rates of 5–12% versus ~1–4% for native speakers).

## On statistical detectors

GPTZero, Turnitin, Originality and similar measure perplexity (predictability) and burstiness (rhythm variance). Real-world accuracy is far below vendor claims, drops >20% against light paraphrasing, and false positives concentrate on formal and non-native writing; several universities have disabled them. Use them, if at all, as one weak signal: never as the verdict.
