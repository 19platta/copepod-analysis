"""
Test that the data processing functions are working properly
"""

import pytest
import process_data
import pandas as pd

# First test the split function
df = pd.DataFrame({'Name': ['John_Smith', 'Amanda_Brown', 'Bernadette_Banner'],
                  'Age': [32, 34, 36]})
df_expected = pd.DataFrame({'Age': [32, 34, 36],
                            'First_Name': ['John', 'Amanda', 'Bernadette'],
                            'Last_Name': ['Smith', 'Brown', 'Banner'],
                            })
df_no_drop = pd.DataFrame({"Name": ["John_Smith", "Amanda_Brown",
                                    "Bernadette_Banner"],
                           "Age": [32, 34, 36],
                           "First_Name": ["John", "Amanda", "Bernadette"],
                           "Last_Name": ["Smith", "Brown", "Banner"]})
df_reset = df.set_index([pd.Index([1, 2, 3])])

# Define this outside the test cases so we don't need to type it every time
names = ["First_Name", "Last_Name"]

test_cases_split = [
    # Test a simple dataframe column split
    (df, "_", "Name", names, True, False, df_expected),
    # Test to make sure retaining the initial column works
    (df, "_", "Name", names, False, False, df_no_drop),
    # Test to make sure resetting the index works
    (df_reset, "_", "Name", names, True, True, df_expected),
]


@pytest.mark.parametrize("input_df, sep, col, names, drop, idx, df_out",
                         test_cases_split)
def test_frame_split(input_df, sep, col, names, drop, idx, df_out):
    split_frame = process_data.split_column(input_df, sep, col, names,
                                            drop=drop,
                                            reset_index=idx)
    pd.testing.assert_frame_equal(split_frame, df_out)

# Next test the filter function


df_filtered = pd.DataFrame({'Name': ['John_Smith'],
                            'Age': [32]})


test_cases_filter = [
    # Test that a simple filter works
    (df, "Name", "John_Smith", df_filtered),
    # Test that it doesn't break if there's nothing to filter
    (df, "Name", "Tiffany_Ferguson", df)
]


@pytest.mark.parametrize("input_df, col, filter_on, output",
                         test_cases_filter)
def test_quick_filter(input_df, col, filter_on, output):
    filtered_df = process_data.anti_filter(input_df, col, filter_on)
    pd.testing.assert_frame_equal(filtered_df, output)


# Now test the anti-filter function


anti_filtered = pd.DataFrame({"Name": ["John_Smith", "Amanda_Brown"],
                              "Age": [32, 34]})

test_cases_anti_filter = [
    # Test that a simple filter works
    (df, "Name", "Bernadette_Banner", anti_filtered),
    # Test that it doesn't break if there's nothing to filter
    (df, "Name", "Tiffany_Ferguson", df)
]


@pytest.mark.parametrize("input_df, col, filter_on, output",
                         test_cases_anti_filter)
def test_quick_filter(input_df, col, filter_on, output):
    filtered_df = process_data.anti_filter(input_df, col, filter_on)
    pd.testing.assert_frame_equal(filtered_df, output)
