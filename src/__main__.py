"""Main module for the TFG project."""
from src.utils import utils
from src.config import TransfermarktData, TransfermarketFiles
from src.core import controller


def main():
    """
    Main function for the project
    """
    controller.process_transfermarket_data()


if __name__ == "__main__":
    main()
