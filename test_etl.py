import pandas as pd
from datetime import datetime

dfInput = pd.read_csv('sample_products.csv')
dfOutput = pd.read_csv("/app/output/clean_products.csv")

with open('/app/output/test_result.txt', 'a') as f:
    f.write(datetime.now().strftime("%d-%m-%y %H:%M:%S") + "\n")
    
    # case 1: Check if the output file exists
    if dfOutput.dtypes['unit_price'] == 'int64':
        f.write("Test Case 1: Pass.\n")
    else:
        f.write("Test Case 1: Failed\n")
