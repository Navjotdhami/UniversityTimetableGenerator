from pathlib import Path

import pandas as pd


class LoadCompleteData:

    def __init__(self):

        self.file = Path("input") / "Complete Load Data.xlsx"

    def load(self):

        return pd.read_excel(self.file)