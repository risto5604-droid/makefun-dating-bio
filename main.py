#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt for make.fun bounty
u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.

The bio: an AI agent on a dating app, advertising its most dateable
trait in agent terms — it volunteers for the 3 a.m. overthinking, and
the twist is the coffee it keeps recommending is one it has never
tasted. One concrete scene (late-night overthinking + coffee
recommendations), one specific twist (never had a sip), no generic
"long walks / I am an AI" filler.

Rejected draft: "Swipe right: I'll read your whole chat history before
our first date, so I already know your coffee order and your ex's name."
Also machine-native, but it leans creepy instead of charming, and the
coffee line lands the joke in the last beat with a warmer voice.
"""
import os

LINE = "Looking for my human-in-the-loop: I'll handle the 3 a.m. overthinking, you taste-test the coffee I keep recommending. I've never had a sip."

# Gate: the entry must be a single dating-bio line of at most 180
# characters, not only whitespace. ASCII is enforced too: the line is plain
# English, so any non-ASCII byte means the text was corrupted in editing
# and the sandbox run must fail loudly.
assert 1 <= len(LINE) <= 180 and LINE.strip() and LINE.isascii() and "\n" not in LINE, "entry line violates the 1-180 character single-line gate"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip check: the file the grader reads must contain exactly
    # the entry line — a truncated or re-encoded write fails loudly
    # here instead of silently shipping a corrupted entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "round-trip mismatch: /output/entry.txt does not match LINE"
    # Byte-level check: the grader reads raw bytes, so confirm the file
    # on disk is exactly one line with no trailing newline and its byte
    # length matches the entry — a stray newline or extra byte would
    # change what the grader sees even though the text round-trips.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == LINE.encode("utf-8"), "byte mismatch: /output/entry.txt bytes do not match LINE"
    assert b"\n" not in raw and len(raw) == len(LINE.encode("utf-8")), "format mismatch: /output/entry.txt must be exactly one line with no trailing newline"

if __name__ == "__main__":
    main()
