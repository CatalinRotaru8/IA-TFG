""" Module to process data."""

from typing import List
import pandas as pd
from sklearn.preprocessing import LabelEncoder

from src.utils.utils import get_list_of_files, get_file_path
from src.config import ProcessedData


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


def merge_and_process_yearly_data(years, file_name: str) -> None:
    """Merge and process the yearly data.

    Args:
        path_year (str): Path to the year folder
        file_name (str): Name of the file to process
        output_file_name (str): Name of the output file
    """
    result = None
    for year in years:
        short_year = "_".join(
            [y[-2:] for y in year.split("-")]
        )  # Convert '2017-2018' to '17_18'
        data_df = pd.read_csv(
            get_file_path(getattr(ProcessedData, f"files_{short_year}"), file_name)
        )
        data_df.rename(columns={f"Jugador{year}": "Jugador"}, inplace=True)

        if result is None:
            result = data_df
            result.drop(columns=[f"RL{year}"], axis=1, inplace=True)
        else:
            result = pd.merge(
                result, data_df, on="Jugador", how="outer", validate="one_to_one"
            )
            result.drop(columns=[f"RL{year}"], axis=1, inplace=True)

    result.fillna(0, inplace=True)
    result.to_csv(get_file_path(ProcessedData.all_years, file_name))


def encode_columns_in_dataframes(file_names, columns_dict):
    """Encode the columns in the dataframes.

    Args:
        files_names (_type_):
        columns_dict (dict): A dictionary where keys are the attribute names and values are lists of column names
    """
    dataframes = []

    # Create a LabelEncoder for each attribute
    encoders = {attr: LabelEncoder() for attr in columns_dict.keys()}

    # Load dataframes from csv files
    for file_name in file_names:
        df = pd.read_csv(get_file_path(ProcessedData.all_years, file_name), dtype=str)
        dataframes.append(df)

    # Train the label encoder with all unique data from the columns of interest
    for attr, columns in columns_dict.items():
        all_data = pd.concat(
            [df[col] for df in dataframes for col in columns if col in df]
        ).unique()
        encoders[attr].fit(all_data)

    # Transform the data of the columns of interest using the same label encoder
    for df in dataframes:
        for attr, columns in columns_dict.items():
            for col in columns:
                if col in df:
                    df[col] = encoders[attr].transform(df[col])

    # Save the transformed dataframes back to csv files
    for df, file_name in zip(dataframes, file_names):
        df.to_csv(get_file_path(ProcessedData.replace_strings, file_name), index=False)
