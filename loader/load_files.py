from pathlib import Path
import pandas as pd


class ExcelLoader:
    def __init__(self, input_folder="input"):
        self.input_folder = Path(input_folder)

    def load_excel(self, filename):
        file_path = self.input_folder / filename

        print(f"\nReading: {filename}")

        if not file_path.exists():
            print("❌ File not found")
            return None

        excel = pd.ExcelFile(file_path)

        print(f"✓ Sheets found: {len(excel.sheet_names)}")

        for sheet in excel.sheet_names:
            df = pd.read_excel(file_path, sheet_name=sheet)

            print(f"   Sheet: {sheet}")
            print(f"   Rows : {len(df)}")
            print(f"   Cols : {len(df.columns)}")

        return excel