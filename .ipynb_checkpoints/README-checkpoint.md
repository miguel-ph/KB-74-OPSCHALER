# KB-74-OPSCHALER
This repository contains code for the KB-74-OPSCHALER project. KB-74 stands for the minor Applied Data Science at The Hague University of Applied Sciences, with Opschaler being the project name. The goal of this project is to predict the energy usage of houses, 1 week ahead with a 10 second resolution. More information about Opschaler can be found at their [website](http://www.opschaler.nl/). 

# Setting up GitHub on JupyterHub
1. Login to JupyterHub on the datascience server. 
2. In the top right press 'New -> Terminal'. A SSH terminal should pop up in a new window. 
3. Next follow this tutorial: [link](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent). 
4. When you have done this you will need to add the SSH key to your GitHub account: [link](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account). Notice that step 1 will not work because 'clip' is not recognized! Work around this by using FileZilla to browse to your `~/.ssh/id_rsa.pub` and download the file. Where `~` is your home folder. Then open the file with a texteditor, copy the contents and go on with the tutorial.
5. Test your connection: [link](https://help.github.com/articles/testing-your-ssh-connection/)
6. You are ready to clone repositories.

## Basic SSH commands
* `ls` Lists directory contents
* `cd directory_name' Moves up to directory_name
* `cd ..` Moves down a directory
* `cp` Copies a file or directory to directory
* Press tab to finish a word automatically.  
Note that `~` represents your home folder. 
More info on Linux commands: [link](https://1.bp.blogspot.com/-Y9rBRKuT0wA/VrJ7xwjdVjI/AAAAAAAAh2k/sdrCyf7nLbo/s1600/linux-reference-bg-invert-1.png)


## Cloning the KB-74-OPSCHALER repository
1. Once GitHub has been setup correctly you can clone this reposotiry by pressing the green `Clone or download` button, copy the (link](https://github.com/deKeijzer/KB-74-OPSCHALER.git). 
2. In the jupyter terminal window you should see the line `studentnumber@datascience:~$`. Move to the 'notebooks' folder by typing `cd notebooks`. The directory you are in now should be `~/notebooks`. 
3. While in here type `git clone <the link you copied, from this repository>`. 
4. Once this is done, move to the 'KB-74-OPSCHALER' folder by typing `cd KB-74-OPSCHALER`. 5. Once in here type `git status`. This will give you additional information and show you that you have cloned successfully. 

## Git push & pull
Before you start working on code in jupyter, be sure that you have the latest version of this repository. Do this by typing `git pull`. Once you have written certain parts of code and want to upload it to this repository do this as follows.
* `git add .` (this will select all files)
* `git commit -m 'commit message. For examples changes that you made to the code.'`
* `git push`
More push & pull information can be found in [this notebook](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/GitHub%20push%20%26%20pull%20tutorial.ipynb).

# Important data locations
Below is a list of the most important data locations for the Opschaler project. <b>Make sure to not modify or add any files in the folders listed below.</b> Some notebooks have been programmed in such a way that they expect all files in a folder to have a certain file structure. For example: in the `smartmeter_data folder` the only files in there should be smartmeter files in the format `dwelling_id.csv`. Any other file in there will crash the notebook which uses this folder to process the files.  
* Only read files, do not write to them.
* Use the [Processed dwelling_id dataframes](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/README.md#processed-dwelling_id-dataframes) files for EDA.


## KNMI
The KNMI data consists of two dataframes. One is the raw format, this is the way KNMI has provided the data. The other dataset is the processed one, this has been cleaned/prepared/processed in such a way that it can be used for EDA.

### KNMI Raw data
Location: `/datc/opschaler/weather_data/knmi_10_min_raw_data`  
This is the raw 10 minute interval data from 2015 till 2018 as provided by the KNMI (by mail).

### KNMI preprocessed dataframe
Location: `//datc//opschaler//weather_data//weather.csv`  
The KNMI dataframe (1,82 GB) contains weather data from 2015 to 2018, with a 10 minute resolution.
More information can be found in [this notebook](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/KNMI/2.KNMI_high_resolution_cleaning_df.ipynb).  
Reading in the data is done as follows:  
* `weather = pd.read_csv('//datc//opschaler//weather_data//weather.csv', delimiter='\t', comment='#', parse_dates=['datetime'])`   
* `weather = weather.set_index(['datetime'])`  
* `weather.head()`  

## Smartmeter data (from the TU Delft server)
This is the smartmeter data as downloaded from the TU Delft server.  

### Raw smartmeter data (from the TU Delft server)
Location: `/datc/opschaler/smartmeter_data`  
These are the raw smartmeter dataframes from the TU Delft server.  
They should be in the format `export_dwelling_id.csv`.  
These files contain the raw electricity and raw gas data.  

## preprocessed dwelling_id dataframes
Location: `//datc//opschaler//combined_gas_smart_weather_dfs//unprocessed`  
The smartmeter, gasmeter and weather dataframes merged into one dataframe.  
`_hour` has a one hour sample rate, `_10s` has a 10 second sample rate.  
NaNs are not removed, the following has been done (in order):  
For `_hour` files:  
* 1. gasPower calculated by using `.diff()` on gas column.  
* 2. smartmeter and weather data downsampled to 1 hour, using mean.  
* 3. merged smartmeter, gas and weather data.  
  
For `_10s` files:  
* 1. gas has been upsampled to 10s by using forward fill (`.ffill()`)  
* 2. gasPower calculated by using `.diff()` on gas column.  
* 3. weather upsampled to 10s by using forward fill  
* 4. merged smartmeter, gas and weather data  

### Processed dwelling_id dataframes (Use these for analysis)
Location: `/datc/opschaler/combined_gas_smart_weather_dfs/processed`  
The smartmeter, gasmeter and weather dataframes merged into one dataframe.
Rows containing a NaN streak which is higher than accepted have been dropped.
NaNs in the weather data have been forward filled.
NaNs in `'eMeter', 'eMeterReturn', 'eMeterLowReturn', 'gasMeter'` have been interpolated.
ePower, ePowerReturn and gasPower might still contain NaNs, drop these after reading in the files (if required).
More information can be found [here](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/loading_combining_smart_gas_weather_generalized.ipynb)  
* `dir = '//datc//opschaler//combined_gas_smart_weather_dfs//processed//'`
* `dwelling_id = 'P01S01W0373'` (for example)
* `df = pd.read_csv(dir+dwelling_id+'.csv', delimiter='\t', parse_dates=['datetime'])`
* `df = df.set_index(['datetime'])`

## NaN Information of not-processed dataframes
Location: `/datc/opschaler/nan_information`  
This folder contains `dwelling_id_threshold_percentage.csv` files together with corresponding plots to get indepth knowledge about the NaNs in all used data.
The notebook in which `dwelling_id_threshold_percentage.csv` is created can be found [here](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/df_NaN_checker.ipynb).

# EDA results locations
location: `//datc//opschaler//EDA//`
The EDA results, saved per dwelling.  
For example, correlation coefficient matrices are saved in `//datc//opschaler//EDA//correlation_matrices`  
