import os 
import zipfile as ZipFile
import pandas as pd 
from zipfile import ZipFile
  
workshop_home = os.environ.get("workshop")


# specifying the zip file name
file_name = os.path.join(workshop_home,"retail_data.zip")
  
# opening the zip file in READ mode
# with ZipFile(file_name, 'r') as zip:
 