
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        student_name = request.form["student_name"]
        course_name = request.form["course_name"]
        assignment_name = request.form["assignment_name"]

        days_until_due = int(request.form["days_until_due"])
        total_assignments = int(request.form["total_assignments"])
        completed_assignments = int(request.form["completed_assignments"])

        if total_assignments < 0 or not 0 <= completed_assignments <= total_assignments:
            return "Invalid assignment totals", 400

        remaining_assignments = total_assignments - completed_assignments

        if total_assignments > 0:
            completion_percent = (completed_assignments / total_assignments) * 100
        else:
            completion_percent = 0

        if days_until_due < 0:
            notification = "OVERDUE"
        elif days_until_due == 0:
            notification = "DUE TODAY"
        elif days_until_due <= 2:
            notification = "HIGH PRIORITY"
        elif days_until_due <= 5:
            notification = "MEDIUM PRIORITY"
        else:
            notification = "LOW PRIORITY"

        result = {
            "student": student_name,
            "course": course_name,
            "assignment": assignment_name,
            "remaining": remaining_assignments,
            "completion": completion_percent,
            "notification": notification
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
