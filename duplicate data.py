# removing duplicate value 1st u need to discover the duplicate value via duplicate() methord
import pandas as pd
a=pd.read_csv("empty.csv")
print(a.to_string())



# check empty set
import pandas as pd
a=pd.read_csv("empty.csv")
print(a.duplicated())

# remove duplicate value
import pandas as pd
a=pd.read_csv("empty.csv")
a.drop_duplicates(inplace=True)
print(a.to_string)

