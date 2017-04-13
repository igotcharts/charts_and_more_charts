def folder_setup():
    current_dir = os.getcwd()
    os.chdir('..')
    base_path = os.getcwd()
    data_folder = (os.path.join(base_path,'data'))
    output_folder = (os.path.join(base_path,'outputs'))
    return base_path, data_folder,output_folder
