"""Main module for the TFG project."""

from src.utils.utils import get_file_path
from src.config import TransfermarketFiles, TransfermarktData, ProcessedData
import pandas as pd
from src.core.controller import process_transfermaket_fbref


def main():
    """
    Main function for the project
    """
    process_transfermaket_fbref()

    # transfermarket_df = pd.read_csv(
    #     get_file_path(ProcessedData.replace_strings, "transfermarter_2022.csv")
    # )

    # # Create a boolean mask for duplicated rows
    # duplicated_mask = transfermarket_df.duplicated(subset=["Name"], keep=False)

    # # Use the mask to filter the DataFrame
    # duplicated_data = transfermarket_df[duplicated_mask]
    # duplicated_data["Name"].to_csv("nombres.csv", index=False)

    # # Print the duplicated data
    # print(duplicated_data)


if __name__ == "__main__":
    main()
