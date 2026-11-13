import os
from pathlib import Path

JOKE = "My agent's code passed all the tests — the tests were written by my agent too."

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
