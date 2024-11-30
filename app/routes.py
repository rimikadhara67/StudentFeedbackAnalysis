from flask import Blueprint, render_template, request
from app.analysis import analyze_professor_feedback
import pandas as pd

# Blueprint for routing
main = Blueprint("main", __name__)

# Load the data once
data = pd.read_csv("data/UMN_CS_Professors_Ratings.csv")

@main.route("/")
def index():
    # Extract professor names for the dropdown
    professor_names = sorted(data["Name"].unique())
    return render_template("index.html", professors=professor_names)

@main.route("/results", methods=["POST"])
def results():
    selected_professor = request.form.get("professor")
    if not selected_professor:
        return "Error: No professor selected", 400

    # Filter data for the selected professor
    professor_data = data[data["Name"] == selected_professor]

    # Perform analysis
    analysis_results = analyze_professor_feedback(professor_data)

    return render_template(
        "result.html",
        professor=selected_professor,
        summary=analysis_results["summary"],
        visuals=analysis_results["visuals"]
    )
