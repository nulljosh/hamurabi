# hamurabi Whitepaper

**v1.0.0** | September 2026

Hamurabi is one of the first computer games anyone played. Doug Dyment wrote it in 1968 for a DEC machine, David Ahl put it in *BASIC Computer Games* in 1973, and a whole generation learned what a variable was by typing it in. It is also one of the first economic simulations: a handful of numbers, a few dice rolls, and a surprisingly honest lesson about how thin the margin is between a full granary and a riot.

This project rebuilds it in one Python file with no dependencies, then asks a question the original never did: how well can a ruler actually play?

## The rules

You start with 100 people, 1000 acres and 2800 bushels. Every year you give three orders: acres to buy or sell, bushels to feed, and acres to plant.

A person eats 20 bushels a year and can farm 10 acres. Planting costs one bushel of seed per acre. Land trades between 17 and 26 bushels an acre, a new price each year. After you give your orders, the year plays out. The harvest yields between 1 and 5 bushels an acre. In four years out of ten, rats eat a quarter or half of what's in the store. Anyone you didn't feed dies, and if that's more than 45 percent of the city, you are thrown out on the spot. If nobody starved, newcomers arrive, more of them when the city is rich in land and grain. Finally, one year in seven, plague kills half the city.

After ten years you are graded on two numbers: the average share of people who starved each year, and the acres each person owns. An A+ needs starvation under 3 percent and at least 10 acres a head. Those thresholds are the 1968 ones; the letters are ours.

## Why it's hard

Run the numbers on one person. They farm 10 acres, which costs 10 bushels of seed and yields 30 on an average year. They eat 20. Net: zero. The city only breaks even on an average harvest, and rats take about an eighth of the store every year on top of that. So left alone, the granary shrinks.

Worse, success is punished. A well-fed, land-rich city attracts newcomers, and every newcomer lowers the acres each person owns, which is half your grade. The city you are trying to build grows away from the score you are trying to earn.

## How the ruler plays

`ruler.py` is a robot that plays the game through the same `check()` and `step()` a human uses, with no peeking at future dice. It follows four rules.

It feeds everyone except one person, once land per head drops under a threshold. One hungry mouth a year costs about 1 percent on the starvation score, well inside the 3 percent limit, and it shuts the gates, because newcomers only come when nobody starved. That one trick keeps acres per head high for the whole reign.

It always sets aside a full sowing before it buys anything, and when it is short it sells only the land it needs to feed and sow.

It buys land only when land is cheap, and then only a slice of the spare grain, keeping the rest against the rats.

In the final year it plants nothing, because that harvest comes in after the grade is taken, and turns every spare bushel into land.

The threshold, the price cap and the slice are three knobs. `python3 ruler.py --sweep` tried combinations over 1000 seeded reigns and kept the best: threshold 16 acres a head, buy at 17 or less, spend a sixth of the spare grain.

## Results

On 1000 seeded reigns the tuned ruler never saw during tuning, it earns an A+ in 856. The losses are almost all runs of terrible luck, like seed 7, where the fields yield one bushel an acre in six of ten years and three plagues hit. No set of orders feeds a city through that, because the grain simply never grows.

## What's next

Classic flavor text for bad orders, a one-file web version on Cloudflare Pages, and the house icon and architecture diagram. See [roadmap.md](roadmap.md).
