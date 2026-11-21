# Handoff: gift wrap charged when the box is not ticked

Summary: every order paid the $2.99 gift wrap fee, even with the box unticked.
Impact: main only, since b1ff7ef was merged. Release v1.0.0 is not affected.
Detected: customer report. Reproduced with check_wrap.py: total 2198, expected 1899.

## Root cause
git bisect run python3 check_wrap.py, good a67ccf2, bad 2e076ae
First bad commit: b1ff7ef "Make gift_wrap optional in cart_total"
It changed the check to "gift_wrap is not None", so gift_wrap=False still paid.

## Fix
Reverted b1ff7ef with git revert: shared history is not rewritten.
New test: test_no_gift_wrap_fee_when_unticked, so it cannot come back.
Pull request #5: checks green on Python 3.11, 3.12 and 3.13.

## How to verify
python3 -m unittest
cart_total([(1200, 1)], gift_wrap=False) returns 1899

## Follow-ups
1. Sam: if gift_wrap must be optional, keep False as the default, test first.
2. Team: test explicit True and False for every cart_total option.
