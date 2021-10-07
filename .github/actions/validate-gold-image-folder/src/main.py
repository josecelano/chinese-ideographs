import os
import json

from validation.validate_filepaths import validate_filepaths


def parse_dvd_diff_ouput(dvd_diff):
    # It gets a plain string list with the added or modified files from the diff json.
    # Input: {"added": [{"path": "data/000001/32/000001-32.600.2.tif"}], "deleted": [], "modified": [], "renamed": []}
    # Ouput: ['data/000001/32/000001-32.600.2.tif']
    # Code Review: parse_dvd_diff_ouput function should be moved to an independant action or dvc-diff action.

    # parse json
    data = json.loads(dvd_diff)

    # only interesting in added or modified files
    filenames = data['added'] + data['modified']

    # parse path from all items
    filenames = [path_object['path'] for path_object in filenames]

    # parse basename
    filenames = [os.path.basename(filename) for filename in filenames]

    return filenames


def main():
    dvd_diff = os.environ["INPUT_FILEPATHS"]

    filenames = parse_dvd_diff_ouput(dvd_diff)

    validate_filepaths(filenames)


if __name__ == "__main__":
    main()
