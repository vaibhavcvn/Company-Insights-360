import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

files = [
    "sales.xls",
    "employees.xls",
    "departments.xls"
]

for file in files:
    input_path = DATA_DIR / file
    df = pd.read_csv(input_path)

    output_path = DATA_DIR / (Path(file).stem + ".csv")
    df.to_csv(output_path, index=False)

    print(f"Created: {output_path.name}")

print("Conversion completed!")