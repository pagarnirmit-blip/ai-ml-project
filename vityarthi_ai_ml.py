#  HOUSE PRICE PREDICTION 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

# CREATE SAMPLE DATASET (You can replace with your own CSV)
data = {
    'Size_sqft': [850, 900, 1200, 1500, 1700, 2000, 2200, 2500, 2800, 3000],
    'Rooms': [2, 2, 3, 3, 4, 4, 4, 5, 5, 6],
    'Location': ["A", "B", "A", "C", "B", "A", "C", "B", "A", "C"],
    'Price': [120000, 130000, 175000, 200000, 220000, 260000, 280000, 310000, 330000, 360000]
}

df = pd.DataFrame(data)

# SET FEATURES & TARGET
X = df[['Size_sqft', 'Rooms', 'Location']]
y = df['Price']

# ONE-HOT ENCODE LOCATION
column_transformer = ColumnTransformer(
    [('encoder', OneHotEncoder(), ['Location'])],
    remainder='passthrough'
)

X_encoded = column_transformer.fit_transform(X)

# TRAIN / TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42
)

# TRAIN THE MODEL
model = LinearRegression()
model.fit(X_train, y_train)

#PREDICT ON TEST SET
y_pred = model.predict(X_test)

# CHECK ACCURACY
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("\n-----------------------------")
print("Root Mean Squared Error:", rmse)
print("-----------------------------\n")


#PREDICTION

example = pd.DataFrame([[1500, 3, "B"]], 
                       columns=['Size_sqft', 'Rooms', 'Location'])

example_encoded = column_transformer.transform(example)
example_price = model.predict(example_encoded)

print("Predicted Price for (1500 sqft, 3 rooms, Location B):", int(example_price))

#PLOT ACTUAL VS PREDICTED
plt.scatter(y_test, y_pred, color='blue')
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.grid(True)
plt.show()
