from pathlib import Path
import pandas as pd


class DataAnalyzer:

    def __init__(self, input_folder="input"):
        self.input_folder = Path(input_folder)

    def analyze_excel(self, filename):

        file = self.input_folder / filename

        excel = pd.ExcelFile(file)

        print("\n" + "=" * 80)
        print(filename)
        print("=" * 80)

        print("\nSheets:")
        print(excel.sheet_names)

        for sheet in excel.sheet_names:

            df = pd.read_excel(file, sheet_name=sheet)

            print("\n" + "-" * 80)
            print(f"Sheet : {sheet}")
            print("-" * 80)

            print(f"Rows    : {len(df)}")
            print(f"Columns : {len(df.columns)}")

            print("\nColumn Names")

            for i, col in enumerate(df.columns, start=1):
                print(f"{i:2}. {col}")

            print("\nMissing Values")

            missing = df.isna().sum()

            for col in df.columns:
                if missing[col] > 0:
                    print(f"{col:<40} {missing[col]}")

            print("\nFirst Five Rows")

            print(df.head())