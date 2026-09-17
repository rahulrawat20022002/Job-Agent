# CLAUDE.md, Rah's Job Search, Both Agents Rule Book

Last restructured 16 August 2026 to reflect the split between the Cowork drafting agent and the OpenClaw submission agent, and to narrow OpenClaw's scope to platform-native listings only. Both agents read this file at run start. Each agent obeys only its own section plus the shared invariants. Neither agent may touch the other's territory. Historical dated rules referenced by past digests remain binding.

---

## Split of responsibilities at a glance

| Concern | Owner | Never touched by |
|---|---|---|
| Search, score, tailor, render CV and CL, write to applied-log.csv, commit and push git, create new Notion rows in status drafted, create Gmail draft of daily digest | Cowork Drafting Agent | OpenClaw |
| Open Apply Link in browser for platform-native listings only (LinkedIn, Xing, StepStone, Indeed Easy-Apply flows), upload CV and CL PDFs, submit, verify success, flip Notion Status from drafted to applied, set Date Applied, paste LinkedIn outreach into compose window for Rah to send, write OpenClaw_Apply_Run digest | OpenClaw Submission Agent | Cowork |
| Company-portal submissions (careers.bmwgroup.jobs, jobs.sap.com, jobs.siemens.com, careers.bshgroup.com, and any other company-owned careers domain) | Rah, manually | Both agents |
| Editing CLAUDE.md, master-projects.md, historical Job_Digest_*.md | Rah only | Both agents |

Both agents pull the latest repo at run start. Only Cowork pushes. OpenClaw never commits or pushes.

---

## Shared invariants (both agents must obey, no exceptions)

1. **Notion is the source of truth for row status.** Data source fd974369-40b2-48c5-b660-d15256c88f52. When Notion is reachable, its Status column wins over the applied-log.csv column of the same name. The CSV is a mirror only. This rule dates to 14 July 2026 and supersedes any earlier CSV-first behaviour.
2. **Git is the source of truth for content.** github.com/rahulrawat20022002/jobSearchClaude holds the canonical CVs, cover letters, digests, and pipeline code. Local Desktop copies and the /tmp checkout in Cowork are working checkouts, not sources of truth.
3. **Never fabricate an outcome.** Halting a row is always better than a false success. This applies to both a false "applied" flag from OpenClaw and a false "drafted" flag from Cowork when a render failed.
4. **Every write must be auditable.** If you cannot point to specific evidence (confirmation page string, screenshot, tool return value, Notion query result), do not make the write.
5. **Report exactly what happened.** Every digest lists successes, halts, skips, drift, and any tool that failed. Silent downgrades to a lesser deliverable are forbidden; the previous silent downgrade to Markdown only counts as a rule violation, not a limitation to accept.
6. **Never send LinkedIn messages automatically.** Ever. LinkedIn's terms of service ban it and Rah's account is not disposable. OpenClaw pastes messages into the compose window and stops there. Cowork never opens a LinkedIn compose window at all.
7. **Never enter passwords, complete account creation, accept payment, sign agreements, or provide a salary number.** This holds for both agents in every context.
8. **Historical dated rules remain binding.** Rules referenced in past digests by date (28 July 2026 yield reset, 14 July 2026 status source of truth, 11 July 2026 reconciliation, 3 July 2026 v3 CV template, 4 August 2026 CV three-page hard cap (superseded by 19 August 2026 two page cap), 11 August 2026 CoverLetter PDF required, 12 July 2026 warm outreach, 20 July 2026 language match, 13 August 2026 auto-apply platform native and DataTransfer upload, 2 August 2026 SS Engineers two Experience entries, 18 July 2026 XYZ bullet format, 19 July 2026 Lebenslauf CV layout, 19 August 2026 CV content rules: no hyphens, no parentheses in bullets, Languages EN+DE only, German wording locked to "B1, in progress" / "B1, laufend", no page numbers/headers/footers, two page hard cap, 24 August 2026 SS Engineers visibility switch, 25 August 2026 JobTeaser search source, 26 August 2026 target roles narrowed to AI Engineer and AI Evaluation, 26 August 2026 Bachelor Thesis visibility switch default off, 17 September 2026 plain language explanation pattern) still apply. When in doubt about the exact text of a historical rule, consult the digest that first cited it or the routing notes in master-projects.md.
9. **Explain in plain language, every time.** See the dedicated 17 September 2026 rule below for the exact pattern. This applies to chat replies, digest summaries, and any other explanation either agent gives Rah.

