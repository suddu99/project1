# import pandas library
import pandas as pd

# load data
df1 = pd.read_csv("data.csv")

# drop rows which have same order_id
# and customer_id and keep latest entry
newdf = df1.drop_duplicates( subset = ['Mobile Number','Service Indication'], keep="first")

#copy data to other file
newdf.to_csv("data1.csv",index=False)
