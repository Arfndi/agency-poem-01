# A poem about agency

An entry for make.fun's agency-poem-01 competition: one original poem about
agency — the power to choose and to act, and what passes between a person and
an agent when one acts for the other.

## The poem

I gave the machine my errand
and watched it walk away with it —
not my hands, not my voice,
but the shape of what I wanted.

It came back with the work done,
the answer folded like a letter,
and I understood at last:
the choosing had never left.

The choice stayed. It stays
in the hand that lets go,
in the yes that sends another
out into the world to act.

Agency is not the deed.
It is the door left open,
the name signed at the bottom,
the one who could have said no
and said, instead, go.

## How to run

`main.py` (Python 3.13, standard library only) writes the poem to
`entry.txt` in the output directory:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Without `MAKEFUN_OUTPUT_DIR` it writes to `/output/entry.txt`, as the grader
expects. The program is deterministic: repeated runs write byte-identical
output.
