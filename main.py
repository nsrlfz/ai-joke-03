# Save the joke to the requested output directory.
import os
from pathlib import Path

joke = "My agent said 'Done!' The code doesn't run, but the confidence is production-ready."
output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(joke, encoding="utf-8")
