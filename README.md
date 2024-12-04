# **Student Feedback Analysis Web Application**

## **Overview**
This project is a Flask-based web application designed to visualize and present professor feedback and sentiment analysis for the University of Minnesota’s Computer Science department. The app displays pre-generated insights and visualizations for selected professors, offering a static, user-friendly interface.

---

## **Features**
- **Professor Insights**: Display structured actionable feedback based on student comments.
- **Keyword Analysis**: Visualizations including pie charts, tag occurrences, and word clouds.
- **Sentiment and Emotion Analysis**: Graphs showcasing sentiment distribution and emotion breakdowns.
- **Static Data**: All insights and visualizations are pre-generated, ensuring quick and seamless presentation.

---

## **Technologies Used**
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Jinja2
- **Data Visualization**: Matplotlib, Seaborn, WordCloud
- **Markdown Rendering**: `markdown` library for formatting insights.

---

## **File Structure**
```plaintext
StudentFeedbackAnalysis-App/
├── app/
│   ├── __init__.py               # Flask app initialization
│   ├── routes.py                 # Application routes and logic
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css        # Styling for the web app
│   │   ├── data/                 # Static data folder
│   │   │   ├── Insights/         # Text insights for professors
│   │   │   ├── Key Word Analysis/ # Keyword analysis visualizations
│   │   │   └── Visualizations/   # Sentiment and emotion analysis charts
│   ├── templates/
│   │   ├── index.html            # Home page for professor selection
│   │   └── result.html           # Professor insights and visualization display
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
├── run.py                        # Main entry point to run the app
