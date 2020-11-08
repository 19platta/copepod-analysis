"""
Retrieve data from online and write to files.
"""

import requests
import io
import zipfile
from dwca.read import DwCAReader as dwcareader


def get_zipped_data(url, path):
    """
    Downloads and extracts a zipped data file from the given url to the given
    path

    Args:
        url: a string containing a url to a zipped file
        path: a string containing the path where the data should be extracted
            to. If no directory with that name currently exists, one will
            be created.
    Returns:
        None
    """
    # Request the content from the page, but defer downloading it until
    # it is accessed. Disable the SSL certificate verification
    r = requests.get(url, stream=True, verify=False)
    # Open the zipped file as a stream of bytes. This is why we delayed
    # downloading the file content until it is accessed.
    zipped_file = zipfile.ZipFile(io.BytesIO(r.content))
    # Extract the files to the given path
    zipped_file.extractall(path)


def read_dwca_data(path_to_data, csv_path):
    """
    Reads the occurrence file from a DwCA file into a Pandas dataframe
    and writes the dataframe to a .csv file at the specified path.

    DwCA files contain three files: a .txt file, a meta.xml file, and an
    eml.xml file. The .txt file contains the data to read to the dataframe.
    This function is specifically for reading from an occurrence dataset,
    which documents observed occurrences (for instance, occurrences of a
    species sighting), so we know the .txt file will be named "occurrence.txt."

    Args:
        path_to_data: a string containing the path to the data to be read
        csv_path: a string containing the path to write the .csv to

    Returns:
        None

    """
    with dwcareader(path_to_data) as dwca:
        core_df = dwca.pd_read('occurrence.txt', parse_dates=True)
    core_df.to_csv(csv_path)


def get_data(url, path):
    """
    Gets file from the given url and writes it to a file at the given path.

    CAUTION: If the file on the given path already exists, it will be
    overwritten.

    Args:
        url: a string containing the url where the file is located
        path: a string containing the path the data should be written to

    Returns:
        None

    """
    data = requests.get(url)
    with open(path, "w") as f:
        f.write(data.text)
