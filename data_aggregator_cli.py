import argparse
import json

from core.datahandler import DataHandler


def main():

    parser = argparse.ArgumentParser(description='Process and aggregate data based on given keys. Uses stdin (pipe) for input data')
    parser.add_argument('keys', nargs='+', type=str, help='Keys for aggregating the data (e.g., currency country city)')

    args = parser.parse_args()

    # if len(args.keys) == 0: not really needed, nargs `+` got it covered
    #     parser.error("At least one key is required for aggregation.")

    # Process the data
    data_handler = DataHandler()
    data_handler.load_from_stdin()

    # Aggregate data by keys
    aggregated_data = data_handler.aggregate_by_keys(args.keys)
    print(json.dumps(aggregated_data, indent=2))


if __name__ == "__main__":
    main()
