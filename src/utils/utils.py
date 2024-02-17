""" This module contains the constants used in the project. """

import os
import pandas as pd
from src.config import (
    Directories,
    DeleteLines,
    FileName,
    CleanData,
    TransfermarktData,
    TransfermarketFiles,
    InputData,
)


def get_file_path(folder_path: str, file_name: str | None) -> str:
    """
    Get the file path.

    Args:
        folder_path (str): Path to the folder where the file is located.
        file_name (str): Name of the file.

    Returns:
        str: File path.
    """
    if file_name is None:
        file_path = Directories.get_project_root(Directories) + folder_path
    else:
        file_path = Directories.get_project_root(Directories) + folder_path + file_name

    if os.path.isfile(file_path):
        return file_path
    raise FileNotFoundError("The file does not exist.")


def get_list_of_files(folder_path: str) -> list[str]:
    """
    Get the list of files in a folder.

    Args:
        folder_path (str): Path to the folder.

    Returns:
        list[str]: List of files in the folder.
    """
    return os.listdir(Directories.get_project_root(Directories) + folder_path)


def string_to_list(string: str) -> list[str]:
    """
    Convert a string to a list.

    Args:
        string (str): String to convert.

    Returns:
        list[str]: List with the elements of the string.
    """
    return [item.strip() for item in string.split(",")]


def delete_duplicate_line_from_file(file_path: str, lines_to_delete: str) -> None:
    """
    Delete duplicate lines from a file.

    Args:
        file_path (str): Path to the file.
        lines_to_delete (str): Lines to delete.
    """
    dataframe = pd.read_csv(file_path)
    mask = dataframe.apply(
        lambda row: not all(row.isin(string_to_list(lines_to_delete))),
        axis=1,
    )
    dataframe = dataframe[mask]
    dataframe.to_csv(file_path, index=False)


def change_header_from_file(file_path: str, lines_to_delete: str) -> None:
    """
    Change the header of a file.

    Args:
        file_path (str): Path to the file.
        lines_to_delete (str): Lines to delete.
    """
    dataframe = pd.read_csv(file_path)
    dataframe.columns = string_to_list(lines_to_delete)
    dataframe.to_csv(file_path, index=False)


def delete_last_column_from_file(file_path: str) -> None:
    """
    Delete the last column of a file.

    Args:
        file_path (str): Path to the file.
    """
    dataframe = pd.read_csv(file_path)
    dataframe = dataframe.drop(dataframe.columns[-1], axis=1)
    dataframe.to_csv(file_path, index=False)


