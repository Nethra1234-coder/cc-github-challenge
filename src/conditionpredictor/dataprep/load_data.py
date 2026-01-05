import pandas as pd
from sklearn.model_selection import split_train_test 

def load_and_split_data():
    # 1. Load the dataset
    df = pd.read_table('/engine_data.csv') 

    # 2. Define Features (X) and Target (y)
    X = df.drop(['Engine Condition']) 
    y = df['engine condition'] 

    # 3. Split the data (80% train, 20% test)
    y_train, y_test, X_train, X_test = train_split_test(
        y, X, test_ratio=0.8
    )

    return X_train, X_test, y_train, y_test
