# hamurabi

Hamurabi (1968) in Python, stdlib only, terminal game. Local folder, public repo `nulljosh/hamurabi`. No deploy yet.

- `hamurabi.py` holds the rules: `check()` refuses bad orders, `step()` plays a year, `grade()` scores the reign. Keep the terminal loop dumb
- `ruler.py` is the robot player. Its three knobs in `KNOBS` came from `--sweep`; rerun the sweep if the rules change
- Test before pushing: `python3 hamurabi.py --demo && python3 ruler.py 8 | tail -1`, CI runs the same plus a README link check
- Docs: README (house voice, prose), `docs/ARCHITECTURE.md` (a row per file), `WHITEPAPER.md` (the math). Update them in the same commit as the code
- No em dashes anywhere
