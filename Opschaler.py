
# coding: utf-8

# In[1]:

import numpy as np
import glob
import pandas as pd
from tqdm import tqdm


# In[2]:

def dwel_path_id(sample_rate, folder, combined):
    """
    Reads in the file paths and dwelling id's of the combined smartmeter data.
    :return: file_paths, dwelling_ids, both as lists.
    """
    path = '//datc//opschaler//combined_gas_smart_weather_dfs//'
    map_ = 'processed//'
    subscript = '_hour'
    combined_ = 'P*'

    if sample_rate == '10s':
        subscript = '_10s'
    if folder == 'unprocessed':
        map_ = 'unprocessed//'
    if combined == 'yes':
        combined_ = 'all_dwellings_combined'
        
    complete_path = path+map_+combined_+subscript+".csv"
    file_paths = np.array(glob.glob(complete_path))

    print('complete_path: '+complete_path)
    print('Detected %s smartmeter_data files.' % len(file_paths))
    
    dwelling_ids = np.array(list((map(lambda x: x[-20:-9], file_paths)))) 
    
    if sample_rate == '10s':
        dwelling_ids = np.array(list((map(lambda x: x[-19:-8], file_paths)))) # 10s ids slicing
    if combined == 'yes':
        dwelling_ids = 'Used all dwellings to make this df'
    
    
    return file_paths, dwelling_ids










def dwel_len(type_, dwelling_id):
    """
    Get the total amount of days of the unprocessed dwelling_id where type=10s/h.
    """
    dir = '//datc//opschaler//combined_gas_smart_weather_dfs//unprocessed//'
    df = pd.read_csv(dir+dwelling_id+'_'+type_+'.csv', delimiter='\t', parse_dates=['datetime'])
    columns = df.columns
    df = df['datetime'] # only keep the datetime column
    start_date = df.iloc[0]
    stop_date = df.iloc[-1]
    
    del df # Free up memory
    
    recorded_days = (stop_date - start_date).days # total amount of recorded days

    return recorded_days, start_date, stop_date, columns









#def read_in

#def read_in_10s

#def read_in_h



# In[ ]:



