# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("data.csv")

# sorting by first name
data.sort_values("Mobile Number", inplace=False)

# dropping ALL duplicte values
data.drop_duplicates(subset="Mobile Number",
                   keep='first', inplace=True)

# displaying data
print(data)
