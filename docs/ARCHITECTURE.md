# Architecture

The whole game is one file. The city is a small record holding the year, people, grain, land and the going price of land. Every year you give three orders. The game first checks the orders are possible, then plays the year out: it pays for land, sets aside food and seed, rolls the harvest, lets the rats in, counts who starved, invites newcomers, and maybe sends a plague.

| File | What it owns |
|---|---|
| `hamurabi.py` | Game state, order checks, the yearly step, the terminal loop, and the `--demo` self-check. |
| `.github/workflows/test.yml` | CI: runs the self-check, plays a scripted game end to end, checks README links. |
