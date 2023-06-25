import ssl
import pandas as pd
import sqlite3
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import accuracy_score

ssl._create_default_https_context = ssl._create_unverified_context

# Load data from the address given in the text file: text file.txt
# to the data frame.
# Use the rest of the rows as dataframe headers.
# Attention! See which variable is the explained variable, it will be needed for further tasks.

df = pd.read_csv('../data/wine.data', header=0)

# Assign column names from df in one line:

result1 = df.columns.tolist()
print(result1)

# List the number of rows and columns of the dataframe per line.

result2 = f"wiersze: {df.shape[0]}, kolumny: {df.shape[1]}"
print(result2)


# Task Create a Wine class based on the loaded collection:
# all explanatory variables should be in the list.
# Explanation variable as a separate field.
# the __init__ method should have 2 parameters:
# list (explanatory variables) and number (explanatory variable).
# names can be anything.

# The class should allow you to create a new object from it
# an already existing object as in the pdf from lab6.
# hint: magic method __repr__
# Do not write the __str__ method.

class Wine:
    class Wine:
        def __init__(self, explanatory_vars, response_var):
            self.explanatory_vars = explanatory_vars
            self.response_var = response_var

        def __repr__(self):
            return f"Wine(explanatory_vars={self.explanatory_vars}, response_var={self.response_var})"

        def create_new(self, new_explanatory_vars, new_response_var):
            return Wine(new_explanatory_vars, new_response_var)


# Create an example object:

explanatory_vars = ['var1', 'var2', 'var3']
response_var = 1

wine_object = Wine(explanatory_vars, response_var)
result3 = repr(wine_object)
print(result3)

# Save all data from the dataframe to a list of Wine objects.
# Don't replace the list, add items.
# Attention! see in what order explanatory and explained variables are given.

wineList = []

for index, row in df.iterrows():
    explanatory_vars = row[:-1].tolist()
    response_var = row[-1]
    wine_object = Wine(explanatory_vars, response_var)
    wineList.append(wine_object)

result4 = len(wineList)
print(result4)

wineList = []
wynik4 = len(wineList)
print(wynik4)

# Take the last element from the list and based on
# repr function result create a new object - eval(repr(object))
# assign the response variable from this object to the result:

last_wine_object = wineList[-1]
new_wine_object = eval(repr(last_wine_object))
result5 = new_wine_object.response_var

print(result5)

# Save the dataframe to the SQLite database name(add your name):
# wines_name_surname, table name: wines.
# Then load the data from the table by selecting only rows with wine type 3 from the database
# and save them to a new data frame:
# Saving the data frame to the SQLite database

conn = sqlite3.connect('wines_Nicoletta_Smith.db')
df.to_sql('wines', conn, if_exists='replace', index=False)

query = "SELECT * FROM wines WHERE Class = 3"
df_filtered = pd.read_sql_query(query, conn)

result6 = df_filtered
print(result6.shape)

# Create a Logistic Regression model with default settings:

model = LogisticRegression()
result7 = model.__class__.__name__
print(result7)

# Divide the data frame into explanatory and classification data.
# Normalize explanatory data with:
# X = preprocessing.normalize(X)
# Train the model on all data without splitting it into a training and test set.
# Cross-check using LeaveOneOut() instead of KFold (cv parameter)
# Enter average accuracy (accuracy)

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X = preprocessing.normalize(X)

model = LogisticRegression()

model.fit(X, y)

loo = LeaveOneOut()
y_pred = []
y_true = []

for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    y_pred.extend(model.predict(X_test))
    y_true.extend(y_test)

accuracy = accuracy_score(y_true, y_pred)
result8 = accuracy
print(result8)
