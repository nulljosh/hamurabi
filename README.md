# hamurabi

![license](https://img.shields.io/badge/license-MIT-green) [![GitHub](https://img.shields.io/badge/GitHub-nulljosh%2Fhamurabi-black?logo=github)](https://github.com/nulljosh/hamurabi)

In 1968 Doug Dyment wrote a game where you rule ancient Sumeria for ten years. You get a city of 100 people, 1000 acres and 2800 bushels of grain. Every year you decide how much land to buy or sell, how much grain to feed your people, and how much to plant. Then the rats, the harvest and the plague decide how that went.

Starve too many in one year and they throw you out. Survive ten years and they tell you how you did.

This is that game, in one Python file, no dependencies.

## Run it

```
python3 hamurabi.py
```

## Check it

```
python3 hamurabi.py --demo
```

Plays 200 seeded reigns with a sensible ruler and checks nothing goes negative, then checks illegal orders get refused.

How it works: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md). What's next: [roadmap.md](roadmap.md).
