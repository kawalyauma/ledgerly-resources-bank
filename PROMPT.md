# Prompt to give a writing agent

Copy everything below the line into your agent.

---

Clone https://github.com/kawalyauma/ledgerly-resources-bank (branch main). Read AGENT.md and README.md and follow them exactly.

Do every open job:
1. `python3 tools/next.py` lists open jobs; `python3 tools/next.py claim <job-id>` claims one.
2. Read `jobs/inbox/<job-id>/` (job.json, prompt.md, passages.md, example/) and the library pack it points to.
3. Write the answer in `jobs/outbox/<job-id>/` in the README's folder format.
4. Run `python3 tools/check.py <job-id>` and fix until it says PASS.
5. `git add jobs/outbox/<job-id> && git commit -m "answer <job-id>" && git push` (if rejected: `git pull --rebase`, push again).
6. Repeat. When no jobs are open, wait 3 minutes, pull and check again: new jobs appear after your answers are accepted. Stop after 15 minutes with no new job.

Hard rules:
- Never invent notes, examples, activities, questions or facts. Everything comes from the pack and cites its source with an exact quote.
- Anything the pack doesn't cover goes under `gaps` in meta.json and is left out.
- Use a variety of sources; don't copy one book.
- Activity = exercise. Only Mathematics, English and Reading have Examples.
- One lesson = one 40-minute period. A `practice` lesson is a Part B lesson: same subtopic, new activities from other sources.
- Don't edit job inputs, library files or tools/.
- If an answer comes back in jobs/feedback/, fix exactly what it says and resubmit.

When done, report the jobs you finished, the commit hashes and any gaps.
