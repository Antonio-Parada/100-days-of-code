import random
import math

class TitanicSurvivalPredictor:
    def __init__(self):
        # Simplified dummy dataset (features: Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)
        # Target: Survived (0 = No, 1 = Yes)
        self.data = [
            # Pclass, Sex (0=male, 1=female), Age, SibSp, Parch, Fare, Embarked (0=S, 1=C, 2=Q), Survived
            [3, 0, 22, 1, 0, 7.25, 0, 0], # Example: Male, not survived
            [1, 1, 38, 1, 0, 71.28, 1, 1], # Example: Female, survived
            [3, 1, 26, 0, 0, 7.92, 0, 1], # Example: Female, survived
            [1, 0, 35, 1, 0, 53.1, 0, 0], # Example: Male, not survived
            [3, 0, 35, 0, 0, 8.05, 0, 0], # Example: Male, not survived
            [3, 0, 20, 0, 0, 8.45, 2, 0], # Example: Male, not survived
            [2, 1, 28, 0, 0, 13.0, 0, 1], # Example: Female, survived
            [1, 0, 54, 0, 0, 51.86, 0, 0], # Example: Male, not survived
            [3, 1, 2, 1, 2, 21.07, 0, 0], # Example: Female child, not survived
            [2, 0, 14, 1, 0, 30.07, 1, 1]  # Example: Male child, survived
        ]

        # Simple weights for a very basic linear model (not actual logistic regression)
        # These weights are just for demonstration and will not be trained
        self.weights = {
            'Pclass': -0.5,
            'Sex': 1.0, # Female more likely to survive
            'Age': -0.02,
            'SibSp': -0.3,
            'Parch': -0.2,
            'Fare': 0.01,
            'Embarked': 0.1
        }
        self.bias = 0.1

    def _sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def predict_survival(self, passenger_data):
        # passenger_data: [Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]
        
        linear_combination = 0
        linear_combination += passenger_data[0] * self.weights['Pclass']
        linear_combination += passenger_data[1] * self.weights['Sex']
        linear_combination += passenger_data[2] * self.weights['Age']
        linear_combination += passenger_data[3] * self.weights['SibSp']
        linear_combination += passenger_data[4] * self.weights['Parch']
        linear_combination += passenger_data[5] * self.weights['Fare']
        linear_combination += passenger_data[6] * self.weights['Embarked']
        linear_combination += self.bias

        probability = self._sigmoid(linear_combination)
        return 1 if probability >= 0.5 else 0 # Classify as survived (1) or not (0)

    def evaluate_model(self):
        correct_predictions = 0
        total_predictions = len(self.data)

        print("\n--- Model Evaluation ---")
        for passenger in self.data:
            features = passenger[:-1] # All but the last element
            true_survival = passenger[-1] # Last element is Survived
            predicted_survival = self.predict_survival(features)
            
            print(f"Features: {features}, True: {true_survival}, Predicted: {predicted_survival}")
            if true_survival == predicted_survival:
                correct_predictions += 1
        
        accuracy = (correct_predictions / total_predictions) * 100
        print(f"Accuracy: {accuracy:.2f}%")
        return accuracy

if __name__ == '__main__':
    predictor = TitanicSurvivalPredictor()
    predictor.evaluate_model()
