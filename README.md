# Founder skills

Skills for AI agents that help startup founders and their teams with goals, growth, fundraising, product, hiring, business model and strategy, and AI workflows. Built by [Objective0](https://objective0.com) and written by founders and operators.

Every skill is a plain `SKILL.md` that any agent can read: Claude, Claude Code, Cursor, Codex and others.

## Install

```bash
# one skill
npx skills add Objective0/public-skills --skill lean-canvas-coach

# everything from one author
npx skills add Objective0/public-skills/skills/objective0

# the whole library (pick from a list)
npx skills add Objective0/public-skills
```

**In Claude (web or desktop):** download the skill's zip from the [latest release](https://github.com/Objective0/public-skills/releases/tag/skills-latest), then upload it under Settings, Capabilities, Skills.

## Skills

| Skill | Author | What it does |
|---|---|---|
| [lean-canvas-coach](skills/objective0/lean-canvas-coach/) | Objective0 | Builds a Lean Canvas with you one question at a time, then challenges the weak assumptions |
| [experiment-coach](skills/objective0/experiment-coach/) | Objective0 | Turns an idea into an experiment with a clear test, and ranks ideas by impact, confidence and ease |
| [jobs-and-outcomes](skills/objective0/jobs-and-outcomes/) | Objective0 | Takes you from feature-speak to the job your customer is hiring you for, and the outcomes they want |
| [four-forces-challenge](skills/objective0/four-forces-challenge/) | Objective0 | Maps the push, pull, anxiety and habit behind a purchase, then tests your assumptions about them |
| [bob-moesta-interview-reviewer](skills/objective0/bob-moesta-interview-reviewer/) | Objective0 | Reviews customer interview transcripts for the forces and timeline behind a purchase, and coaches your interviewing |
| [outreach-template](skills/objective0/outreach-template/) | Objective0 | Writes outreach for customer discovery interviews: no pitch, no jargon, adapted to the channel |
| [deal-qualification-coach](skills/objective0/deal-qualification-coach/) | Objective0 | Scores sales calls with BANT and MEDDIC, shows the gaps in a deal and what to fix next |
| [deep-tech-launchpad](skills/objective0/deep-tech-launchpad/) | Objective0 | Separates what you know from what you assume for an early B2B or deep tech product, and designs research to close the gaps |
| [narrative-strategy](skills/objective0/narrative-strategy/) | Objective0 | Turns strategy docs and meeting notes into a narrative: PR angles, podcast pitches, talks and thought leadership |

## Add your skill, with your AI

You don't need to know git. Paste this into Claude, Cursor or any capable agent:

> Fetch https://raw.githubusercontent.com/Objective0/public-skills/main/AGENTS.md and follow its submission flow. Interview me properly about my skill: how I actually do this, the judgement calls, my real examples and numbers. Then write it up in the repo's format, check it, and open the pull request (or give me the issue text if you can't use git).

Your agent interviews you, writes the skill, checks it and opens the pull request. Every submission is read by a person before it goes in. Details in [CONTRIBUTING.md](CONTRIBUTING.md).

## Layout

```
skills/
  <author>/            # one folder per author: their profile and all their skills
    author.md          # who they are
    <skill>/
      SKILL.md         # the skill: portable, works with any tool
      references/      # optional: deeper material the skill reads when it needs it
```

The skill's folder name is its permanent name. It's how people install it, so it never changes once merged.

## What makes a skill good here

A good skill carries judgement, not just steps: what the best founder or operator checks first, the trap most people fall into, and what good looks like at the end. It works whatever tools the reader uses. It's on one of our topics: goals, growth, fundraising, product, hiring, business model and strategy, or AI workflows.

## Licence

MIT, see [LICENSE](LICENSE). Credit stays with you: your `author.md` travels with your skills.
