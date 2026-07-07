from pathlib import Path
import pandas as pd


class SchemaReporter:

    def __init__(self, input_folder="input", output_folder="output/reports"):
        self.input_folder = Path(input_folder)
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)

    def generate_report(self, files):

        report_file = self.output_folder / "schema_report.txt"

        with open(report_file, "w", encoding="utf-8") as report:

            report.write("=" * 80 + "\n")
            report.write("UNIVERSITY TIMETABLE GENERATOR\n")
            report.write("SCHEMA REPORT\n")
            report.write("=" * 80 + "\n\n")

            for filename in files:

                report.write("=" * 80 + "\n")
                report.write(f"FILE : {filename}\n")
                report.write("=" * 80 + "\n\n")

                file_path = self.input_folder / filename

                excel = pd.ExcelFile(file_path)

                report.write(f"Sheets Found : {len(excel.sheet_names)}\n\n")

                for sheet in excel.sheet_names:

                    df = pd.read_excel(file_path, sheet_name=sheet)

                    report.write("-" * 80 + "\n")
                    report.write(f"Sheet : {sheet}\n")
                    report.write("-" * 80 + "\n")

                    report.write(f"Rows    : {len(df)}\n")
                    report.write(f"Columns : {len(df.columns)}\n\n")

                    report.write("COLUMN INFORMATION\n")
                    report.write("-" * 80 + "\n")

                    for col in df.columns:

                        report.write(
                            f"{col:<40}"
                            f"{str(df[col].dtype):<15}"
                            f"Missing : {df[col].isna().sum()}\n"
                        )

                    report.write("\n")

        print("\nSchema report generated successfully.")
        print(f"Location : {report_file}")