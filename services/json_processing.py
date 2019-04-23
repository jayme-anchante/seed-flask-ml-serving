# core
import json
# external
import pandas as pd
from pandas.io.json import json_normalize


class ProcessJson:
    def __init__(self):
        """Simple columns are non-nested values, compound columns are nested dictionaries"""
        self.nonnested_columns = [""]
        self.nested_columns = [""]
        self.id = ""
        pass

    def read_json(self, payload):
        """Read the JSON payload from the API"""
        print("Reading JSON")
#         json_file = json.loads(open(file=payload, mode="r", encoding="utf-8").read())
        json_file = json.loads(payload)
        return json_file

    def read_nonnested_columns(self, json_file):
        """Read the nonested (aka root) columns from the JSON"""
        print("Converting nonnested columns")
        df = pd.DataFrame(json_file).loc[:, self.nonnested_columns]
        return df

    def read_nested_columns(self, json_file, nested_column):
        """Read the nested columns from the JSON"""
        print("Converting nested columns")
        normalized_df = json_normalize(data=json_file, record_path=nested_column, meta=self.id)
        return normalized_df

    def process_json(self, payload):
        """Run all ProcessJson functions"""
        print("\n\nBegin: preprocessing JSON\n")
        df_dict = {}
        json_file = self.read_json(payload=payload)
        nonnested_df = self.read_nonnested_columns(json_file=json_file)
        for column in self.nonnested_columns:
            df_dict[column] = nonnested_df.loc[:, [self.id, column]]
        for column in self.nested_columns:
            df_dict[column] = self.read_nested_columns(json_file=json_file, nested_column=column).loc[:, [self.id, column]]
        print("\nEnd:   preprocessing JSON\n\n")
        return df_dict
