import pandas as pd
import logging


def preprocess_data(data):
    logging.info("Starting data preprocessing.")

    # Step 1: Check for missing values
    if data.isnull().sum().any():
        logging.warning(
            "Missing values detected. Filling missing values with 0.")
        # Fill missing values with 0 (assuming absence of symptom/condition)
        data = data.fillna(0)

    # Step 2: Ensure all values are binary (0 or 1)
    for col in data.columns:
        unique_vals = set(data[col].unique())
        if unique_vals.issubset({0, 1}):
            logging.info(f"Column '{col}' is already binary.")
        elif len(unique_vals) == 2:
            # Standardize binary column with two unique values
            sorted_vals = sorted(unique_vals)
            data[col] = data[col].apply(
                lambda x: 1 if x == sorted_vals[1] else 0)
        else:
            logging.warning(
                f"Column '{col}' is non-binary. Converting to binary.")
            mean_val = data[col].mean()
            data[col] = data[col].apply(lambda x: 1 if x > mean_val else 0)

    # Step 3: Ensure all columns are boolean (0 or 1)
    # Convert it boolean (ture or false)
    data = data.astype(bool)

    logging.info("Data preprocessing completed.")
    return data
