import pandas as pd
#from IPython.display import VimeoVideo 
#VimeoVideo("656321516", h="e85e3bf248", width=600)
"""df1 = pd.read_csv("data/mexico-real-estate-1.csv")
df2 = pd.read_csv("data/mexico-real-estate-2.csv")
df3 = pd.read_csv("data/mexico-real-estate-3.csv")

# Print object type and shape for DataFrames
print("df1 type:", type(df1))
print("df1 shape:", df1.shape)
print()
print("df2 type:", type(df2))
print("df2 shape:", df2.shape)
print()
print("df3 type:", type(df3))
print("df3 shape:", df3.shape)"""

#Task 1.2.2: Inspect df1 by looking at its shape attribute. Then use the info method to see the data types and number of missing values for each column. Finally, use the head method to determine to look at the first five rows of your dataset.
# Print df1 shape
#df1.shape
# Print df1 info
#df1.info()
# Get output of df1 head
#df1.head(10)

#Task 1.2.3: Clean df1 by dropping rows with NaN values. Then remove the "$" and "," characters from "price_usd" and recast the values in the column as floats.
# Drop null values from df1
"""df1.dropna(inplace=True)
# Clean "price_usd" column in df1
df1["price_usd"] = (
    df1["price_usd"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "")
    .astype(float)
)

# Print object type, shape, and head
print("df1 type:", type(df1))
print("df1 shape:", df1.shape)
df1.head()
"""