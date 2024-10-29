from flask import Flask, render_template, url_for, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/faculties')
def faculties():
    return render_template('faculties.html')

@app.route('/institutions')
def institutions():
    return render_template('institutions.html')

def calculate_aps(marks):
    """Calculate APS points based on the student's marks."""
    points = [7 if mark >= 80 else 6 if mark >= 70 else 5 if mark >= 60 else
              4 if mark >= 50 else 3 if mark >= 40 else 2 if mark >= 30 else 0 for mark in marks]
    return sum(points)

def get_eligible_courses(aps):
    """Fetch eligible courses from the database based on APS."""
    with sqlite3.connect('courses.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, institution, Duration FROM courses WHERE required_aps <= ?", (aps,))
        return [row[0] for row in cursor.fetchall()]

@app.route('/science', methods=['GET', 'POST'])
def science():
    eligible_courses = []
    aps = 0

    if request.method == 'POST':
        # Collect marks from the form
        marks = [int(request.form.get(subject, 0)) for subject in 
                 ['math', 'physics', 'life_sciences', 'geography', 'english_home', 'life_orientation']]

        # Calculate APS and determine eligible courses
        aps = calculate_aps(marks)
        eligible_courses = get_eligible_courses(aps)

    return render_template('science.html', aps=aps, eligible_courses=eligible_courses)
if __name__ == "__main__":
    app.run(debug=True)