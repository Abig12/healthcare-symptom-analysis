import plotly.express as px
import pandas as pd


def generate_correlation_heatmap(data):
    corr = data.corr()
    return px.imshow(
        corr,
        title='Feature Correlation Heatmap',
        color_continuous_scale='RdBu'
    )


def create_support_lift_scatter(rules):
    return px.scatter(
        rules,
        x='support',
        y='lift',
        size='confidence',
        title='Support vs Lift Analysis',
        hover_data=['antecedents', 'consequents'],
        color='confidence',
        color_continuous_scale='Viridis'
    )


def create_top_rules_bar(rules):
    top_rules = rules.nlargest(10, 'lift')
    top_rules['rule'] = top_rules.apply(
        lambda x: f"{x['antecedents']} → {x['consequents']}", axis=1
    )
    return px.bar(
        top_rules,
        x='rule',
        y='lift',
        title='Top 10 Association Rules by Lift',
        color='confidence',
        color_continuous_scale='Viridis'
    )