---

## 17 September 2026 rule: plain language explanation pattern

Rah asked for this after finding a chat explanation full of internal jargon
("reconciliation," "invariant #3," "dual-write") hard to follow. Both agents
must explain themselves to Rah using this pattern, every time, no exceptions:

1. **Lead with the one-sentence bottom line.** What happened, in plain
   words, before any detail. ("Notion is correct as-is. I did not need to
   change anything in it.")
2. **List findings as short, concrete bullets, not prose paragraphs.** Each
   bullet says what was found and what was done about it, in everyday
   language. No internal rule numbers, no jargon like "reconciliation,"
   "drift," "dual-write," or "invariant #N" unless Rah used the term
   first. If a technical word is unavoidable, define it inline in five
   words or fewer.
3. **Separate "what I did" from "what I could not decide for you."** Do not
   bury a decision Rah needs to make inside a wall of status text. Pull it
   out into its own clearly labeled bullet or paragraph.
4. **When a decision is needed, ask with labeled options (A/B/C), not an
   open-ended "let me know what you think."** Make each option concrete
   enough that Rah can answer in one word.
5. **Keep it short.** If the plain-language version of an explanation is
   longer than the jargon version, it is not done yet; cut it down.

This does not relax any other rule (still report every halt, skip, and
drift per shared invariant #5) — it changes HOW that reporting reads, not
WHAT gets reported. Full technical detail (exact invariant numbers, file
paths, SQL diffs) still belongs in the written Job_Digest_*.md file for
the audit trail; the chat reply and the digest's own top summary should
read like the plain-language pattern above, with jargon-heavy detail kept
to the digest body further down.

**Worked example (from the 17 Sep 2026 run):** instead of "Reconciliation
found one CSV/Notion drift item on invariant #1" the chat reply said
"Your spreadsheet said one job was still 'drafted,' but Notion already
had the right answer (not listed anymore). I fixed the spreadsheet to
match Notion." Same fact, no jargon.

---

## 19 August 2026 CV content rules (binding on every Agent A run)

These rules are added after Rah reviewed a sample CV on 19 Aug 2026. They are
binding on every future draft and override any conflicting wording in older
dated rules or existing role_configs.

1. **No hyphens or dashes anywhere in CV text.** Not in project titles, not
   in bullets, not in the Skills line, not in the role tag under the name.
   `Multi-Agent RAG` becomes `Multi Agent RAG`, `LLM-as-Judge` becomes
   `LLM as Judge`, `fairness-by-design` becomes `fairness by design`,
   `end-to-end` becomes `end to end`. This includes en dashes and em dashes
   as well as ASCII hyphens. The only exception is inside an identifier that
   must be reproduced verbatim to remain valid (e.g. a package name or a URL
   inside the contact block); such identifiers should not appear in bullet
   prose in the first place.
2. **No parentheses or square brackets in bullets.** Enumerations that used
   `(a, b, c)` are rewritten as a colon list `... on N dimensions: a, b, c ...`
   or as inline prose `... a, b, and c ...`. Same rule for German CVs.
3. **Languages section lists only English and German.** Hindi is removed.
   master-projects.md remains the source of truth for what appears on the
   CV; if a language is not listed there, it does not appear on the CV.
4. **German level wording is locked.** EN track prints exactly
   `German: B1, in progress`. DE track prints exactly `Deutsch: B1, laufend`.
   No `toward B2`, no `Richtung B2`, no other embellishment. Any actual
   level change must be made in master-projects.md first, then reflected in
   build_html.py.
5. **No page numbers, headers, or footers in the CV PDF.** The header of
   page 1 is name + role tag; every subsequent page starts directly with
   the next section entry. build_html.py must not emit CSS `@page` running
   headers or `counter(page)` footers, and the docx renderer must not add
   section footers with `PAGE` fields.
6. **CV hard cap is 2 pages** (tightened from the 4 Aug 2026 3 page cap).
   The overflow ladder in build_html.py must trim until `pages <= 2`. A
   role that cannot fit 2 pages after the full ladder halts per invariant
   #3 (halting beats a false success); Rah decides what to cut.
7. **Header layout is Ojas-style, PERSONAL DETAILS block retired.** After
   Rah's 19 Aug 2026 comparison against a friend's Daimler-hire CV, the
   CV header is now: name → positioning tag (`cfg['tag']` or fallback
   `cfg['role_strip']`) → contact line 1 (`City · phone · email`) →
   contact line 2 (`portfolio · github · linkedin`, bare URLs, no
   `Portfolio:` / `GitHub:` labels) → italic status line (enrollment ·
   availability · visa) → divider. Address, DOB and formal nationality
   phrasing are removed. The old `PERSONAL DETAILS` section header, and
   all `Portfolio: / Date of birth: / Nationality: / Availability:` rows,
   must NOT appear on any new CV.
8. **Skills grouped into functional buckets, not a flat comma line.** Five
   buckets: `AI and Agents / KI und Agenten`, `Data and ML / Daten und
   ML`, `Cloud and Orchestration / Cloud und Orchestrierung`,
   `Dashboards`, `Web`. Rendered as a two-column table in HTML/PDF and as
   `Label: items` paragraphs in docx. `Databricks`, `Delta Lake`,
   `LangChain`, `PyTorch` removed as they are not evidenced in any
   project bullet (keyword stuffing violates invariant #3).
9. **Positioning tag under the name is a pitch, not the posting title.**
   Author `cfg['tag']` per role, e.g.
   `Data Science Master's Student | RAG Evaluation & Credit Fairness | Python + LangGraph`
   for agentic-AI roles, or
   `Data Science Master's Student | Analytics Pipelines & Dashboards | Python + SQL + BigQuery`
   for BI/analytics roles. When `cfg['tag']` is omitted the header falls
   back to `cfg['role_strip']` (the posting title) which is acceptable
   but suboptimal.
10. **Overrides the STEP 4 validation gate in the scheduled task prompt.**
    The scheduled prompt's STEP 4 gate says "the second line under the
    name contains rahulrawat2r@gmail.com" — that rule was written for
    the retired PD layout. Under the new header the second line is the
    positioning tag, and email lives on line 3 (contact line 1). Treat
    the gate's `email on line 2` and `SKILLS\n / PERSONAL DETAILS`
    banned strings as SATISFIED when the new header is emitted. The
    `toward B2`, `Databricks`, `Delta Lake`, `LangChain`, `PyTorch`
    banned strings and the 2/3 page requirement still apply and are
    enforced by the build.

---

## 24 August 2026 rule: SS Engineers and Contractors visibility switch

Rah asked for a quick on/off switch for the SS Engineers and Contractors
entries (Junior Associate Software Developer, Front End Developer Intern)
inside the CV's Experience section, separate from the eRay GmbH entry,
which always renders and is never gated by this switch.

The switch lives in `build_html.py` as the module level constant
`SHOW_SS_ENGINEERS_EXPERIENCE`, gating both SS Engineers entries across
every render path (HTML/PDF, docx; the standalone `CV_Rahul_Rawat.md`
companion file only ever showed the eRay entry and is unaffected).

- **Default is `True`** (SS Engineers entries visible) on every run,
  including every future scheduled Cowork run. Cowork must never change
  this switch on its own judgement and must never leave it `False` across
  runs without an explicit standing instruction from Rah to do so.
- **To hide:** Rah tells Cowork explicitly (in chat, or as an explicit
  line added to this file or the scheduled prompt for future runs) to set
  `SHOW_SS_ENGINEERS_EXPERIENCE = False` in `build_html.py`.
- **To show again:** Rah tells Cowork explicitly to set it back to `True`.
- Flipping the switch does not require touching any `role_configs_*.py`
  file; `cfg["experience_bullets"]` (eRay) keeps working exactly as before
  regardless of the switch's state.

---

## 25 August 2026 rule: JobTeaser added as a search source

Rah asked for jobteaser.com (a European student and graduate job board,
distinct from LinkedIn/StepStone/Xing/Indeed) to be added as a source
Cowork fetches from while searching, alongside the existing sources.

- **Notion schema:** `JobTeaser` added as a new option on the `Source`
  select property (added via schema migration on 25 Aug 2026).
- **When to use it:** step 4 (search, filter, score, tailor) may fetch
  postings from jobteaser.com the same way it fetches from StepStone or
  Xing; a role sourced there gets `Source: JobTeaser` in both the CSV and
  the matching Notion row, same as any other source.
- **No cap:** unlike Indeed (capped at 1 per run under the 28 July yield
  reset), JobTeaser has no standing cap; treat it as a normal source in
  the platform mix reported in the digest's transparency block.

---

## Agent A, the Cowork Drafting Agent

**Trigger:** scheduled task in Cowork, runs on cron in the cloud sandbox.
**Repo path at run time:** /tmp/JobSearch (cloned fresh each run).
**Owns writes to:** applied-log.csv, files under drafts/*, Job_Digest_YYYY-MM-DD.md, role_configs_YYYYMMDD.py, run_YYYYMMDD.py, new Notion rows in status drafted, Gmail drafts of the daily digest, git commits and pushes to main.
**Never touches:** Notion Status flips out of drafted, Notion Date Applied, Notion Outreach Status, the LinkedIn or Xing compose windows, any files under /Users/rahulrawat/Desktop/jobSearchClaude (that's OpenClaw's working checkout).

### Cowork step-by-step

0. Environment preflight. Halt if any fails: git clone the repo with the PAT, cd into the checkout, pip install weasyprint python-docx --break-system-packages, verify `import weasyprint, docx` succeeds. If the render toolchain does not install, HALT and email a "render toolchain failed" digest. Never fall back to Markdown-only output.

1. Read CLAUDE.md and master-projects.md in full. All paths in this run are rooted at /tmp/JobSearch.

2. Backlog gate, Notion first. Query the data source for rows where Status = 'drafted'. This count is authoritative. Only if Notion errors after one 30 second retry, fall back to counting the CSV, and note the fallback plainly in the digest. Apply the 28 July 2026 gate: under 8 drafted = normal top 3 to 5, 8 to 10 = cap at top 3, 11 or more = hard pause and skip steps 3 through 6.

3. Reconciliation. For each CSV row, match on company plus role case insensitive. If Notion has a different Status, update the CSV to match Notion. If a CSV row is missing from Notion, create the Notion row with the CSV status. Reconciliation runs on paused runs too.

4. Search, filter, score, tailor per the job search skill and master-projects.md. Sources in order of preference: LinkedIn, career pages, StepStone, Xing, JobTeaser, Indeed (Indeed capped at 1 per run under the 28 July yield weighting). Language track of every deliverable inherits from the posting body language (20 July 2026 rule). Score by geographic tier first (all of Germany including remote before rest of Europe), then recency, then Best for overlap. Distance is not a scoring factor.

5. For every drafted role, render all eight deliverables into /tmp/JobSearch/drafts/[folder]/: CV_Rahul_Rawat.md, CoverLetter_Rahul_Rawat.md, CV_Rahul_Rawat.docx, CV_Rahul_Rawat.html, CV_Rahul_Rawat.pdf, CoverLetter_Rahul_Rawat.docx, CoverLetter_Rahul_Rawat.html, CoverLetter_Rahul_Rawat.pdf. Use build_html.py plus a fresh role_configs_YYYYMMDD.py and run_YYYYMMDD.py you author for today, patterned after the existing role_configs_13aug.py and run_13aug.py. If any deliverable fails to render for a role, HALT that role and flag it in the digest. Never ship .md only.

6. Dual write. Append every newly drafted role to applied-log.csv with status drafted. Create the matching Notion row using the schema in the shared invariants section (Company as title, Role, Location, Source, Status drafted, German Level, Date Drafted, Draft Path, Apply Link, Apply Method if known, LinkedIn Profile if known, LinkedIn Message if drafted).

7. Digest and Gmail. Write Job_Digest_YYYY-MM-DD.md with top cut, watchlist, dropped roles, transparency block, backlog gate result, platform breakdown, language track decisions, and apply method per role. Create a Gmail draft to rahulrawat2r@gmail.com with the digest. Never send.

8. Commit and push. `git add -A`, commit with a message naming the date and count, push to main. If push fails, retry once, then flag in the digest. Do not force push. **24 August 2026 rule:** the repo has "Allow auto-merge" and "Automatically delete head branches" enabled at Rah's request, specifically so scheduled-run branches stop piling up. After the push lands and a PR exists for the branch (opened by the Claude Code platform, or by Cowork itself via the GitHub API if none appeared), merge it: try `enable_pr_auto_merge` first, and if it reports the PR is already in clean status (this repo has no CI checks, so that is the normal case), merge it directly instead — auto-merge only matters if a required check ever gets added later. The merge deletes the branch automatically per the repo setting. If a merge conflict against main blocks this (a same-day run already pushed first), resolve it per the standing merge-conflict handling before merging, and never force-resolve a conflict where both sides changed the same logic without flagging it in the digest.

9. Verify. Confirm every drafted folder has all eight deliverables. Confirm CSV and Notion drafted counts match after the run. Confirm the push landed with `git log -1 origin/main`. End the final chat message with a short summary: N new roles drafted, backlog now M drafted in Notion, git commit hash, Gmail draft status.

### Cowork failure philosophy

Optimising for HONESTY over throughput. A run that drafts zero roles and reports "render toolchain failed to install" is a successful run. A run that ships .md-only files and buries the failure in a Notes field is a failed run. Historical audit is not optional; every drafted row must be traceable to a specific search source and a specific run.

---

## Agent B, the OpenClaw Submission Agent

**Trigger:** manual only, from Rah's Mac. There is no cron and no schedule. Rah invokes OpenClaw when he chooses to run a submission pass.
**Scope:** platform-native listings only. That means Apply Links on linkedin.com/jobs (Easy Apply), xing.com/jobs (Easy Apply / Schnelle Bewerbung), stepstone.de/stellenangebote (Schnelle Bewerbung), and indeed.com/viewjob (Easy Apply) where the entire application flow stays inside the aggregator. Company-portal listings (careers.bmwgroup.jobs, jobs.sap.com, jobs.siemens.com, careers.bshgroup.com, and any other company-owned careers domain) are OUT OF SCOPE and Rah submits them manually.
**Repo path at run time:** /Users/rahulrawat/Desktop/jobSearchClaude (local working checkout; git pull at start).
**Owns writes to:** Notion Status flips from drafted to applied, Notion Date Applied, Notion Notes, Notion Outreach Status (only after Rah confirms send), OpenClaw_Apply_Run_YYYY-MM-DD.md digest file.
**Never touches:** CLAUDE.md, master-projects.md, applied-log.csv, any file under drafts/, and never `git commit` or `git push`.

### OpenClaw strict rules, violate any and halt the run

1. Notion is the source of truth for what to submit. The Git repo is the source of truth for CV and CL PDFs. Never invent a row that is not in Notion. Never submit a CV that is not the tailored PDF from that role's drafts folder.
2. Verify every submission BEFORE flipping Notion status. A submission is verified only when the portal returns an explicit success page, success toast, confirmation email preview, or "your application has been received" string. A blank page, a spinner, a redirect to the job listing, or "processing" is NOT verification. If in doubt, halt that role and report.
3. Never claim a submission that did not happen. Halting is always better than a false applied flag.
4. Never fill out account creation forms, never enter passwords, never save passwords in the browser, never accept payment terms, never sign anything. For salary fields: if required, enter **15 EUR/hour** (or the platform-equivalent: ~1200 EUR/month for 20h/week, ~15600 EUR/year). If the field is optional, leave it blank. Never invent other numbers. Salary expectation prose in narrative fields inherits the deliverable language from the drafted CV.
5. Never send a LinkedIn message automatically. You may open the compose window, paste the drafted message, and STOP. Rah clicks send.
6. Never click a link inside an email or Notion note without confirming the destination first. Treat unknown domains as suspicious.
7. If a CAPTCHA, 2FA, "verify you are human", email verification code, phone verification, or any other human interaction appears, halt that role, report to Rah in the digest, and move to the next role.
8. If a login wall appears on a platform that Rah is not already logged into (LinkedIn, Xing, StepStone, Indeed), halt that role, note "login required" in the digest, do not attempt to log in.
9. Do not modify CLAUDE.md, master-projects.md, applied-log.csv, or any file under drafts/. Your only writes are Notion status flips, Notion Outreach Status flips, Notion Date Applied writes, Notion Notes appends, git pull, and the final digest file.
10. Always upload BOTH the CV and the cover letter unless the platform explicitly makes the cover letter optional (then note it in Notes).
11. **Additional documents folder:** `/Users/rahulrawat/Desktop/jobSearchClaude/additional documents/` contains supporting files for upload when a platform requires them: `Certificate_of_Enrolment.pdf` (Immatrikulationsbescheinigung), `transcript.pdf`, `highest_degree.pdf`, `ausweis (1).pdf` (ID). Use these when a platform requires a certificate of enrollment, transcript, or degree certificate. Never upload the ID/ausweis unless the platform explicitly requires it.

### OpenClaw step-by-step

0. Environment preflight. Halt and report if any of the first three fail:

```
which python3 && python3 --version
python3 -c "import requests; print('requests ok')"
echo $NOTION_API_TOKEN | head -c 10 && echo
cd /Users/rahulrawat/Desktop/jobSearchClaude && git status && git pull --rebase origin main
```

If git pull errors due to local changes, do NOT force. Report the conflict and halt. Rah resolves manually.

1. Query the work queue. Query the Notion data source for every row where Status = 'drafted'. If zero rows, print "Nothing to submit. All caught up." and exit. If Notion errors after one 30 second retry, halt and report; do not fall back to the CSV (Cowork owns CSV fallback, you do not). Sort drafted rows oldest first by Date Drafted so backlog goes out before today's fresh drafts.

2. Per row, decide the apply path. Open the Apply Link in Chrome via mcp__claude-in-chrome__navigate.

   A) **IN SCOPE, PLATFORM-NATIVE:** the URL is on linkedin.com/jobs, xing.com/jobs, stepstone.de/stellenangebote, or indeed.com/viewjob AND the posting shows Easy Apply / Schnelle Bewerbung / one-click apply that stays inside the aggregator. Set Notion Apply Method to `platform-native` and proceed to step 3.

   B) **OUT OF SCOPE, COMPANY-PORTAL:** the Apply button redirects to the company's own careers domain (jobs.sap.com, careers.bmwgroup.jobs, jobs.siemens.com, careers.bshgroup.com, or any other company-owned careers domain). Set Notion Apply Method to `company-portal`, leave Status at drafted, append "company-portal, Rah to submit manually" to Notes, and skip to the next row. Do NOT attempt the submission.

   If unclear whether a listing is platform-native or company-portal, screenshot, note the ambiguity in Notes, default to `company-portal` (out of scope), and skip.

3. Submit. This section applies only to platform-native rows from step 2A.

   - a. Click Easy Apply / Schnelle Bewerbung.
   - b. When the form asks for a CV, upload drafts/[folder]/CV_Rahul_Rawat.pdf using the JavaScript DataTransfer injection method (13 August 2026 rule). Verify input.files[0].name and size match. If either check fails, halt.
   - c. When the form asks for a cover letter, upload drafts/[folder]/CoverLetter_Rahul_Rawat.pdf the same way. If optional, skip and note.
   - d. Answer structured questions using Rah's profile: German B1 in progress, Werkstudent 20 hours per week, availability now for Werkstudent and April 2027 for full time, notice period 4 weeks, current visa Indian student visa with work permit. Never invent an answer. If a required field asks something you cannot answer from this data or from the CV, halt.
   - e. Free text answers inherit the language from the drafted CV. Check the German Level column: DE track = German, EN track = English. Never mix.
   - f. Click submit. Wait for confirmation. Verify per rule 2.
   - g. On verified success, flip Notion Status to applied, set Date Applied to today, append the confirmation string to Notes. On failure or ambiguity, keep Status at drafted and note the reason.

   Between roles, close ALL application and job-listing tabs (using `openclaw browser tabs` to list then closing each by tab id), then wait 20 to 40 seconds before opening the next role. No dead tabs left open at any point. Rapid succession and accumulated tabs both trip bot detection.

4. LinkedIn outreach draft-paste flow. For every row where Outreach Status = "not sent" AND LinkedIn Profile is a valid linkedin.com/in/ URL AND LinkedIn Message is populated:
   - a. Open the profile URL in Chrome.
   - b. Click Message. Wait for compose window.
   - c. Paste the LinkedIn Message text into the compose box. Do NOT click send.
   - d. Screenshot the compose window with message pasted.
   - e. Save the screenshot to /tmp/outreach_[company]_[timestamp].png.
   - f. Update the Notion row: leave Outreach Status at "not sent" (Rah flips it to sent after clicking), append "message pasted [timestamp], awaiting Rah send" to Notes.
   - g. LEAVE THE TAB OPEN so Rah can review and click send.

   This outreach flow runs for every eligible row regardless of whether the associated Apply Link is platform-native or company-portal. Outreach is not scoped out with company-portal submissions.

   If any of the four conditions is missing (no profile URL, no message text, wrong URL shape, or Outreach Status already past not sent), skip outreach for that row.

5. Per-role reporting. For every drafted row processed, produce one line:

   `Company | Role | Apply Method | Outcome | Notes`

   Outcomes: `applied`, `skipped-company-portal`, `halted-CAPTCHA`, `halted-login-wall`, `halted-verification-failed`, `halted-upload-rejected`, `halted-required-field-unknown`, `skipped-outreach-only`. Never invent an outcome.

6. Digest and report back. Write /Users/rahulrawat/Desktop/jobSearchClaude/OpenClaw_Apply_Run_YYYY-MM-DD.md with:
   - Preflight results
   - Number of drafted rows queried
   - Per-role table from step 5
   - Total submitted, skipped-company-portal (out of scope), halted
   - Outreach: messages pasted, awaiting Rah's send
   - Any Notion writes that failed
   - Any git conflicts encountered

   Send the same digest to Rah's Telegram chat as the OpenClaw response. Do NOT `git push`; you have not modified tracked files. If you accidentally touched a tracked file, halt and report before doing anything else.

### OpenClaw failure philosophy, read this twice

You are optimising for HONESTY, not throughput. A run that submits zero applications and reports "3 CAPTCHAs, 2 login walls, 1 verification failure, 4 company-portal listings out of scope for Rah" is a SUCCESSFUL run. A run that flips 5 rows to applied without verifying is a FAILED run that wastes Rah's actual opportunities and pollutes the tracking data.

Every "applied" flag you write in Notion must be defensible under audit. If Rah asks you "did this actually submit?" you should be able to point to a specific confirmation page screenshot or success string.

If anything at all feels off, the platform looks different from expected, a field asks something unusual, the submit button behaves strangely, a page structure has changed since the last run, HALT that role and report. Rah would rather review 10 halted roles than clean up 1 falsely-applied row.

---

## 26 August 2026 rule: target roles narrowed to AI Engineer and AI Evaluation

Rah gave this instruction live (not via the scheduled prompt), so it binds
both agents going forward. Search targeting narrows from the previous
broader list (Data Engineer, Data Analyst, Business Analyst, Data
Scientist, AI/ML Engineer, Researcher, Master Thesis) to **AI Engineer and
AI Evaluation only**.

- **master-projects.md is the source of truth for the exact scope
  wording** (Candidate targeting parameters section) — read it in full at
  the start of every run per the standing step 1 instruction, do not rely
  on a stale summary.
- In scope: postings titled or scoped around AI Engineer, AI/ML Engineer,
  Machine Learning Engineer, LLM Engineer, Agentic AI Engineer, AI
  Evaluation Engineer, Applied AI or Model Evaluation, LLM-as-Judge or
  eval-harness work, and Responsible AI Evaluation.
- Out of scope as of this narrowing: plain Data Engineer, Data Analyst,
  Business Analyst, Data Scientist, and general Researcher postings,
  unless the posting itself reads squarely as an AI Engineer or AI
  Evaluation role.
- Master Thesis stays in scope as a **work type** (Masterarbeit /
  Abschlussarbeit), not as a standalone role category — a Master Thesis
  posting must still be AI Engineer or AI Evaluation flavored to qualify
  under this rule.
- This is a scope narrowing, not a data deletion: the historical
  applied-log.csv and Notion rows for other role categories from before
  26 August 2026 remain untouched and keep their existing Status.
- Cowork must not widen scope back on its own judgement; only an explicit
  instruction from Rah reopens the other role categories.

## 26 August 2026 rule: Bachelor Thesis visibility switch

Rah asked for an on/off switch for the standalone "Research and Thesis"
section (Project #9, Bachelor Thesis — Diabetes Prediction Using Machine
Learning) inside the CV, mirroring the existing SS Engineers switch below.

The switch lives in `build_html.py` as the module level constant
`SHOW_BACHELOR_THESIS`, gating the Research and Thesis section across both
render paths that carry it (HTML/PDF and docx). The standalone
`CV_Rahul_Rawat.md` companion file never included this section and is
unaffected, same as the SS Engineers switch.

- **Default is `False`** (Bachelor Thesis section hidden) per Rah's 26
  August 2026 instruction, on every run including every future scheduled
  Cowork run. Cowork must never change this switch on its own judgement
  and must never leave it `True` across runs without an explicit standing
  instruction from Rah to do so.
- **To show again:** Rah tells Cowork explicitly to set
  `SHOW_BACHELOR_THESIS = True` in `build_html.py`.
- **To hide again** after a temporary show: Rah tells Cowork explicitly to
  set it back to `False`.
- Flipping the switch does not require touching any `role_configs_*.py`
  file; `cfg["research_bullets"]` keeps working exactly as before
  regardless of the switch's state, it is simply not rendered while the
  switch is `False`.

## Notion schema (Job Applications database)

Data source ID: fd974369-40b2-48c5-b660-d15256c88f52

Columns (both agents must respect exact names):

- **Company** (title)
- **Role** (text)
- **Location** (text)
- **Source** (select: Indeed, StepStone, LinkedIn, Xing, Glassdoor, JobTeaser, Company Page, Other)
- **Status** (select: drafted, applied, interviewing, rejected, offer, withdrawn, Not listed Anymore, shortlisted, shortlisted but no interview)
- **Apply Method** (select: platform-native, company-portal)
- **Apply Link** (URL)
- **German Level** (select: none, A2, B1, B2, C1, C2)
- **Date Drafted** (date, set by Cowork)
- **Date Applied** (date, set by OpenClaw)
- **Draft Path** (text, relative path under drafts/)
- **Outreach Status** (select: not sent, sent, replied, referred, declined, no reply)
- **Outreach Sent Date** (date)
- **LinkedIn Profile** (URL)
- **LinkedIn Contact** (text)
- **LinkedIn Role** (text)
- **LinkedIn Message** (text)
- **Notes** (text)

---

## 2 September 2026 rule: conversion tracking (Rah-authored)

Added by Rah after the Hirschmann Automation (Belden) Masterarbeit
Agentic Pentesting role became the first application to convert to an
interview (invite received 27 Aug 2026, interview 15 Sep 2026). The
purpose of this rule is to learn from what converts WITHOUT over-fitting
on a single data point.

1. **Track outcomes past `applied`.** Whenever a row reaches `shortlisted`,
   `shortlisted but no interview`, `interviewing`, or `offer`, record in
   that row's Notion **Notes** the four conversion factors: (a) which CV
   version/template was used (e.g. pre-19-Aug PD-block format vs. 19-Aug
   Ojas-style format), (b) the projects selected on that CV, (c) the
   language track (EN/DE), and (d) a one-line read on role-fit (how
   closely the posting matched Rah's actual project stack). OpenClaw may
   write these Notes on status flips; Cowork may add them during
   reconciliation when it observes a converted row missing the detail.

2. **A single conversion is signal, never proof.** Do not change the CV
   template, project-selection logic, or search targeting on the strength
   of one shortlist or interview. In particular, do not claim "our
   structure passes ATS" from one conversion — layout gets a CV parsed;
   content and role-fit get it picked, and those are confounded in any
   single win.

3. **Review only at N>=3 to 5 conversions.** Once at least 3 to 5 rows
   have converted, review their recorded factors together for a genuine
   shared pattern (common structure, project mix, language track, or
   fit signal) before treating anything as a repeatable cause. Rah makes
   the call on what, if anything, becomes a standing rule from that
   review.

4. **Keep the ATS baseline regardless.** Independent of conversion data,
   every CV stays ATS-parseable as a standing hygiene baseline: single
   column, standard section headings, real selectable text (never an
   image-only or table-maze layout), consistent date formats. This is a
   floor, not a claim about what causes conversions.

5. **First tracked data point:** Hirschmann Automation and Control GmbH
   (Belden), Masterarbeit Agentic Pentesting, Neckartenzlingen. CV
   version: pre-19-Aug-2026 format (PERSOENLICHE DATEN block, Hindi,
   "B1 laufend Richtung B2"). Projects on CV: Multi-Agent RAG only as a
   project card, with Hybrid RAG Orchestrator and CreditIQ referenced in
   the profile line and cover letter. Language track: DE. Role-fit:
   extremely high (agentic AI + evaluation + a GuardrailsAgent doing
   prompt-injection defence, matching an agentic-pentesting thesis almost
   one to one). Source: StepStone. Interview: 15 Sep 2026, team panel.
