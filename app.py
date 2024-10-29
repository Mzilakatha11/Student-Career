from flask import Flask, render_template, url_for, request

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

@app.route('/accounting', methods=['GET', 'POST'])
def accounting():
    eligible_courses = []
    aps = 0

    if request.method == 'POST':
        # Collect marks from the form
        marks = [
            int(request.form.get('math', 0)),
            int(request.form.get('accounting', 0)),
            int(request.form.get('business_studies', 0)),
            int(request.form.get('economics', 0)),
            int(request.form.get('english_home', 0)),
            int(request.form.get('life_orientation', 0))
        ]

        # Calculate APS and determine eligible courses
        aps = calculate_aps(marks)
        eligible_courses = get_eligible_courses(aps)

    return render_template('accounting.html', aps=aps, eligible_courses=eligible_courses)


# Sample course requirements for the Faculty of Accounting (course -> required APS)
COURSE_REQUIREMENTS = {
    "Diploma Accounting: DUT, MUT  Course duration: 3 yrs Min. points: 25": 25,
    "Dip ICT in Application Development:DUT Course duration: 3 yrs Min. points: 27": 27,
    "BBS Investment Science: UKZN course duration: 4 yrs Min. points: 38": 38,
}


@app.route('/art', methods=['GET', 'POST'])
def art():
    eligible_courses = []
    aps = 0

    if request.method == 'POST':
        # Collect marks from the form
        marks = [
            int(request.form.get('math', 0)),
            int(request.form.get('accounting', 0)),
            int(request.form.get('business_studies', 0)),
            int(request.form.get('economics', 0)),
            int(request.form.get('english_home', 0)),
            int(request.form.get('life_orientation', 0))
        ]

        # Calculate APS and determine eligible courses
        aps = calculate_aps(marks)
        eligible_courses = get_eligible_courses(aps)

    return render_template('art.html', aps=aps, eligible_courses=eligible_courses)


# Sample course requirements for the Faculty of Accounting (course -> required APS)
COURSE_REQUIREMENTS = {
    "Bachelor of Applied Arts in Commercial Photography: DUT  Course duration: 3 yrs Min. points: 28": 28,
    "BA (Anthropology & History):ZU Course duration: 3 yrs Min. points: 26": 26,
    "B Child & Youth Care: DUT course duration: 4 yrs Min. points: 38": 38,
}



def calculate_aps(marks):
    """Calculate APS points based on the student's marks."""
    aps = 0
    for mark in marks:
        if mark >= 80:
            aps += 7
        elif mark >= 70:
            aps += 6
        elif mark >= 60:
            aps += 5
        elif mark >= 50:
            aps += 4
        elif mark >= 40:
            aps += 3
        elif mark >= 30:
            aps += 2
        else:
            aps += 0
    return aps

def get_eligible_courses(aps):
    """Return a list of courses the student qualifies for based on APS."""
    return [
        course for course, required_aps in COURSE_REQUIREMENTS.items() if aps >= required_aps
    ]


if __name__ == "__main__":
    app.run(debug=True)