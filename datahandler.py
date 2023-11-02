import json
from os import PathLike
from typing import Union
import sys


class OriginData:
    """
    Class that handles input data for the script, data will be loaded from a loader function
    """

    def __init__(self):
        # no interface needed, will be loaded through loaders
        self.country: str = ""
        self.city: str = ""
        self.currency: str = ""
        self.amount: float = 0

    def __repr__(self):
        return f"OriginData(country={self.country}, city={self.city}, currency={self.currency}, amount={self.amount})"

    def load_from_dict(self, data: dict) -> None:
        self.country = data["country"]
        self.city = data["city"]
        self.currency = data["currency"]
        self.amount = data["amount"]

    def transform_by_keys(self, *keys) -> dict:
        def nest_dict(remaining_data, key_sequence):
            if not key_sequence:
                # Exclude the keys used for nesting
                return [{k: v for k, v in self.__dict__.items() if k not in keys}]

            current_key = key_sequence[0]
            next_keys = key_sequence[1:]

            if current_key not in remaining_data:
                return {}

            # Recursive nesting
            return {
                remaining_data[current_key]: nest_dict(remaining_data, next_keys)
            }

        # Start the recursive nesting
        return nest_dict(self.__dict__, keys)


class DataHandler:
    def __init__(self):
        self.data: [OriginData] = []

    def from_json(self, json_data: list[dict]) -> None:
        """
        Loads data from json data structure (pythonized dict) and saves it into self.data
        Currently I am omitting data structure checking, typing got the needed file structure
        :return: None
        """
        for data_entry in json_data:
            origin_data = OriginData()
            origin_data.load_from_dict(data_entry)
            self.data.append(origin_data)

    def load_from_json(self, json_path: Union[PathLike, str]) -> None:
        """
        Loads data from JSON file and saves it into self.data
        Currently I am omitting data structure checking
        :param json_path: Path to a JSON file
        :return: None
        """
        with open(json_path) as f:
            loaded_data = json.load(f)

        for data_entry in loaded_data:
            origin_data = OriginData()
            origin_data.load_from_dict(data_entry)
            self.data.append(origin_data)

    def load_from_stdin(self):
        """
        Loads data from JSON file and saves it into self.data
        Currently I am omitting data structure checking
        :param json_path: Path to a JSON file
        :return: None
        """
        loaded_data = json.load(sys.stdin)
        for data_entry in loaded_data:
            origin_data = OriginData()
            origin_data.load_from_dict(data_entry)
            self.data.append(origin_data)

    def aggregate_by_keys(self, keys):
        def merge(a, b):
            """ Merge two structures """
            if isinstance(a, dict) and isinstance(b, dict):
                return {k: merge(a.get(k), b.get(k)) for k in set(a) | set(b)}
            elif isinstance(a, list) and isinstance(b, list):
                return a + b
            else:
                return a if b is None else b

        transformed_data = []
        for d in self.data:
            transformed_data.append(d.transform_by_keys(*keys))

        result = {}
        for item in transformed_data:
            for key, value in item.items():
                result[key] = merge(result.get(key), value)
        print(result)
        return result

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        return iter(self.data)


if __name__ == "__main__":
    dh = DataHandler()
    dh.load_from_json("input_data.json")
    dh.aggregate_by_keys(("currency", "country", "city"))
