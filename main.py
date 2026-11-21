import os
import shutil
from pathlib import Path


ENTRY = (
    "Your heel makes a small hollow in the wet sand. "
    "Water seeps in around the edges. A slip of sky lies in it. "
    "Far out past your toes, under miles of the same water, "
    "the sand lies in long folds, one after another."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    for child in output_dir.iterdir():
        if not child.is_symlink() and child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()

    (output_dir / "entry.txt").write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
