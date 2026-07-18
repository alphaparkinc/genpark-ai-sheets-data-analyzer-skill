from client import AiSheetsDataAnalyzerClient
client = AiSheetsDataAnalyzerClient()
result = client.analyze(
    "product_name, price, revenue, region, quarter",
    "Which region had the highest revenue growth last quarter?"
)
print(result["insight_summary"])
print("Recommended chart:", result["chart_recommendation"])
