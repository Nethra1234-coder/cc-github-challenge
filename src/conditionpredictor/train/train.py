from conditionpredictor.dataprep.load_data import load_and_split_data
from conditionpredictor.train.model import get_model
from conditionpredictor.train.trainer import train_and_evaluate

def main():
    X_train, X_test, y_train, y_test = load_and_split_data()
    model = get_model()
    train_and_evaluate(model, X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()
