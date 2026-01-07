import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_split_data():
    # 1. Load the dataset
    df = pd.read_csv('data.csv') 

    # 2. Define Features (X) and Target (y)
    X = df.drop(columns = ['Engine Condition']) 
    y = df['Engine Condition'] 

    # 3. Split the data
    X_train, X_test, y_train, y_test= train_test_split(
        X,y, test_size=0.2
    )

    return X_train, X_test, y_train, y_test
