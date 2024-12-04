// List of professors and their visualizations

function populateProfessorDropdown() {
    const dropdown = document.getElementById("professor-select");
    professors.forEach(professor => {
        const option = document.createElement("option");
        option.value = professor;
        option.textContent = professor;
        dropdown.appendChild(option);
    });
}

function loadProfessorData() {
    const professorName = document.getElementById("professor-select").value.replace(" ", "_");
    const insightsPath = `./data/Insights/${professorName}_insight.txt`;
    const visualizations = {
        keywordPieChart: `./data/Key Word Analysis/${professorName}_pie_chart.png`,
        tagOccurrences: `./data/Key Word Analysis/${professorName}_tag_occurrences.png`,
        wordcloud: `./data/Key Word Analysis/${professorName}_wordcloud.png`,
        sentimentChart: `./data/Visualizations/${professorName}_Sentiment_BarChart.png`,
        emotionPieChart: `./data/Visualizations/${professorName}_Emotion_PieChart.png`,
    };

    // Load insights
    fetch(insightsPath)
        .then(response => {
            if (!response.ok) throw new Error("Insights not available");
            return response.text();
        })
        .then(data => {
            document.getElementById("insights-container").innerHTML = `<pre>${data}</pre>`;
        })
        .catch(err => {
            document.getElementById("insights-container").innerHTML = `<p>Insights not available for ${professorName.replace("_", " ")}</p>`;
        });

    // Update visualization sources
    Object.entries(visualizations).forEach(([key, path]) => {
        const imgElement = document.getElementById(key);
        imgElement.src = path;
        imgElement.style.display = "block";
        imgElement.onerror = () => {
            imgElement.style.display = "none";
        };
    });
}

// Populate dropdown when the page loads
window.onload = populateProfessorDropdown;
