# How we ship harborpine-shop

Decision: trunk-based development, with short-lived release branches only when we must patch an old version.

Why:
- Small team (2-3 people), one live version of the shop
- Every pull request runs the tests on Python 3.11, 3.12 and 3.13
- Unfinished work stays on main behind feature flags (shop/flags.py)

Rules:
1. Branch from main, keep it under 2 days, merge with a pull request when checks are green.
2. Release from main: tag vMAJOR.MINOR.PATCH on a green commit, publish a GitHub release.
3. Hotfix an old release: fix on main first, then cherry-pick -x into release/X.Y.

Review this decision: when we support more than one live version.
