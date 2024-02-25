"""Main module for the TFG project."""

from src.utils.utils import get_file_path
from src.config import TransfermarketFiles, TransfermarktData, ProcessedData
from src.core.controller import process_transfermarket
import pandas as pd
from sklearn.preprocessing import LabelEncoder


def main():
    """
    Main function for the project
    """
    process_transfermarket()
    # transfermarkt_data = pd.read_csv(
    #     get_file_path(
    #         TransfermarktData.transfermarket, TransfermarketFiles.transfermarket
    #     )
    # )

    # columns = ["Position", "Transfer Type"]
    # label = LabelEncoder()
    # for column in columns:
    #     transfermarkt_data[column] = label.fit_transform(
    #         transfermarkt_data[column].astype(str)
    #     )

    # transfermarkt_data.to_csv(
    #     get_file_path(
    #         ProcessedData.replace_strings, TransfermarketFiles.transfermarket
    #     ),
    #     index=False,
    # )


if __name__ == "__main__":
    main()
