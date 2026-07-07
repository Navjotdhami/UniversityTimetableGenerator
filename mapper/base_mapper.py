import pandas as pd


class BaseMapper:
    """
    Base class for all mappers.

    Provides common helper methods for safely reading values
    from pandas DataFrames.
    """

    def __init__(self, dataframe):
        self.df = dataframe

    def get_str(self, row, column, default=""):

        value = row.get(column, default)

        if pd.isna(value):
            return default

        return str(value).strip()

    def get_int(self, row, column, default=0):

        value = row.get(column, default)

        if pd.isna(value):
            return default

        try:
            return int(float(value))
        except (ValueError, TypeError):
            return default

    def get_float(self, row, column, default=0.0):

        value = row.get(column, default)

        if pd.isna(value):
            return default

        try:
            return float(value)
        except (ValueError, TypeError):
            return default

    def is_blank(self, row, column):

        value = row.get(column)

        if pd.isna(value):
            return True

        if str(value).strip() == "":
            return True

        return False