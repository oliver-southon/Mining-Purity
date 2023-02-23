import pandas as pd
import numpy as np

from tensorflow import keras
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor 
from sklearn.ensemble import GradientBoostingRegressor

from joblib import dump

def _RunRandomForest(X_values, y_values):
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X_values, y_values, test_size = 0.2, random_state=1)

    # Make Model
    rf = RandomForestRegressor(n_estimators=100, max_depth=3, random_state=1).fit(X_train, y_train)

    dump(rf, 'rf.joblib')

def _GradientBoost(X_values, y_values):
    X_train, X_test, y_train, y_test = train_test_split(X_values, y_values, random_state=2, test_size=0.1)
    sc = StandardScaler()
    X_train_std = sc.fit_transform(X_train)
    X_test_std = sc.fit_transform(X_test)

    gbr = GradientBoostingRegressor(
        n_estimators=100,
        max_depth=3,
        learning_rate=0.1,
        random_state=2
    )

    gbr.fit(X_train_std, y_train)   
    dump((gbr, sc), 'gbr.joblib')

def _NeuralNetwork(X_values, y_values):
    sc = StandardScaler()
    X_train, X_test, y_train, y_test = train_test_split(X_values, y_values, random_state=3, test_size=0.2) # Feature selection more important for NN, so using X_selected
    # Define the Network
    model = keras.Sequential([
        keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(1, activation='linear') # Linear function for final dense layer
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])

    # Standardise the data
    X_train_std = sc.fit_transform(X_train)
    X_test_std = sc.transform(X_test)

    # Train the model
    history = model.fit(X_train_std, y_train, epochs=30, batch_size=32, validation_data=(X_test_std, y_test))
    dump((model, sc), 'nn.joblib')

def _getXY():

    mining_data = pd.read_feather('modelling/mining_quality_data.feather')
    selected_features = ['% Iron Feed', 'Flotation Column 02 Air Flow',  'Flotation Column 04 Air Flow', 'Flotation Column 05 Air Flow', 'Ore Pulp Density', 'Ore Pulp Flow']

    X = mining_data[selected_features]
    y = mining_data['% Silica Feed']
    return X, y

# def getModels(X, y):
#     rf = _RunRandomForest(X, y)
#     gbr = _GradientBoost(X, y)
#     nn = _NeuralNetwork(X, y)

#     return rf, gbr, nn

def generateModels():
    X, y = _getXY()
    _RunRandomForest(X, y)
    _GradientBoost(X, y)
    _NeuralNetwork(X, y)


def makePreds(models, feature_values, scalers):
    predictions = [] # Store predictions

    # Check that the feature_values array has the correct shape
    if feature_values.shape != (1, 6):
        raise ValueError(f"Expected feature_values to have shape (1, 6), got {feature_values.shape}\n{feature_values}")

    # Predict using each model
    for model, scaler in zip(models, scalers):
        if type(model).__name__ != "RandomForestRegressor":
            # Scale input data
            feature_values_std = scaler.transform(feature_values)
            feature_values_std = feature_values_std.reshape(1, -1)
            # Run prediction
            pred_std = model.predict(feature_values_std)[0]

            # Change to float if in array
            if isinstance(pred_std, (list, tuple, np.ndarray)):
                pred_std = pred_std[0]

            # Save value
            predictions.append(pred_std)
        else:
            pred = model.predict(feature_values)[0]
            predictions.append(pred) # Save values

    return predictions # Return list of predictions

if __name__ == "__main__":
    generateModels()