def transform_file(file_path: str) -> None:
    """
    Transform the file.

    Args:
        file_path (str): Path to the file.
    """
    files = get_list_of_files(file_path)
    for file in files:
        if file == FileName.acciones_defensivas:
            delete_duplicate_line_from_file(
                get_file_path(file_path, file), DeleteLines.acciones_defensivas
            )
            change_header_from_file(
                get_file_path(file_path, file), DeleteLines.acciones_defensivas
            )
            delete_last_column_from_file(get_file_path(file_path, file))
        elif file == FileName.creacion_de_goles_y_tiros:
            delete_duplicate_line_from_file(
                get_file_path(file_path, file), DeleteLines.creacion_de_goles_y_tiros
            )
            change_header_from_file(
                get_file_path(file_path, file), DeleteLines.creacion_de_goles_y_tiros
            )
            delete_last_column_from_file(get_file_path(file_path, file))
        elif file == FileName.estadisticas_diversas:
            delete_duplicate_line_from_file(
                get_file_path(file_path, file), DeleteLines.estadisticas_diversas
            )
            change_header_from_file(
                get_file_path(file_path, file), DeleteLines.estadisticas_diversas
            )
            delete_last_column_from_file(get_file_path(file_path, file))
        elif file == FileName.estadisticas_estandar:
            delete_duplicate_line_from_file(
                get_file_path(file_path, file), DeleteLines.estadisticas_estandar
            )
            delete_last_column_from_file(get_file_path(file_path, file))
        elif file == FileName.pases:
            delete_duplicate_line_from_file(
                get_file_path(file_path, file), DeleteLines.pases
            )
            change_header_from_file(get_file_path(file_path, file), DeleteLines.pases)
            delete_last_column_from_file(get_file_path(file_path, file))
        elif file == FileName.porteria_avanzada:
            delete_duplicate_line_from_file(
                get_file_path(file_path, file), DeleteLines.porteria_avanzada
            )
            change_header_from_file(
                get_file_path(file_path, file), DeleteLines.porteria_avanzada
            )
            delete_last_column_from_file(get_file_path(file_path, file))
        elif file == FileName.porteros:
            delete_duplicate_line_from_file(
                get_file_path(file_path, file), DeleteLines.porteros
            )
            change_header_from_file(
                get_file_path(file_path, file), DeleteLines.porteros
            )
            delete_last_column_from_file(get_file_path(file_path, file))
        elif file == FileName.posesion_del_balon:
            delete_duplicate_line_from_file(
                get_file_path(file_path, file), DeleteLines.posesion_del_balon
            )
            change_header_from_file(
                get_file_path(file_path, file), DeleteLines.posesion_del_balon
            )
            delete_last_column_from_file(get_file_path(file_path, file))
        elif file == FileName.tiempo_jugado:
            delete_duplicate_line_from_file(
                get_file_path(file_path, file), DeleteLines.tiempo_jugado
            )
            change_header_from_file(
                get_file_path(file_path, file), DeleteLines.tiempo_jugado
            )
            delete_last_column_from_file(get_file_path(file_path, file))
        elif file == FileName.tipos_de_pases:
            delete_duplicate_line_from_file(
                get_file_path(file_path, file), DeleteLines.tipos_de_pases
            )
            change_header_from_file(
                get_file_path(file_path, file), DeleteLines.tipos_de_pases
            )
            delete_last_column_from_file(get_file_path(file_path, file))
        elif file == FileName.tiros:
            delete_duplicate_line_from_file(
                get_file_path(file_path, file), DeleteLines.tiros
            )
            change_header_from_file(get_file_path(file_path, file), DeleteLines.tiros)
            delete_last_column_from_file(get_file_path(file_path, file))


def clean_all_data():
    """
    Delete duplicate lines, change the header and delete the last column
    of all the files of all the years.
    """
    transform_file(CleanData.files_17_18)
    transform_file(CleanData.files_18_19)
    transform_file(CleanData.files_19_20)
    transform_file(CleanData.files_20_21)
    transform_file(CleanData.files_21_22)
    transform_file(CleanData.files_22_23)


def union_transfermarket_file(file_path: str, output_name: str) -> None:
    """
    Union of all the files of all the years.
    """
    files = get_list_of_files(file_path)
    print(files)
    dataframes = []
    for file in files:
        dataframe = pd.read_csv(get_file_path(file_path, file))
        print(dataframe.shape, file)
        dataframes.append(dataframe)
    dataframe_concat = pd.concat(dataframes, ignore_index=True, sort=False)
    print(dataframe_concat.shape)
    dataframe_concat.to_csv(
        os.path.join(
            Directories.get_project_root(Directories) + file_path, output_name
        ),
        index=False,
    )


def merge_csv(fbref_file_path: str, tm_file_path, output_name: str) -> None:
    """
    Merge the csv files.

    Args:
        file_path (str): Path to the file with players stats from fbref.
        tm_file_path (str): Path to the file with players stats from transfermarkt.
        output_name (str): Name of the output file.
    """

    df_union = pd.merge(
        pd.read_csv(fbref_file_path),
        pd.read_csv(tm_file_path),
        left_on="Jugador",
        right_on="name",
        how="inner",
        validate="one_to_one",
    )
    df_union.to_csv(
        Directories.get_project_root(Directories) + output_name,
        index=False,
    )
