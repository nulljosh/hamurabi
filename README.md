# hamurabi

![version](https://img.shields.io/badge/version-v1.0.0-blue) ![python](https://img.shields.io/badge/python-3.10%2B-blue) ![deps](https://img.shields.io/badge/dependencies-none-brightgreen) [![tests](https://github.com/nulljosh/hamurabi/actions/workflows/test.yml/badge.svg)](https://github.com/nulljosh/hamurabi/actions/workflows/test.yml) ![license](https://img.shields.io/badge/license-MIT-green) [![GitHub](https://img.shields.io/badge/GitHub-nulljosh%2Fhamurabi-black?logo=github)](https://github.com/nulljosh/hamurabi)

In 1968 Doug Dyment wrote a game where you rule ancient Sumeria for ten years. You get a city of 100 people, 1000 acres and 2800 bushels of grain. Every year you decide how much land to buy or sell, how much grain to feed your people, and how much to plant. Then the rats, the harvest and the plague decide how that went.

Starve too many in one year and they throw you out. Survive ten years and they tell you how you did.

This is that game in one Python file with no dependencies, plus a robot ruler that plays it for the top grade.

## Run it

```
python3 hamurabi.py
```

## Check it

```
python3 hamurabi.py --demo
```

Plays 200 seeded reigns with a sensible ruler and checks nothing goes negative, then checks illegal orders get refused.

## Watch a ruler play

```
python3 ruler.py 8
python3 ruler.py --sweep
```

`ruler.py` plays for the top grade. It feeds everyone but one person a year, which shuts the city gates to newcomers and keeps land per head high, buys land only when it's cheap, and pours every spare bushel into land in the final year. It gets an A+ in about 86 of every 100 reigns it has never seen. The rest are years like seed 7, where the fields yield one bushel an acre six years out of ten and nobody could save that city.

How it works: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md). Why and the math behind it: [WHITEPAPER.md](WHITEPAPER.md). What's next: [roadmap.md](roadmap.md).
