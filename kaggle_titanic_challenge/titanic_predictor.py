import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def train_and_predict(train_file, test_file):
    # Load data
    try:
        train_df = pd.read_csv(train_file)
        test_df = pd.read_csv(test_file)
    except FileNotFoundError:
        print("Error: train.csv or test.csv not found. Please ensure they are in the same directory.")
        return

    # Preprocessing (simplified)
    train_df['Sex'] = train_df['Sex'].map({'female': 0, 'male': 1})
    test_df['Sex'] = test_df['Sex'].map({'female': 0, 'male': 1})
    train_df['Age'].fillna(train_df['Age'].median(), inplace=True)
    test_df['Age'].fillna(test_df['Age'].median(), inplace=True)
    train_df['Fare'].fillna(train_df['Fare'].median(), inplace=True)
    test_df['Fare'].fillna(test_df['Fare'].median(), inplace=True)

    # Select features and target
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
    X_train = train_df[features]
    y_train = train_df['Survived']
    X_test = test_df[features]

    # Train model
    model = LogisticRegression(random_state=42, solver='liblinear')
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)
    return predictions

if __name__ == "__main__":
    # Create dummy data for demonstration if files don't exist
    if not (os.path.exists('train.csv') and os.path.exists('test.csv')):
        print("Creating dummy train.csv and test.csv for demonstration.")
        dummy_train_data = {
            'PassengerId': [1, 2, 3, 4, 5],
            'Survived': [0, 1, 1, 1, 0],
            'Pclass': [3, 1, 3, 1, 3],
            'Name': ['Braund, Mr. Owen Harris', 'Cumings, Mrs. John Bradley (Florence Briggs Thayer)', 'Heikkinen, Miss. Laina', 'Futrelle, Mrs. Jacques Heath (Lily May Peel)', 'Allen, Mr. William Henry'],
            'Sex': ['male', 'female', 'female', 'female', 'male'],
            'Age': [22.0, 38.0, 26.0, 35.0, 35.0],
            'SibSp': [1, 1, 0, 1, 0],
            'Parch': [0, 0, 0, 0, 0],
            'Ticket': ['A/5 21171', 'PC 17599', 'STON/O2. 3101282', '113803', '373450'],
            'Fare': [7.25, 71.2833, 7.925, 53.1, 8.05],
            'Cabin': ['', 'C85', '', 'C123', ''],
            'Embarked': ['S', 'C', 'S', 'S', 'S']
        }
        dummy_test_data = {
            'PassengerId': [6, 7, 8, 9, 10],
            'Pclass': [3, 1, 3, 1, 3],
            'Name': ['Moran, Mr. James', 'McCarthy, Mr. Timothy J', 'Palsson, Master. Gosta Leonard', 'Ostby, Mr. Engelhart C', 'Woolner, Mr. Hugh'],
            'Sex': ['male', 'male', 'male', 'male', 'male'],
            'Age': [None, 54.0, 2.0, 28.0, None],
            'SibSp': [0, 0, 3, 0, 0],
            'Parch': [0, 0, 1, 2, 0],
            'Ticket': ['330877', '17463', '349909', '113509', 'A/5. 3336'],
            'Fare': [8.4583, 51.8625, 21.075, 26.55, 8.6625],
            'Cabin': ['', 'E46', '', 'B30', ''],
            'Embarked': ['Q', 'S', 'S', 'S', 'S']
        }
        pd.DataFrame(dummy_train_data).to_csv('train.csv', index=False)
        pd.DataFrame(dummy_test_data).to_csv('test.csv', index=False)

    predictions = train_and_predict('train.csv', 'test.csv')
    if predictions is not None:
        print("Predictions:", predictions)
