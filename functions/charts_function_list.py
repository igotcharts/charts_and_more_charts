import os

def folder_setup():
    current_dir = os.getcwd()
    os.chdir('..')
    base_path = os.getcwd()
    data_folder = (os.path.join(base_path,'data'))
    output_folder = (os.path.join(base_path,'outputs'))
    return base_path, data_folder,output_folder

def numeric_code(df,column,first_number=1):
    d = {x:i for i,x in enumerate(df[column].unique())}
    return df[column].map(d)+first_number
