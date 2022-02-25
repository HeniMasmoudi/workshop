import os 
import zipfile as ZipFile
import pandas as pd 


from zipfile import ZipFile
  
# specifying the zip file name
file_name = "my_python_files.zip"
  
# opening the zip file in READ mode
# with ZipFile(file_name, 'r') as zip:
    
d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   

print(d)