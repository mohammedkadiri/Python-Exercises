import os
from datetime import datetime

# print(dir(os))  Displays all the functions inside a module

# print(os.getcwd())

# mod_time = os.stat('hi.txt').st_mtime
#
# print(datetime.fromtimestamp(mod_time))

# print(os.listdir())

os.chdir('C:/Users/Mo')
print(os.getcwd())

# for dirpath, dirnames, filenames in os.walk('C:/Users/Mo/Documents'):
#     print('Current Path: ', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)
#     print()
