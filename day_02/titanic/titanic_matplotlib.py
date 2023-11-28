import pandas as pd
import matplotlib.pyplot as plt

# get data 
titanic = pd.read_csv("../data/titanic.csv")
# titanic.head(), titanic.info(), titanic.describe()
# clarify survived col semantics
titanic.loc[:, "Survived"].replace([0,1],["No", "Yes"], inplace=True) 

# 1D age dist - hist
fig, ax_hist = plt.subplots()
ax_hist.hist(titanic["Age"], edgecolor="white", bins=8)


# 1D age distribution - strip plot 
fig, ax_age = plt.subplots()

ax_age.eventplot(titanic["Age"])
ax_age.set_xlim(0,81)
ax_age.set_ylim(0.5,1)
ax_age.yaxis.set_ticklabels([])
plt.show()

# resculpt my data 
titanic_sub = titanic.loc[:,["Age", "Survived", "Pclass"]]
titanic_sub["Age bins"] = pd.cut(titanic_sub["Age"], range(0,81,10))  # .cut() to segment and sort data values into bins

s_cnts = titanic_sub.groupby(["Age bins","Survived","Pclass"]
                             ).size().unstack(level=1).reset_index()
s_cnts["Net survived"] = s_cnts["Yes"] - s_cnts["No"]

# 2d age and survivorship - pandas plot style 
s_cnts_allclasses = titanic_sub.groupby(["Age bins","Survived"])["Pclass"].size().unstack(level=1).reset_index()
print(s_cnts_allclasses)

s_cnts_allclasses.plot(
    kind="bar",
    color=["salmon", "steelblue"]
    )


# 2d age, survivorship, class - pandas plot using pivot for finer-grained control of shaping 
s_cnts_indiv_class = s_cnts.loc[:,["Age bins", "Pclass", "Net survived"]]
s_cnts_indiv_class_g = s_cnts_indiv_class.pivot(index="Age bins", columns="Pclass", values="Net survived").reset_index()
print(s_cnts_indiv_class_g)

s_cnts_indiv_class_g.plot(
    kind="bar",
    )
plt.show()

