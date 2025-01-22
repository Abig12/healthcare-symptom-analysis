import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import pickle
from utils.preprocessing import preprocess_data
import logging

# Set up logging
logging.basicConfig(
    filename='healthcare_symptom.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def train_model():
    # Load data
    data = pd.read_csv('data/healthcare_symptom_dataset.csv')
    logging.info(
        f"Loaded dataset with {data.shape[0]} records and {data.shape[1]} features.")
    logging.info("Dataset Summary Statistics:\n" + str(data.describe()))

    # Preprocess data
    processed_data = preprocess_data(data)
    logging.info("Data preprocessing completed.")

    # Verify the processed data
    print("Processed Data Summary:")
    print(processed_data.head())
    print("\nUnique Values in Each Column:")
    print(processed_data.nunique())

    # Generate frequent itemsets
    min_support = 0.1
    frequent_itemsets = apriori(
        processed_data, min_support=min_support, use_colnames=True)
    logging.info(
        f"Generated {len(frequent_itemsets)} frequent itemsets with min_support={min_support}.")

    # Generate association rules
    min_confidence = 0.7
    num_itemsets = len(frequent_itemsets)
    rules = association_rules(
        frequent_itemsets, metric="confidence", min_threshold=min_confidence, num_itemsets=num_itemsets)
    logging.info(
        f"Generated {len(rules)} association rules with min_confidence={min_confidence}.")

    # Save rules to a file
    with open('model.pkl', 'wb') as model_file:
        pickle.dump(rules, model_file)
    logging.info("Association rules saved to model.pkl.")

    # Print evaluation metrics
    print("Top 10 Association Rules:")
    print(rules.head(10))
    print(f"Average Lift: {rules['lift'].mean()}")
    print(f"Average Confidence: {rules['confidence'].mean()}")
    print(f"Average Conviction: {rules['conviction'].mean()}")
    print(f"Average Leverage: {rules['leverage'].mean()}")


if __name__ == "__main__":
    train_model()
