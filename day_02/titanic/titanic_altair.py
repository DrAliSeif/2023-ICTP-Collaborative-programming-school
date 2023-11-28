import pandas as pd
import altair as alt

# bring in data 
titanic = pd.read_csv("../data/titanic.csv", index_col=False)
titanic.loc[:,"Survived"].replace([0,1],["No","Yes"], inplace=True)
print(titanic.columns)

# explore one variable - age individ spread
age_strip = alt.Chart(titanic).mark_tick().encode(
    alt.X("Age:Q"),  
).properties(width=600)

# histogram - age agg
age_histo = alt.Chart(titanic).mark_bar().encode(
    alt.X("Age:Q", bin=True),
    alt.Y("count()"),
    alt.Tooltip("Age", aggregate="count")
).properties(width=600)

# explore 2 variables - age and surivorship 
age_survive = alt.Chart(titanic).mark_bar().encode(
    alt.X("Age:Q").bin(),
    alt.Y("count()",stack=True),
    alt.Tooltip("Age", aggregate="count"),
    alt.Color("Survived:N", legend=alt.Legend(title="Survived?")),
)
age_survive.save("altair-view.html")

# explore 3 variables - age, survivorship, class 
age_survive_class = alt.Chart(titanic).mark_bar().encode(
    alt.X("Age:Q", bin=True),
    alt.Y("count()"),
    alt.Color("Survived:N", legend=alt.Legend(title="Survived?")),
    column="Pclass"
)

#alt.vconcat(age_strip, age_histo, age_survive, age_survive_class).save("altair-view.html")