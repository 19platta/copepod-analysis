"""
Process and clean dataframe data.
"""

import pandas as pd


def split_column(df, sep, col, names, n=0, drop=True, reset_index=False):
    """
    Splits a column in a dataframe into multiple columns

    Args:
        df: the dataframe containing the column to split
        sep: a string containing the delimiter to separate around
        col: a string containing the name of the column to split
        names: a list containing the names of the columns to create
        n: integer representing number of splits to return. Defaults to 0,
            which will return all splits
        drop: boolean indicating the original column should be kept after
            splitting. Defaults to True, so column will be dropped. Can be
            set to False to retain original column
        reset_index: boolean indicating whether the index of the returned
            dataframe should be reset. Defaults to False. Set to True if
            the input dataframe has been filtered and the index does not
            begin at 0 and continue sequentially.

    Returns:
        a new dataframe with the given column split into the columns given in
        names

    """
    if reset_index is True:
        df = df.reset_index(drop=True)
    # Split the given column on the given separator.
    split_data = df[col].str.split(sep, n=n)
    data = split_data.to_list()
    # Create a new dataframe of just the split data
    new_data = pd.DataFrame(data, columns=names)
    # Join the split dataframe to the full dataframe
    full_data = df.join(new_data)
    # If not changed from the default, eliminate the original column
    # since we just split it
    if drop is True:
        return full_data.drop(col, axis=1)
    # Otherwise, return the full original dataframe, plus the new columns
    return full_data


def quick_filter(df, col, criteria):
    """
    Filter a dataframe based on a column value.

    Example: calling quick_filter(names, "last_names", "Smith") will filter
    the dataframe names to all the rows where the column "last_names" is
    equal to "Smith"

    Args:
        df: the dataframe to filter
        col: a string containing the column to filter on
        criteria: the criteria to filter on

    Returns:
        a new dataframe, containing only the observations that match the given
            criteria
    """
    return df[df[col] == criteria]


def anti_filter(df, col, criteria):
    """
    Filter a dataframe based on an undesired column value.

    Example: calling quick_filter(names, "last_names", "Smith") will filter
    the dataframe names to all the rows where the column "last_names" is NOT
    equal to "Smith"

    Args:
        df: the dataframe to filter
        col: a string containing the column to filter on
        criteria: the criteria to filter on

    Returns:
        a new dataframe, containing only the observations that match the given
            criteria
    """
    return df[df[col] != criteria]
