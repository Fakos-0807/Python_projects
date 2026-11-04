import pandas as pd
import matplotlib
import os
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("titanic.csv")

df.drop(["PassengerId", "Name", "Cabin", "Ticket"], axis = 1, inplace = True)
df["Embarked"].fillna("S", inplace = True)
df[list(pd.get_dummies(df["Embarked"]).columns)] = pd.get_dummies(df["Embarked"])
df.drop("Embarked", axis = 1, inplace= True)

age_1 = df[df["Pclass"] == 1]["Age"].median()
age_2 = df[df["Pclass"] == 2]["Age"].median()
age_3 = df[df["Pclass"] == 3]["Age"].median()


def fill_age(row):
    if pd.isnull(row["Age"]):
        if row["Pclass"] == 1:
            return age_1
        elif row["Pclass"] == 2:
            return age_2
        else:
            return age_3
    else:
        return row["Age"]

df["Age"] = df.apply(fill_age, axis=1)

def fill_gender(row):
    if row["Gender"] == "male":
        return 1
    else:
        return 0 

df["Gender"] = df.apply(fill_gender, axis=1)

x = df.drop("Survived", axis = 1)
y = df["Survived"]
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x,y)

new_passenger = pd.DataFrame([{
    "Pclass":1,
    "Gender":1,
    "Age":35.0,
    "SibSp":0,
    "Parch":0,
    "Fare":55,
    "C":False,
    "Q":True,
    "S":False
}])

result = knn.predict(new_passenger)[0]
probability = knn.predict_proba(new_passenger)[0]
if result == 0:
    print("Not lived")
else:
    print("All is ok")
print("Probability:")
print(round(probability[1]*100,2), "%")
#print(df.head(5))