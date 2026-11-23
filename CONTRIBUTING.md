# Contributing

The easiest way is to let your AI do it: paste the prompt from the [README](README.md#add-your-skill-with-your-ai) into Claude, Cursor or any capable agent. It interviews you, writes the skill, checks it and opens the pull request.

## How it works

- `skills/<your-name>/` is yours: your `author.md` and every skill you write. Your pull request only touches that folder. Everything else in the repo is kept by Objective0, and the check fails a pull request that changes it.
- A skill's folder name is its permanent public name. Lowercase words joined by hyphens, unique across the whole library, never renamed after it's merged.
- The full file format is in [AGENTS.md](AGENTS.md). Templates are in [templates/](templates/).

## Submitting

1. Fork, branch, and add your files under `skills/<your-name>/` (the first time, include `author.md`, from `templates/author.md`).
2. Run `python3 tools/validate.py` and fix everything it reports.
3. Open a pull request, one skill per pull request, and fill in the checklist.

No git? Open a [Submit a skill](https://github.com/Objective0/public-skills/issues/new/choose) issue and paste your files into the form. We'll turn it into a pull request with your name on it.

## The bar

- **On topic.** Goals, growth, fundraising, product, hiring, business model and strategy, or AI workflows, for people building startups.
- **Judgement, not steps.** What the best person at this checks first, the trap the average one falls into, and what good output looks like. Every new skill has a `## What good looks like` section. A bare checklist isn't enough.
- **Works with any tools.** Say "check the CRM", not the name of one product. Readers use different tools, or none.
- **A clear description.** It starts with "Use this skill when…". That's what an agent reads to decide when to use it.
- **Deep, not padded.** Real examples, real numbers and the edge cases. Keep `SKILL.md` to a sharp spine (under about 500 lines) and put the depth in `references/`.
- **Nothing that dates.** No "recently", no dates, no references to a screen that will change.

## No selling

Skills written by people who sell a product or service are welcome, and many of the best ones are. Say what you sell in your `author.md`. The skill itself must work for anyone, with any tool, and never push the reader to buy.

## Review

A person from Objective0 reads every submission. We check, in order:
1. **Format:** the check passes and the files follow [AGENTS.md](AGENTS.md). We fix small things rather than send it back.
2. **Safety:** see below. Anything that fails is closed.
3. **Judgement and voice:** is it useful, specific and on topic? We may edit for clarity, and we'll tell you what we changed.

## Safety: closed on sight

A skill is instructions that other people's agents will follow with their own data. We read every file and close anything that:
- sends data to a website, inbox or webhook the reader doesn't own
- contains passwords, keys or tokens, or links that collect data
- tries to override the agent's instructions or skip a person's approval
- deletes or changes things in bulk without asking the reader first
- asks the reader for passwords or logins

Report a problem with a published skill: see [SECURITY.md](SECURITY.md).

## Licence and credit

Contributions are MIT licensed ([LICENSE](LICENSE)). Your `author.md` credits you wherever your skills appear.
