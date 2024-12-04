from flask import render_template, request, url_for
import os
from markdown import markdown
from app import app

# Use app.root_path to construct absolute paths
DATA_PATH = os.path.join(app.root_path, "static", "data")
INSIGHTS_PATH = os.path.join(DATA_PATH, "Insights")
KEYWORD_ANALYSIS_PATH = os.path.join(DATA_PATH, "Key Word Analysis")
VISUALIZATIONS_PATH = os.path.join(DATA_PATH, "Visualizations")


@app.route("/")
def index():
    # Get list of professors from the Insights folder
    try:
        professors = [
            file.replace("_insight.txt", "").replace("_", " ")
            for file in os.listdir(INSIGHTS_PATH)
            if file.endswith("_insight.txt")
        ]
    except FileNotFoundError:
        return "Insights directory not found. Please check your file structure.", 500

    return render_template("index.html", professors=professors)


@app.route("/professor")
def professor():
    professor_name = request.args.get("professor_name")
    if not professor_name:
        return "Professor not selected", 400

    safe_professor_name = professor_name.replace(" ", "_")

    # Define file paths for existence checks
    visualizations_files = {
        "keyword_pie_chart": os.path.join(KEYWORD_ANALYSIS_PATH, f"{professor_name}_pie_chart.png"),
        "tag_occurrences": os.path.join(KEYWORD_ANALYSIS_PATH, f"{professor_name}_tag_occurrences.png"),
        "wordcloud": os.path.join(KEYWORD_ANALYSIS_PATH, f"{professor_name}_wordcloud.png"),
        "sentiment_chart": os.path.join(VISUALIZATIONS_PATH, f"{professor_name}_Sentiment_BarChart.png"),
        "emotion_pie_chart": os.path.join(VISUALIZATIONS_PATH, f"{professor_name}_Emotion_PieChart.png"),
    }

    # Generate URLs for existing files
    visualizations_urls = {
        key: url_for("static", filename=f"data/{os.path.relpath(path, start=os.path.join(app.root_path, 'static', 'data'))}")
        for key, path in visualizations_files.items() if os.path.exists(path)
    }

    # Read insights file
    insights_file = os.path.join(INSIGHTS_PATH, f"{safe_professor_name}_insight.txt")
    insights = None
    if os.path.exists(insights_file):
        with open(insights_file, "r", encoding="utf-8") as file:
            raw_insights = file.read()
            insights = markdown(raw_insights)

    # Check if no data exists
    if not insights and not visualizations_urls:
        return render_template(
            "result.html", professor_name=professor_name, no_data=True
        )

    return render_template(
        "result.html",
        professor_name=professor_name,
        insights=insights,
        visualizations=visualizations_urls,
    )
