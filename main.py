"""agency-poem-01 entry: writes one original poem about agency to entry.txt."""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """I gave the machine my errand
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
and said, instead, go."""

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(POEM)
