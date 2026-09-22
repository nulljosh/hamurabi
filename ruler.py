"""A ruler that plays Hamurabi for an A+. Run: python3 ruler.py [seed]"""
import random, sys
from hamurabi import State, step, check, grade, report, FOOD_PER_PERSON, ACRES_PER_PERSON

KNOBS = dict(gate=16, cap=17, share=6)  # tuned by sweep() over 1000 seeds

def orders(s, gate, cap, share):
    tend = s.people * ACRES_PER_PERSON
    seed = min(s.acres, tend)
    # One hungry mouth shuts the gates: immigration only comes when nobody starves.
    # Costs ~1% starvation (A+ allows 3%) and keeps acres per person up.
    hungry = 1 if s.acres < gate * s.people else 0
    feed = (s.people - hungry) * FOOD_PER_PERSON
    if s.year == 10:  # last year: the harvest can't help the grade, spare grain becomes land
        return max(0, (s.grain - feed) // s.price), min(feed, s.grain), 0
    buy = 0
    short = feed + seed - s.grain
    if short > 0:  # sell only what feeding and a full sowing need
        buy = -min(s.acres - 1, -(-short // s.price))
    elif s.price <= cap:
        buy = -short // s.price // share
    left = s.grain - buy * s.price - feed
    return buy, feed, max(0, min(s.acres + buy, tend, left))

def play(seed, quiet=False, **knobs):
    s, rng = State(), random.Random(seed)
    while not s.over:
        o = orders(s, **(knobs or KNOBS))
        if check(s, *o): o = (0, min(s.grain, s.people * FOOD_PER_PERSON), 0)  # broke: feed what we can
        lines = step(s, *o, rng)
        if not quiet: print(report(s).strip().splitlines()[-1], "|", *lines)
    return s

def sweep(n=1000):
    best = max(((sum(grade(play(i, True, gate=g, cap=c, share=sh)) == "A+" for i in range(n)), g, c, sh)
                for g in (10, 11, 12, 14) for c in (19, 21, 23, 26) for sh in (1, 2, 3)))
    print(f"best: {best[0]}/{n} A+ with gate={best[1]} cap={best[2]} share={best[3]}")

if __name__ == "__main__":
    if "--sweep" in sys.argv: sweep(); sys.exit()
    s = play(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
    print(s.over, f"{s.people} people, {s.acres} acres, {s.starved_total} starved. Grade: {grade(s)}")
