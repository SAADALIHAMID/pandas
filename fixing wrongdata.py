                                                   #  wrong data
# import pandas as pd
# a=pd.read_csv('empty.csv')
# print(a.to_string())
# here we will set duration 

# a=pd.read_csv('empty.csv')

# a.loc[20,"Duration"]=60
# print(a.to_string)
 
                                                 #  we use loop for large data
import pandas as pd
a=pd.read_csv('empty.csv')
for i in a.index:
    if a.loc[i,"Duration"]>120:
        a.loc[i,"Duration"]=120
print(a.to_string())        

                                                 #  we can remove a row for wrong data
import pandas as pd
a=pd.read_csv('empty.csv')
for i in a.index:
    if a.loc[i,"Duration"]>120:
        a.drop(i,inplace=True)
print(a.to_string()) 