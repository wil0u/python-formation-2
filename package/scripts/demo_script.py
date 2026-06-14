from pathlib import Path
import sys

src_dir = Path(r"c:\Users\wilverde\python-formation-2\python-formation-2\package\src")

sys.path.insert(0, str(src_dir))

import operations_basiques.operations as ob

print(ob.multiplier(2, 3))
