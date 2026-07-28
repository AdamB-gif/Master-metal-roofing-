# 15 — Owner Instructions Log

Running log of standing instructions from the site owner, captured verbatim (lightly trimmed)
plus how each is being applied. Append new entries at the top; never delete — if an instruction
is later reversed, note the reversal instead of removing the original line.

---

## 2026-07-28

**Instruction:** "Everything I tell you, I want you to add to the scale after we're done."
**Applied as:** Every standing instruction/requirement given in conversation gets logged in this
file so it persists across sessions and doesn't get lost or re-asked.

**Instruction:** "Screenshot it and fix all these errors. Do the same thing for desktop view and
mobile view."
**Applied as:** Screenshot the site at a desktop width and a mobile width, list every visual/
functional defect found, fix them, and re-screenshot to confirm. Repeat this pass whenever a
significant round of changes is made, not just once.

**Instruction:** "Revamp it using front-end design. If you don't know what that is, look at
GitHub, find it, download it, make sure it's safe."
**Applied as:** Pull in real front-end design reference/inspiration from reputable, well-vetted
open-source sources on GitHub (checked for license, maintainer legitimacy, and no malicious code
before anything is used) rather than relying solely on a from-scratch guess at "good design."

**Instruction:** "Before you push to GitHub, always check and see if any personal information or
any foothold that somebody could use to get into my network is not exposed."
**Applied as:** **Standing rule, every push, no exceptions:** before `git push`, scan the diff
being pushed for secrets, API keys, tokens, credentials, private keys, internal IPs/hostnames,
personal contact info not meant for publication, `.env` files, and anything else that could give
an attacker a foothold. Report findings before pushing; do not push if anything questionable is
found without flagging it first.
