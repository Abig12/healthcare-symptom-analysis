# Healthcare Symptom Analysis

A Flask-based web application for analyzing healthcare symptom data using association rule mining and interactive visualizations.

## Features
- **Association Rule Mining**: Discover relationships between symptoms and conditions using the Apriori algorithm.
- **Interactive Visualizations**: View correlation heatmaps, support-lift scatter plots, and top association rules using Plotly.
- **Preprocessing**: Automatically preprocess the dataset to handle missing values and convert non-binary data.
- **User-Friendly Interface**: Built with Flask, HTML, CSS, and JavaScript for a seamless user experience.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Abig12/healthcare-symptom-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd healthcare-symptom-analysis
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open your browser and go to `http://127.0.0.1:5000` to view the application.

## Usage
- **Homepage**: Set the `min_support` and `min_confidence` values for association rule mining.
- **Visualizations**: Explore interactive charts for correlation heatmaps, support-lift scatter plots, and top association rules.
- **Association Rules**: View the top 10 association rules and their evaluation metrics (lift, confidence, conviction, leverage).

## Dataset
The dataset used in this project is `healthcare_symptom_dataset.csv`, which contains binary data for symptoms and conditions. It includes the following columns:
- **Symptoms**: `Fever`, `Cough`, `Fatigue`, `Headache`, `Sore Throat`, `Runny Nose`, `Sneezing`, `Nausea`, `Muscle Pain`, `Chills`.
- **Conditions**: `Flu`, `Cold`, `Allergy`.

## Technologies Used
- **Backend**: Flask, Python
- **Frontend**: HTML, CSS, JavaScript
- **Data Visualization**: Plotly
- **Association Rule Mining**: mlxtend (Apriori algorithm)

## Screenshots
### Homepage
![Image](https://github.com/user-attachments/assets/04bc2e74-5db5-441c-99f3-03a564098730)
