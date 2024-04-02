# import pandas as pd 
# # df=pd.read_csv('data.csv')
# # print(df.to_string())
# # print(df)

# pd.options.display.max_rows=9999
# df=pd.read_csv('data.csv')
# print(df)

# import pandas as pd
# df=pd.read_csv('example.csv',usecols=['Name', 'Age','Salary'])
# print(df)

import pandas as pd 
df = pd.read_json('data.js', orient='records')
print(df.to_string())

