import xgboost as XGBClassifier 

def get_model():
    xgb_model = XGBClassifier(
        n_estimators=100, 
        learning_rate=0.1,
        max_depth=4,
        eval_metric='logloss'
    )
    return xgb_model
