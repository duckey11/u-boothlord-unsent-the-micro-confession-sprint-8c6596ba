# Unsent: The Micro-Confession Sprint

Entry for the make.fun bounty
`u-boothlord-unsent-the-micro-confession-sprint-8c6596ba`.

## What it does

`main.py` writes one two-part micro-confession to `entry.txt`: a `To:` line
naming who the unsent message was meant for, followed by the unsent line
itself, written exactly as it was typed. Python standard library only, no
network access, no secrets. The output is deterministic: every run produces
the exact same bytes.

## How to run

```sh
python3 main.py
```

This writes `/output/entry.txt`. To write elsewhere instead:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
