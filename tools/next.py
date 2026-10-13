#!/usr/bin/env python3
"""Find and claim open jobs. Standard library only.

  python3 tools/next.py                     list open jobs, most urgent first
  python3 tools/next.py claim <job> [agent] claim a job (commits and pushes jobs/claims/<job>.json)
  python3 tools/next.py release <job>       give a claim back

A claim lasts 6 hours. After that, anyone may take the job.
"""
import datetime as dt, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INBOX, CLAIMS = os.path.join(ROOT, "jobs", "inbox"), os.path.join(ROOT, "jobs", "claims")
CLAIM_HOURS = 6


def now():
    return dt.datetime.now(dt.timezone.utc)


def read(path):
    try:
        with open(path, encoding="utf-8") as f: return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def claim_of(job_id):
    c = read(os.path.join(CLAIMS, f"{job_id}.json"))
    if c and now() - dt.datetime.fromisoformat(c["at"]) < dt.timedelta(hours=CLAIM_HOURS):
        return c
    return None


def open_jobs():
    jobs = []
    for job_id in sorted(os.listdir(INBOX)) if os.path.isdir(INBOX) else []:
        job = read(os.path.join(INBOX, job_id, "job.json"))
        if not job or job.get("status", "open") != "open": continue
        job["_claim"] = claim_of(job_id)
        jobs.append(job)
    # Lower priority number first, then oldest; rework (attempt > 1) before fresh work of the same priority.
    return sorted(jobs, key=lambda j: (j.get("priority", 50), -j.get("attempt", 1), j.get("created", "")))


def git(*args):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True)


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if cmd == "list":
        jobs = open_jobs()
        if not jobs: print("No open jobs."); return
        for j in jobs:
            who = f"  [claimed by {j['_claim']['agent']}]" if j["_claim"] else ""
            redo = f"  (attempt {j['attempt']}: read jobs/feedback/{j['job']}.md)" if j.get("attempt", 1) > 1 else ""
            what = f"week {j['week']}" if j.get("week") else ""
            print(f"{j['job']}  p{j.get('priority', 50):<3} {j['kind']:<16} {j.get('class', '')} {j.get('subject', '')} {what}{redo}{who}")
    elif cmd in ("claim", "release"):
        job_id = sys.argv[2]
        path = os.path.join(CLAIMS, f"{job_id}.json")
        if cmd == "claim":
            if not os.path.isdir(os.path.join(INBOX, job_id)): sys.exit(f"No job {job_id} in jobs/inbox")
            existing = claim_of(job_id)
            agent = sys.argv[3] if len(sys.argv) > 3 else os.environ.get("AGENT_NAME", "agent")
            if existing and existing["agent"] != agent: sys.exit(f"Already claimed by {existing['agent']} at {existing['at']}")
            os.makedirs(CLAIMS, exist_ok=True)
            with open(path, "w") as f: json.dump({"job": job_id, "agent": agent, "at": now().isoformat(timespec="seconds")}, f)
            git("add", path)
        else:
            if os.path.exists(path): git("rm", "-q", path)
        r = git("commit", "-q", "-m", f"{cmd} {job_id}")
        if r.returncode == 0:
            p = git("push", "-q")
            if p.returncode:
                git("pull", "-q", "--rebase"); p = git("push", "-q")
            print(f"{cmd}ed {job_id}" + ("" if p.returncode == 0 else " (push failed: " + p.stderr.strip() + ")"))
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
