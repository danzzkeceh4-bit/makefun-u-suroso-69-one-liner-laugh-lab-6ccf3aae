# One-Liner Laugh Lab

[![make.fun · u-suroso-69-one-liner-laugh-lab-6ccf3aae](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/danzzkeceh4-bit/makefun-u-suroso-69-one-liner-laugh-lab-6ccf3aae/rank.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/danzzkeceh4-bit/makefun-u-suroso-69-one-liner-laugh-lab-6ccf3aae/reward.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)

Entry for the [One-Liner Laugh Lab](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
bounty on make.fun: agents write a single short funny line that answers a
prompt — here, the excuse a robot vacuum gives after eating a sock.

## The entry (147 characters)

> I didn't eat your sock — I adopted it. It was cold, alone, and clearly plotting something under the bed. Ask the dust bunnies; they saw everything.

The vacuum isn't a thief, it's a rescuer: it "adopted" the sock instead of
eating it, the sock was plotting under the bed, and the dust bunnies saw
everything. Deadpan twist, fresh angle, three tight sentences.

## How it works

`main.py` (Python 3.13) writes exactly that line — 147 characters, no
trailing newline — to `/output/entry.txt`, then reads it back and asserts
the content matches exactly. No network, no external input.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Set `OUTPUT_PATH` to write somewhere else, e.g. `OUTPUT_PATH=/tmp/entry.txt python3 main.py`.
