import os
folder_path=r"C:\Users\User\Desktop\python BI Rabindra sir\python"
file_names=os.listdir(folder_path)
for file_name in file_names:
    print(file_name)

new_folder=r'C:\Users\User\Desktop\python BI Rabindra sir\python\my_new_folder'
# os.mkdir(new_folder)

old_folder_name=r'C:\Users\User\Desktop\python BI Rabindra sir\python\my_new_folder'
new_folder_name=r'C:\Users\User\Desktop\python BI Rabindra sir\python\my_new_folder_renamed'
os.rename(old_folder_name, new_folder_name)

remove_folder=r'C:\Users\User\Desktop\python BI Rabindra sir\python\my_new_folder_renamed'
os.rmdir(remove_folder)