"""
Fetch the copepod and whale data from the internet. This script only needs
to be run once.
"""

import data_fetch_functions as dat_func

# Get the aerial survey data as a DwC-A (Darwin Core Archive) file
dat_func.get_zipped_data("http://ipt.env.duke.edu/archive.do?r=zd_513&v=1.8",
                         "data/whale_data")

# Read the aerial survey data and write it to a .csv file
whale_data = dat_func.read_dwca_data("data/whale_data", "data/whale_df.csv")

# Get the copepod data and write it to a .csv file
dat_func.get_data(
    "https://www.st.nmfs.noaa.gov/copepod/atlas/data_src/\n"
    "copepod__4212000-compilation.txt",
    "data/copepod_data.csv")
