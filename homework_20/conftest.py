import json
import os
import pytest
from homework_20.data_model import DataModel
# Change the current working directory to the directory containing the script
os.chdir(os.path.dirname(__file__))


def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found. Current directory: {os.getcwd()}")
    except json.JSONDecodeError:
        raise ValueError(f"Error decoding JSON in file '{filename}'.")


@pytest.fixture
def test_data():
    test_data = read_json_file(os.path.join('moke_data.json'))
    yield DataModel(test_data)
