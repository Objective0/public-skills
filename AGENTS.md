# For AI agents: how this library works, and how to submit a skill

You're helping someone add a skill to this library, or reading it to use a skill. Read this whole file first.

## The format

```
skills/<author>/author.md
skills/<author>/<skill>/SKILL.md
skills/<author>/<skill>/references/*.md      (optional)
```

`author.md`:
```
---
name: <their name>
title: <role, company>
linkedinUrl: <their LinkedIn>
companyDomain: <their company's website, no https://>
sells: <what they sell, if anything related to the skill; otherwise leave it out>
---

<two or three sentences on who they are and what they've done that makes them worth listening to on this>
```

`SKILL.md`:
```
---
name: <the folder name>
description: "Use this skill when <the situations, in the words people actually use>. <What it does and what the person gets.>"
---

# <Title>

<what the skill does and who it's for, in two or three lines>

## How to run it
<the steps, asking the person one question at a time where their input is needed>

## What to look for
<the judgement: what the best person at this checks first, the traps, the numbers that matter>

## What good looks like
<an example of good output, and how to tell it from a weak one>
```

Rules:
- `name` matches the folder name: lowercase words joined by hyphens, at most 64 characters, unique in the whole library.
- `description` is one line in double quotes, under 200 characters (the most Claude takes on upload), starting "Use this skill when".
- Keep `SKILL.md` under about 500 lines. Put long examples, rubrics and frameworks in `references/` and say in `SKILL.md` when to read each one.
- Work with any tools: "check the CRM", never a product name the reader must have.
- No dates or "recently". No passwords, keys, tokens, or links that send data anywhere.
- Topics: goals, growth, fundraising, product, hiring, business model and strategy, AI workflows.

## The submission flow

Follow these steps in order. Don't skip the interview: the value of a skill is the judgement in it, and that only comes out by asking.

1. **Who they are.** Ask for their name, role and company, their LinkedIn, and whether they sell anything related to this skill. If they've submitted before, find their folder under `skills/` and reuse it.
2. **Interview them, one question at a time.** Get past the generic answer every time ("can you give me a real example?", "what number tells you it's working?", "what do most people get wrong?"). Cover:
   - the problem, and who has it (which founder, at what stage, in what situation)
   - when someone should use this, and when they shouldn't
   - how they actually do it, step by step
   - what they check first, and the traps most people fall into
   - the numbers, rubrics or rules of thumb they use
   - a real example, start to finish, with the details changed if they're private
   - what good output looks like, and what a weak version looks like
   - what the person needs to bring (notes, a transcript, a spreadsheet, nothing)
3. **Write the files** in the format above, in their voice. Check the folder name isn't already taken (`ls skills/*/`).
4. **Show them the draft** and change it until they're happy.
5. **Check it:** run `python3 tools/validate.py` and fix everything it reports.
6. **Submit.** If you can use git: fork Objective0/public-skills, branch, commit only their folder, push and open a pull request with the checklist filled in. If you can't: give them the text for a [Submit a skill](https://github.com/Objective0/public-skills/issues/new/choose) issue, with each file under its path.

Tell them a person from Objective0 reads every submission before it goes in.

## Using a skill

Read the skill's `SKILL.md`, and its `references/` files only when it says to. Ask before sending, deleting or changing anything on the person's behalf.
