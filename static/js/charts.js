class ChartManager {
  constructor() {
    this.charts = {};
  }

  updateCharts(data) {
    this.updateCorrelationHeatmap(data.heatmap);
    this.updateSupportLiftScatter(data.scatter);
    this.updateTopRulesBar(data.topRules);
    this.updateHistogram(data.ageHistogram, "age_histogram");
    this.updateBarChart(data.diabetesBar, "diabetes_bar");
  }

  updateCorrelationHeatmap(data) {
    const layout = {
      title: "Feature Correlation Heatmap",
      height: 400,
      margin: { t: 50, l: 50, r: 50, b: 50 },
    };
    Plotly.newPlot("correlation-heatmap", data, layout);
  }

  updateSupportLiftScatter(data) {
    const layout = {
      title: "Support vs Lift Analysis",
      height: 400,
      xaxis: { title: "Support" },
      yaxis: { title: "Lift" },
    };
    Plotly.newPlot("support-lift-scatter", data, layout);
  }

  updateTopRulesBar(data) {
    const layout = {
      title: "Top 10 Association Rules by Lift",
      height: 400,
      xaxis: { title: "Rules", tickangle: -45 },
      yaxis: { title: "Lift Value" },
    };
    Plotly.newPlot("top-rules-bar", data, layout);
  }

  updateHistogram(data, elementId) {
    const layout = {
      title: "Age Distribution",
      height: 400,
      xaxis: { title: "Age" },
      yaxis: { title: "Count" },
    };
    Plotly.newPlot(elementId, data, layout);
  }

  updateBarChart(data, elementId) {
    const layout = {
      title: "Diabetes Distribution",
      height: 400,
      xaxis: { title: "Diabetes" },
      yaxis: { title: "Count" },
    };
    Plotly.newPlot(elementId, data, layout);
  }
}
