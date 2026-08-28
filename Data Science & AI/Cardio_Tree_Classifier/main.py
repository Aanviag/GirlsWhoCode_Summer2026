import pandas as pd
import GWCutilities as util

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

print("\n-----\n")

#Create a variable to read the dataset
df = pd.read_csv("heartDisease_2020_sampling.csv")

print("We will be performing data analysis on this Indicators of Heart Disease Dataset. Here is a sample of it: \n")

#Print the dataset's first five rows


input("\n Press Enter to continue.\n")



#Data Cleaning
#Label encode the dataset
df = util.labelEncoder(df, ["HeartDisease", "GenHealth", "Smoking", "AlcoholDrinking", "PhysicalActivity", "Sex", "AgeCategory"])
print(df.head())

print("\nHere is a preview of the dataset after label encoding. \n")

input("\nPress Enter to continue.\n")

#One hot encode the dataset
df = util.oneHotEncoder(df, ["Race"])
print(df.head())

print(
    "\nHere is a preview of the dataset after one hot encoding. This will be the dataset used for data analysis: \n"
)


input("\nPress Enter to continue.\n")



#Creates and trains Decision Tree Model
from sklearn.model_selection import train_test_split
X = df.drop("HeartDisease", axis = 1)
y = df["HeartDisease"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 3)
print(X_train.head())

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth = 2, class_weight = 'balanced')
clf = clf.fit(X_train, y_train)






#Test the model with the testing data set and prints accuracy score
test_predictions = clf.predict(X_test)

from sklearn.metrics import accuracy_score
test_acc = accuracy_score(y_test, test_predictions)

print("\nThe accuracy with the testing data set of the Descision Tree is: " + str(test_acc))


#Prints the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, test_predictions, labels= [1, 0])
print("The confusion matrix of the tree is: ")
print(cm)





#Test the model with the training data set and prints accuracy score
train_predictions = clf.predict(X_train)

from sklearn.metrics import accuracy_score
train_acc = accuracy_score(y_train, train_predictions)

print("\nThe accuracy with the training data set of the Descision Tree is: " + str(train_acc))



input("\nPress Enter to continue.\n")



#Prints another application of Decision Trees and considerations
print("\nBelow is another application of decision trees and considerations for using them:\n")
print("Data Decision Trees can be used in restuarants to recommend food options to a user. One exmaple, is a pizza business, where the model can suggest pizza topics or options based on someone's tastes, options, etc.. One thing to make sure would be to feed unbaised data to the tree and make it not suggesting information based on location, race, etc..")




#Prints a text representation of the Decision Tree
print("\nBelow is a text representation of how the Decision Tree makes choices:")
input("Press Enter to continue.\n")

util.printTree(clf, X.columns)
