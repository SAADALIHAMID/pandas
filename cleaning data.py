# import pandas as pd
# a=pd.read_csv('empty.csv')
# a["Date"] = pd.to_datetime(a['Date'], format='%Y%m%d')
# print(a.to_string())
# import pandas as pd

# try:
#     a = pd.read_csv('empty.csv')
#     # Assuming "Date" column is present in the CSV file
#     if "Date" in a.columns:
#         a["Date"] = pd.to_datetime(a["Date"], format='%Y%m%d')
#         print(a.to_string())
#     else:
#         print("Error: 'Date' column not found in the CSV file.")
# except FileNotFoundError:
#     print("Error: File 'empty.csv' not found.")
# except Exception as e:
#     print("An error occurred:", e)

# import pandas as pd

# try:
#     a = pd.read_csv('empty.csv')
    
#     # Assuming "Date" column is present in the CSV file
#     if "Date" in a.columns:
#         try:
#             # Try to convert to datetime, handle errors by printing a message
#             a["Date"] = pd.to_datetime(a["Date"], errors='coerce')
#             a.dropna(subset=['Date'], inplace = True)
#             print(a.to_string())
#         except Exception as e:
#             print("An error occurred during date conversion:", e)
#     else:
#         print("Error: 'Date' column not found in the CSV file.")
# except FileNotFoundError:
#     print("Error: File 'empty.csv' not found.")
# except Exception as e:
#     print("An error occurred:", e)
# import pandas as pd
# df=pd.read_csv('empty.csv')
# df['Date']=pd.to_datetime(df['Date']),
# format=('%Y%m%d,')
# print(df.to_string)

import pandas as pd

df = pd.read_csv('empty.csv')

# Assuming 'Date' column contains date strings in the format 'YYYYMMDD'
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')

print(df.to_string())
