from sklearn.metrics import accuracy_score, confusion_matrix
def train_and_evaluate(model, X_train, X_test, y_train, y_test):
    # 4. Initialize and Train XGBoost
    model.fit(X_train, y_train)

    # 5. Make Predictions
    y_pred = model.predict(X_test)

    # 6. Evaluate the Model
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print("\nConfusion Matrix:\n", confusion_matrix(y_test,y_pred))

    # 7. Importance Score
    importance = model.get_booster().get_scores(importance_type='gain')
    print("\nFeature Importance:", importance)
 