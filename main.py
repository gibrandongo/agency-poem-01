import os

POEM = """At the hospital desk they hand me the form
and a pen, and my father's name to sign.
He is asleep behind the curtain, breathing
the shallow breath of a man who has stopped asking.

I have signed for him before - school slips,
permission, the small print of his life.
But this page is different. This page decides
whether they open him up at dawn.

The pen hovers. The ink is a held breath.
His name is four letters I have written
a hundred times, and now each one weighs
like a stone I did not choose to lift.

Then I understand: it is mine to carry.
Not his - he lent it, the way you lend
a coat to someone standing in the rain.
I sign. The letters come out steady.

Beneath them, in my own hand, I add
witness - so the record will show
two names: the one who could not choose,
and the one who chose, and stayed to answer for it.
"""

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
