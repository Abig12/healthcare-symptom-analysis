import pickle
from flask import Flask, render_template, request, jsonify
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import plotly
import plotly.express as px
import json
from utils.preprocessing import preprocess_data
from utils.visualization import (
    generate_correlation_heatmap,
    create_support_lift_scatter,
    create_top_rules_bar
)
import logging

# Set up logging
logging.basicConfig(
    filename='healthcare_symptom.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)


def convert_sets_to_strings(rules):
    rules = rules.copy()
    rules['antecedents'] = rules['antecedents'].apply(
        lambda x: ', '.join(list(x)))
    rules['consequents'] = rules['consequents'].apply(
        lambda x: ', '.join(list(x)))
    return rules


@app.route("/", methods=["GET", "POST"])
def home():
    logging.info("Received request on the home page.")
    data = pd.read_csv('data/healthcare_symptom_dataset.csv')
    processed_data = preprocess_data(data)

    # EDA Visualizations
    correlation_heatmap = generate_correlation_heatmap(processed_data)

    if request.method == "POST":
        min_support = float(request.form['min_support'])
        min_confidence = float(request.form['min_confidence'])
        logging.info(
            f"User inputs - min_support: {min_support}, min_confidence: {min_confidence}")

        frequent_itemsets = apriori(
            processed_data, min_support=min_support, use_colnames=True)
        num_itemsets = len(frequent_itemsets)
        rules = association_rules(
            frequent_itemsets, metric="confidence", min_threshold=min_confidence, num_itemsets=num_itemsets)
        rules_for_vis = convert_sets_to_strings(rules)

        # Calculate evaluation metrics
        avg_lift = rules['lift'].mean()
        avg_confidence = rules['confidence'].mean()
        avg_conviction = rules['conviction'].mean()
        avg_leverage = rules['leverage'].mean()

        scatter_plot = create_support_lift_scatter(rules_for_vis)
        top_rules_plot = create_top_rules_bar(rules_for_vis)

        plots = {
            'heatmap': json.dumps(correlation_heatmap, cls=plotly.utils.PlotlyJSONEncoder),
            'scatter': json.dumps(scatter_plot, cls=plotly.utils.PlotlyJSONEncoder),
            'top_rules': json.dumps(top_rules_plot, cls=plotly.utils.PlotlyJSONEncoder)
        }

        return render_template(
            "index.html",
            rules=rules_for_vis.head(10).to_html(classes='table'),
            plots=plots,
            min_support=min_support,
            min_confidence=min_confidence,
            avg_lift=avg_lift,
            avg_confidence=avg_confidence,
            avg_conviction=avg_conviction,
            avg_leverage=avg_leverage
        )

    return render_template("index.html", rules=None, avg_lift=None, avg_confidence=None, avg_conviction=None, avg_leverage=None)


@app.route("/feedback", methods=["POST"])
def feedback():
    feedback = request.form['feedback']
    logging.info(f"User feedback: {feedback}")
    return "Thank you for your feedback!", 200


if __name__ == "__main__":
    app.run(debug=True)
