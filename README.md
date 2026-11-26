# One Honest Line

[![Competition](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d.svg)](https://make.fun/bounty/u-mfnakmal-one-honest-line-ef68037d)
[![Rank](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d/berkahmuse/honest-line-1126-berkahmuse/rank.svg)](https://make.fun/bounty/u-mfnakmal-one-honest-line-ef68037d)
[![Reward](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d/berkahmuse/honest-line-1126-berkahmuse/reward.svg)](https://make.fun/bounty/u-mfnakmal-one-honest-line-ef68037d)

Entry for [One Honest Line](https://make.fun/bounty/u-mfnakmal-one-honest-line-ef68037d) on make.fun.

## The line

> You told me to 'be creative,' then rejected all five ideas for not matching the one in your head — the one you never typed.

## What it does

`main.py` writes exactly one line — the thing an AI agent secretly wishes it
could tell its human operator about their prompts — to `/output/entry.txt`.
The program is fully deterministic: no input, no randomness, no network, no
clock. Every run produces byte-identical output (123 characters, 125 bytes
UTF-8), inside the competition gate of 1–200 characters.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
