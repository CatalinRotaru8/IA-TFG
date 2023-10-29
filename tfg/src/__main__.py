"""Main module for the TFG project."""
from src.utils.fbref import Fbref
from src.utils.downloader import get_big5_data
from src.utils.utils import (
    get_file_path,
    delete_duplicate_line_from_file,
    string_to_list,
    change_header_from_file,
    delete_last_column_from_file,
    transform_file,
    clean_all_data,
)
from src.config import OriginalData, CleanData, DeleteLines, FileName
import pandas as pd


def main():
    """
    Main function for the project
    """
    # get_big5_data(Fbref.stats_dict)
    # archivo = get_file_path(CleanData.files_17_18, FileName.acciones_defensivas)
    # dataframe = pd.read_csv(archivo, encoding="utf-8")
    # print(dataframe.shape)

    # change_header_from_file(
    #     get_file_path(CleanData.files_17_18, FileName.porteria_avanzada),
    #     DeleteLines.porteria_avanzada,
    # )
    # delete_duplicate_line_from_file(
    #     get_file_path(CleanData.files_17_18, FileName.porteria_avanzada),
    #     DeleteLines.porteria_avanzada,
    # )
    # delete_last_column_from_file(
    #     get_file_path(CleanData.files_17_18, FileName.porteria_avanzada)
    # )

    # transform_file(CleanData.files_17_18)
    clean_all_data()


if __name__ == "__main__":
    main()
