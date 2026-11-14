print("===== College Of Engineering Agenda =====")


student_name = input("Enter your name: ")
course_name = input("Enter your course name: ")
assignment_name = input("Enter your assignment name: ")

days_until_due = int(input("Enter days until assignment is due: "))

remaining_assignments = total_assignments - completed_assignments


if total_assignments > 0:
    completion_percent = (completed_assignments / total_assignments) * 100
    remaining_percent = (remaining_assignments / total_assignments) * 100
else:
    completion_percent = 0
    remaining_percent = 0
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


print()
print("===== ENGINEERING STUDENT DASHBOARD =====")

print("Student:", student_name)
print("Course:", course_name)
print("Assignment:", assignment_name)

print()
print("===== ASSIGNMENT PROGRESS =====")

print("Total Assignments:", total_assignments)
print("Completed Assignments:", completed_assignments)
print("Remaining Assignments:", remaining_assignments)

print("Completion Percentage:", completion_percent, "%")
print("Remaining Percentage:", remaining_percent, "%")

print()
print("===== NOTIFICATION SUMMARY =====")

print("Days Until Due:", days_until_due)
print("Notification:", notification)
