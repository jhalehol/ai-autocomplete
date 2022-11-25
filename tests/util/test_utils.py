import json
import os


def load_json_data(file_name: str):
    """Loads the json content of the given file

    Args:
        file_name (str): File name located in /data folder from tests
    """
    json_content = None
    file_path = build_resource_absolute_path(file_name)
    with open(file_path) as scores_file:
        json_content = json.load(scores_file)

    return json_content


def build_resource_absolute_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), '../data/' + file_name)
