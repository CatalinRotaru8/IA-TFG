"""Main module for the TFG project."""
from src.utils.utils import (
    get_file_path,
    delete_duplicate_line_from_file,
    change_header_from_file,
    delete_last_column_from_file,
    clean_all_data,
    transform_file,
)
from src.config import CleanData, DeleteLines, FileName
import pandas as pd
from src.utils.fbref import Fbref
from src.utils.downloader import get_big5_data


def main():
    """
    Main function for the project
    """
    # get_big5_data(Fbref.stats_dict)

    clean_all_data()


if __name__ == "__main__":
    main()
