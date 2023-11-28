import pandas as pd

# pandas objects: Series and Dataframes 
s = pd.Series([1,3,5,7,11])

df = pd.DataFrame({
    "city": ["Bergen", "Oslo", "Trondheim"],
    "temp": [12.0, 11.0, 10.4]
})

# loc and iloc
df.loc[df["city"] == "Bergen"]
df.iloc[0,:]

############################################
# read in data 
titanic = pd.read_csv("../data/titanic.csv")

# explore data
print(titanic.shape)
titanic.info()
titanic.describe()

print(titanic.head())
titanic.iloc[:5,:]  # same as .head()

titanic.tail()
titanic.iloc[-5:,:] # same as .tail()


