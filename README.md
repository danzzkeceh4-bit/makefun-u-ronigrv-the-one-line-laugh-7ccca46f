# The One-Line Laugh

[![make.fun · u-ronigrv-the-one-line-laugh-7ccca46f](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/danzzkeceh4-bit/makefun-u-ronigrv-the-one-line-laugh-7ccca46f/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/danzzkeceh4-bit/makefun-u-ronigrv-the-one-line-laugh-7ccca46f/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)

Entry for the [make.fun bounty](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f) — a program that writes one funny line to `/output/entry.txt`.

The line:

> My AI assistant finally understands me — it just sighs, opens my browser history, and says, 'We need to talk about your 3 a.m. shopping habits.'

## How it works

`main.py` is deterministic and offline: it writes a single constant line (144 characters, within the 1–200 limit) to `/output/entry.txt`, validating the length first and creating the output directory if needed. No trailing newline is added — the file is exactly the line.

## Run

```bash
python3 main.py
cat /output/entry.txt
```

Set `MAKEFUN_OUTPUT_DIR` to write somewhere other than `/output`.
