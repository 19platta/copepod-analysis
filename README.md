# Analysis of Copepod Effects on Right Whale Distribution

A repository for Software Design Project 2. 

## Background:

In this project, I investigate what effect the changing distribution of the zooplankton species Calanus finmarchicus, the primary food source for North Atlantic Right Whales, has on sightings of North Atlantic Right Whales. I also look at whether C. finmarchicus distribution has been changing over time, and if this lines up with a shift in whale locations. This is important because if C. finmarchicus is moving, and right whales are moving along with it, the environmental implications are many and serious. 

## Setup

I used the Anaconda Python distribution for this project. It can be downloaded at the bottom of [this page](https://www.anaconda.com/products/individual). You will need to choose your install based on your operating system. Installation guides for Windows, Linux, and MacOS can be found [here](https://docs.anaconda.com/anaconda/install/). 

If you prefer not to use Anaconda, the packages used are listed below:   

`plotly`  
`pandas`

There is one library used for reading Darwin Core Archive (DwC-A) data files that is not included in Anaconda. It can be downloaded with the command `pip install python-dwca-reader`. Documentation for the package can be found [here](https://python-dwca-reader.readthedocs.io/en/latest/). 

I used Pytest to create unit tests for the data processing functions. To install, run the command `pip install -U pytest`. For more help and getting started, visit [this page](https://docs.pytest.org/en/stable/getting-started.html).  

## Structure

This project contains the following files: 

data/: a directory where the data is written to and stored. Not tracked by Github, nor is the data due to licensing.      
    whale_data: where the whale data is extracted to      
        eml.xml    
        meta.xml    
        occurrence.txt: this is the main file containing the actual data   
    copepod_data.csv: where the copepod data is written to  
    whale_df.csv: where the whale data gets written to after being extracted  
data_fetch_functions.py: the functions used to retrieve online data  
effects_of_c_finmarchicus.py: The Jupyter notebook containing a computational essay walking through the project   
process_data.py: the functions used for filtering and splitting dataframes  
retrieve_data.py: script that scrapes the necessary websites and downloads the data to .csv files  
test_process_data.py: pytest file that tests the functions in process_data.py  
visualizations.py: file containing functions helpful for creating visualizations


## Usage

Before beginning the Jupyter notebook walkthrough, you will need to run the script `retrieve_data.py` to download and extract the necessary data in the correct format. It may take 20-ish minutes or more to run, as the copepod dataset is very large. You only need to run this script once, as it will create the .csv files in the folder `data/`.

Once the script has been run, simply open the Jupyter notebook and follow along.   

## Tests

Tests are available for the functions found in `process_data.py`. They can be run by running the file `test_process_data.py` as a Pytest on `process_data.py`. 

## Citations

Cole, T. and C. Khan. 2016. NEFSC Right Whale Aerial Survey. Data downloaded from OBIS-SEAMAP (http://seamap.env.duke.edu/dataset/513) on 2020-10-24.

Duke University. "Lull in ship noise after Sept. 11 attacks eased stress on right whales." ScienceDaily. ScienceDaily, 8 February 2012. <www.sciencedaily.com/releases/2012/02/120208132711.htm>.

Lenz, Petra H et al. “Functional genomics resources for the North Atlantic copepod, Calanus finmarchicus: EST database and physiological microarray.” Comparative biochemistry and physiology. Part D, Genomics & proteomics vol. 7,2 (2012): 110-23. doi:10.1016/j.cbd.2011.12.001

## Links

[NOAA's COPEPOD database](https://www.st.nmfs.noaa.gov/copepod/atlas/index-atlas.html)
