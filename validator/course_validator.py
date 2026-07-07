import pandas as pd


class CourseValidator:

    def __init__(self, dataframe):
        self.df = dataframe

        self.results = {}

    def validate(self):

        print("\nValidating Course Data...")
        print(f"Total Records : {len(self.df)}")

        self.results["Missing Course Code"] = self.check_missing("Course Code")
        self.results["Missing Course Title"] = self.check_missing("Course Title")
        self.results["Missing Section"] = self.check_missing("Section")
        self.results["Missing Final Section"] = self.check_missing("FINAL SECTION")

        self.results["Missing Year"] = self.check_missing("Year")
        self.results["Missing Term"] = self.check_missing("Term")

        self.results["Missing Students"] = self.check_missing("No of Students")

        self.results["Missing L"] = self.check_missing("L")
        self.results["Missing T"] = self.check_missing("T")
        self.results["Missing P"] = self.check_missing("P")

        self.results["Invalid Groups"] = self.check_invalid_groups()

        self.print_summary()

    def check_missing(self, column):

        if column not in self.df.columns:
            print(f"\n⚠ Column '{column}' not found.")
            return 0

        missing = self.df[self.df[column].isna()]

        count = len(missing)

        print(f"\n{column}")
        print(f"Missing : {count}")

        if count > 0:

            print("First 5 rows:")

            for idx in missing.head(5).index:

                print(f"   Excel Row {idx + 2}")

        return count

    def check_invalid_groups(self):

        if "Groups" not in self.df.columns:
            return 0

        invalid = self.df[
            (self.df["Groups"].fillna(0) <= 0)
        ]

        count = len(invalid)

        print(f"\nGroups <= 0 : {count}")

        if count > 0:

            print("First 5 rows:")

            for idx in invalid.head(5).index:

                print(f"   Excel Row {idx + 2}")

        return count

    def print_summary(self):

        print("\n" + "=" * 60)
        print("COURSE VALIDATION SUMMARY")
        print("=" * 60)

        for key, value in self.results.items():

            print(f"{key:<30}: {value}")

        print("=" * 60)