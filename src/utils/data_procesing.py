""" Module to process data."""

from typing import List
import pandas as pd

from src.utils.utils import get_list_of_files, get_file_path


def sum_values_from_duplicate_player(
    file_path: str, excluded_columns: List[str]
) -> None:
    """Group the data by 'Jugador' and sum the numeric columns.

    Args:
        file_path (str): file path to read the data
        excluded_columns (List[str]): List of columns to exclude
    """
    year = file_path.split("/")[3]
    print(f"Processing data from {file_path}")
    files = get_list_of_files(file_path)
    for file in files:
        print(file)

        orginal_df = pd.read_csv(get_file_path(file_path, file))
        df_numeric = orginal_df[orginal_df.columns.difference(excluded_columns)]

        # List of columns to convert(all except 'Jugador' which is string)
        cols_to_convert = df_numeric.columns.difference(["Jugador"])

        # Convert the columns to numeric
        for col in cols_to_convert:
            df_numeric.loc[:, col] = pd.to_numeric(df_numeric[col], errors="coerce")

        df_sum = df_numeric.groupby("Jugador").sum().reset_index()

        df_excluded = orginal_df[excluded_columns + ["Jugador"]].drop_duplicates(
            "Jugador"
        )
        # Ensure that 'Jugador' is of the same type in both dataframes
        df_excluded["Jugador"] = df_excluded["Jugador"].astype(str)
        df_sum["Jugador"] = df_sum["Jugador"].astype(str)

        processed_df = pd.merge(
            df_excluded,
            df_sum,
            on="Jugador",
            how="left",
            validate="one_to_one",
        )
        processed_df = processed_df.reindex(columns=orginal_df.columns).rename(
            columns=lambda x: x + year
        )
        processed_df.to_csv(get_file_path(file_path, file), index=False)
