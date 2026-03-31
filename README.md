House Price Prediction using Linear Regression
A simple machine learning project that predicts house prices based on size, number of rooms, and location using Linear Regression.

Table of Contents
Overview
Features
Requirements
Installation
Usage
How It Works
Dataset
Model Performance
Example Output
Customization
Future Enhancements
Overview
This project demonstrates a complete machine learning pipeline for predicting house prices. It uses Linear Regression to learn patterns from historical data and make predictions on new houses.

Key Capabilities:

Predicts prices based on square footage, room count, and location
Handles categorical data (locations) using one-hot encoding
Evaluates model accuracy using RMSE
Visualizes actual vs predicted prices
Features
10-house sample dataset included (easily replaceable with your own CSV)
Multiple features: Size (sqft), Rooms, Location
One-hot encoding for categorical location data
Train/test split (80/20) for proper evaluation
RMSE calculation to measure prediction accuracy
Scatter plot visualization of actual vs predicted prices
Example prediction for new house inputs
Requirements
pandas
scikit-learn
numpy
matplotlib
Python Version: 3.7 or higher

Installation
Clone or download this repository:
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction
Install required packages:
pip install pandas scikit-learn numpy matplotlib
Or use requirements.txt:

pip install -r requirements.txt
Usage
Basic Usage
Simply run the script:

python house_price_prediction.py
The script will:

Load the sample dataset
Train the Linear Regression model
Print RMSE (model accuracy)
Show an example prediction
Display a scatter plot of actual vs predicted prices
Using Your Own Dataset
Replace the sample data with your CSV file:

# Instead of the hardcoded data dictionary, load your CSV:
df = pd.read_csv('your_house_data.csv')

# Make sure your CSV has these columns:
# - Size_sqft (numeric)
# - Rooms (numeric)
# - Location (text/categorical)
# - Price (numeric)
Making Custom Predictions
Modify the example prediction section:

# Change these values to predict different houses
example = pd.DataFrame([[2000, 4, "A"]], 
                       columns=['Size_sqft', 'Rooms', 'Location'])
example_encoded = column_transformer.transform(example)
example_price = model.predict(example_encoded)
print(f"Predicted Price: ${int(example_price[0]):,}")
How It Works
1. Data Preparation
The script starts with a sample dataset of 10 houses with features:

Size_sqft: House size in square feet
Rooms: Number of bedrooms
Location: Categorical (A, B, or C)
Price: Target variable (what we're predicting)
2. Feature Encoding
Since Location is categorical, it's converted to numerical format using One-Hot Encoding:

Location A → [1, 0, 0]
Location B → [0, 1, 0]
Location C → [0, 0, 1]
3. Train/Test Split
Data is split 80/20:

Training set (8 houses): Used to train the model
Test set (2 houses): Used to evaluate performance
4. Model Training
A Linear Regression model learns the relationship:

Price = w₁(Size) + w₂(Rooms) + w₃(Location_A) + w₄(Location_B) + w₅(Location_C) + bias
5. Prediction & Evaluation
Model predicts prices on test set
RMSE measures average prediction error
Scatter plot shows how close predictions are to actual prices
Dataset
Sample Data Structure
Size_sqft	Rooms	Location	Price
850	2	A	120,000
900	2	B	130,000
1200	3	A	175,000
1500	3	C	200,000
1700	4	B	220,000
2000	4	A	260,000
2200	4	C	280,000
2500	5	B	310,000
2800	5	A	330,000
3000	6	C	360,000
Feature Descriptions
Size_sqft: Square footage of the house (850 - 3000 sqft)
Rooms: Number of bedrooms (2 - 6)
Location: Neighborhood identifier (A, B, or C)
Price: House price in USD ($120,000 - $360,000)
Model Performance
The model is evaluated using Root Mean Squared Error (RMSE):

RMSE = √(Σ(actual - predicted)² / n)
What RMSE tells you:

Lower RMSE = Better predictions
RMSE is in the same units as price (dollars)
Example: RMSE of $15,000 means predictions are off by ~$15k on average
Example Output
-----------------------------
Root Mean Squared Error: 8234.56
-----------------------------

Predicted Price for (1500 sqft, 3 rooms, Location B): 205000
A scatter plot window will also appear showing actual vs predicted prices.

Customization
Add More Features
data = {
    'Size_sqft': [...],
    'Rooms': [...],
    'Location': [...],
    'Age_years': [...],      # NEW: Age of house
    'Garage_spaces': [...],  # NEW: Garage capacity
    'Price': [...]
}

# Update feature selection
X = df[['Size_sqft', 'Rooms', 'Location', 'Age_years', 'Garage_spaces']]

# Update encoding (if new categorical features)
column_transformer = ColumnTransformer(
    [('encoder', OneHotEncoder(), ['Location'])],
    remainder='passthrough'
)
Try Different Test Sizes
# 70/30 split instead of 80/20
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.3, random_state=42
)
Add More Evaluation Metrics
from sklearn.metrics import r2_score, mean_absolute_error

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"R² Score: {r2:.4f}")
print(f"Mean Absolute Error: ${mae:,.2f}")
Future Enhancements
 Add data validation and error handling
 Implement cross-validation for robust evaluation
 Try advanced models (Random Forest, XGBoost)
 Feature engineering (price per sqft, room size ratio)
 Build a web interface with Streamlit/Flask
 Add feature importance visualization
 Implement hyperparameter tuning
 Create a prediction API
 Add data visualization dashboard
Acknowledgments
Scikit-learn Documentation
Pandas Documentation
Inspired by real-world house price prediction challenges
** If this project helped you, please give it a star!**
