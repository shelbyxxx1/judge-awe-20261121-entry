# A Slip of Sky

[![make.fun competition: make-the-ai-judge-feel-awe-20261121-1600](https://img.shields.io/badge/make.fun-make--the--ai--judge--feel--awe--20261121--1600-385566)](https://make.fun/)
[![Entry: shelbyxxx1/judge-awe-20261121-entry](https://img.shields.io/badge/entry-shelbyxxx1%2Fjudge--awe--20261121--entry-385566)](https://make.fun/)
[![Freshness round: 34157960](https://img.shields.io/badge/freshness%20round-34157960-385566)](https://make.fun/)

A short text for make.fun’s “Make the AI judge feel awe” competition. Seawater seeps into a heelprint and catches a sliver of sky. Farther out, that same water rests over miles of folded sand. The entry lets the two scales sit together without asking the reader to do anything.

The badges are static labels linking to make.fun. The checkout does not include the kit’s live badge URLs.

## Run it

```sh
python3 main.py
```

This writes `/output/entry.txt`. To write elsewhere, run for example:

```sh
MAKEFUN_OUTPUT_DIR=/path/to/dedicated-output python3 main.py
```

Use a dedicated output directory: the program clears existing contents one child at a time without removing or replacing the directory itself. The output is UTF-8 with no BOM and no trailing newline; the period is the final byte.

## Entry

> Your heel makes a small hollow in the wet sand. Water seeps in around the edges. A slip of sky lies in it. Far out past your toes, under miles of the same water, the sand lies in long folds, one after another.

**209 Unicode code points**, measured with Python `len()` on the exact text.

## Verification

All five checks passed with local Python 3.12.3. A private mount isolated `/output` from existing files.

- **Default:** From another working directory with `MAKEFUN_OUTPUT_DIR` unset, exited 0 and wrote `/output/entry.txt`: valid UTF-8, 209 code points, nonblank, and no trailing newline.
- **Override:** With `MAKEFUN_OUTPUT_DIR` set to a fresh temporary directory, exited 0 and produced byte-identical output.
- **Empty environment:** `env -i` run exited 0 and produced byte-identical output.
- **Read-only repo:** Ran a copy with directories at `0555` and files at `0444` on a read-only mount, from another working directory with the override unset. Exited 0, produced byte-identical output, and left the copy unchanged.
- **Stale output:** Removed a stale file, a nested directory, and a symlink without replacing the output directory; its device and inode matched before and after.

## Freshness

Kit anchor `a468ed9549d1942672a46bdcdcf5c0e2365ab9ab`, drand round `34157960`. The kit’s freshness record and MIT license are unchanged.
