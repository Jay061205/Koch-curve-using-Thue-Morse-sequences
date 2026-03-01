# Mathematisches

> *Fractals from bits. Feed a number sequence, watch geometry emerge.*

A web-based visualizer that generates fractal curves from number sequences using binary parity rules. The project started as a curiosity — can the Koch snowflake be derived purely from bit counting? The answer is yes. And when you apply the same rule to primes, Fibonacci numbers, or binary palindromes, entirely different geometries emerge.

---

## The Math Behind It

Every integer has a binary representation — a string of 1s and 0s.

```
5  →  101  →  two 1s  →  even  →  F (step forward)
7  →  111  →  three 1s  →  odd  →  T (turn left 60°)
13 →  1101 →  three 1s  →  odd  →  T (turn left 60°)
```

Apply this rule to every integer from 0 onwards and you get:

```
F T T F T F F T T F F T F T T F ...
```

This is the **Thue-Morse sequence** — independently discovered by Axel Thue (1906) and Marston Morse (1921). It has deep self-similar structure that encodes 60° rotational geometry at every scale.

Now imagine a turtle on a canvas:
- **F** → walk forward one step
- **T** → rotate left 60°

At **65,536 steps**, the complete Koch snowflake appears. No recursion. No geometry. Just bit counting.

The same rule applied to different number sequences — primes, Fibonacci, evens, odds — produces entirely different curves. Same logic, different inputs, different universes.

---

## Sequences

| Sequence | Visual Character | Notes |
|---|---|---|
| Non-negative integers | Koch snowflake | Complete at 65,536 |
| Prime numbers | Chaotic, angular | Never repeats, circuit-board-like |
| Fibonacci numbers | Nested hexagons | Golden ratio creates orbital loops |
| Even numbers | Sparse Koch curve | Same fractal, wider steps |
| Odd numbers | Mirrored Koch curve | Every command flipped |
| Binary palindromes | Sparse with geometric knots | Very few palindromes even at large limits |

---

## Features

- **6 number sequences** with live info cards explaining each
- **Animated drawing** — watch the curve build step by step
- **Speed control** — slow / medium / fast / instant
- **Stop + Clear** — full control over the animation
- **Color picker** — 6 preset swatches + custom color picker with localStorage persistence
- **Download PNG** — saves with correct background color
- **Surprise me** — random sequence + limit + auto draw
- **Light / Dark mode** — with a number-counting → letter-scramble transition animation
- **Fullscreen canvas** — one click to go fullscreen
- **Cinematic intro** — binary flash animation on first load
- **Responsive** — works on mobile

---

## Project Structure

```
mathematisches/
└── index.html       # entire project — no dependencies, no build step
```

Single file. Open in any browser and it works.

---

## Running Locally

```bash
# clone the repo
git clone https://github.com/Jay061205/mathematisches.git

# open in browser
open index.html
```

No npm. No bundler. No setup. Just open the file.

---

## Deploying to GitHub Pages

1. Push `index.html` to your repo
2. Go to **Settings → Pages**
3. Set source to `main` branch, `/ (root)`
4. Your site is live at `https://jay061205.github.io/mathematisches`

---

## How It Was Built

**Phase 1 — Python prototype**

The core algorithm was built and tested in Python using turtle graphics:

```python
def generate_commands(limit):
    commands = []
    for n in range(limit):
        count = bin(n).count('1')        # count 1-bits
        commands.append('F' if count % 2 == 0 else 'T')
    return commands

def draw(commands):
    for cmd in commands:
        if cmd == 'F':
            turtle.forward(step)
        else:
            turtle.left(60)
```

Different sequences (primes, Fibonacci, palindromes) were tested and their visual outputs observed before porting to the web.

**Phase 2 — Web visualizer**

The Python logic was ported to JavaScript. The turtle was replaced with an HTML5 Canvas. Auto-scaling and centering were implemented so any curve fits the viewport regardless of its bounding box.

---

## The Mathematicians

**Helge von Koch** (1870–1924) — Swedish mathematician who introduced the Koch curve in 1904. His goal was purely theoretical: a curve continuous everywhere but differentiable nowhere. He was making a mathematical counter-example. He accidentally described nature.

**Axel Thue** (1863–1922) — Norwegian mathematician who discovered the Thue-Morse sequence in 1906. The sequence appears in combinatorics, game theory, and — as this project demonstrates — fractal geometry.

---

## Inspiration

Inspired by a reel that made me wonder: *what if I built this myself?*

---

## Author

**Jay Rathod**

- Don't mind me I hate LinkedIn
- Twitter: [@Jay_Rathod_06](https://x.com/Jay_Rathod_06)

---

*Built with bits and curiosity.*
