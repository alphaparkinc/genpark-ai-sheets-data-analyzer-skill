class AiSheetsDataAnalyzerClient:
    def analyze(self, csv_header_row: str, analysis_query: str) -> dict:
        columns = [c.strip() for c in csv_header_row.split(",")]
        numeric_cols = [c for c in columns if any(kw in c.lower() for kw in ["price", "revenue", "count", "qty", "amount", "age"])]
        chart = "Bar Chart" if len(numeric_cols) >= 2 else "Line Chart" if numeric_cols else "Table"
        summary = f"Analyzing {len(columns)} columns {columns} for: '{analysis_query}'. "                   f"Numeric dimensions: {numeric_cols or ['none detected']}."
        return {"insight_summary": summary, "chart_recommendation": chart}
