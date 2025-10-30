# Load packages
import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

print("Loaded packages from pandas, numpy, and sklearn.")

# Load training data
train_df = pd.read_csv("src/data/train.csv")
print("Loaded train.csv.")

# View data
train_df.head()
print("Viewing data...")

# Keep only variables needed for prediction
train_df_sub = train_df[['Survived','Pclass','Sex','Age','Fare']]
print("Created filtered data frame that includes variables I think would help predict survival: pclass, sex, age, and fare")

train_df_sub.isna().sum() #missing values for age
print("Checking missing values; find missing values for age")

# Impute missing values
print(train_df_sub.isna().sum()) #look for missing values; find missing for age
train_df_sub.loc[:, 'Age'] = train_df_sub['Age'].fillna(train_df_sub['Age'].median()) #fill missing age values
print("Imputed missing age values using median age.")

# Initialize encoder
le_sex = LabelEncoder()
print("Initialized label encoders to encode categorical variables for sex.")

# Fit and transform 'Sex'
train_df_sub.loc[:, 'Sex'] = le_sex.fit_transform(train_df_sub['Sex'])

print("Encoded categorial variable 'Sex'.")

train_df_sub.head()
print("Viewing data...")

# Building regression model 
x_train = train_df_sub.drop("Survived", axis=1)
y_train = train_df_sub["Survived"]

model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)
print("Logistic regression model trained.") 

# Accuracy on training set
train_preds = model.predict(x_train)
train_acc = accuracy_score(y_train, train_preds)
print(f"Training accuracy: {train_acc:.4f}")

# Load test data 
test_df = pd.read_csv("src/data/test.csv")
print("test.csv loaded.")

# Filter data to same prediction variables
test_df_sub = test_df[['Pclass','Sex','Age','Fare']]

print(test_df_sub.isna().sum()) #missing values for age
print("Checking missing values; find missing values for age")

test_df_sub.loc[:, 'Age'] = test_df_sub['Age'].fillna(test_df_sub['Age'].median()) #fill missing age values
test_df_sub.loc[:, 'Fare'] = test_df_sub['Fare'].fillna(test_df_sub['Fare'].median()) #fill missing fare values
print("Imputed missing age and fare values using median values.")

# Initialize encoder
le_sex = LabelEncoder()
print("Initialized label encoders to encode categorical variables for sex.")

# Fit and transform 'Sex'
test_df_sub.loc[:, 'Sex'] = le_sex.fit_transform(test_df_sub['Sex'])

print("Encoded categorial variable 'Sex'.")

# Predict and evaluate
test_preds = model.predict(test_df_sub)
print("Predictions on test set complete.")

# Reload original test data to recover PassengerId
original_test_df = pd.read_csv("src/data/test.csv")

# Create a DataFrame with PassengerId and predictions
output_df = pd.DataFrame({
    "PassengerId": original_test_df["PassengerId"],
    "Survived": test_preds
})

# Save predictions to CSV
output_df.to_csv("src/test_predictions.csv", index=False)
print("Predictions saved to test_predictions.csv.")