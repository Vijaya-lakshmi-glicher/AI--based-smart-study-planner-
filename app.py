from datetime import datetime

print("===== AI-Based Smart Study Planner =====")

subjects = []
n = int(input("Enter number of subjects: "))

for i in range(n):
    name = input(f"\nEnter Subject {i+1} Name: ")
    exam_date = input("Enter Exam Date (YYYY-MM-DD): ")
    difficulty = input("Difficulty (Easy/Medium/Hard): ")

    subjects.append({
        "name": name,
        "exam_date": exam_date,
        "difficulty": difficulty
    })

study_hours = int(input("\nEnter available study hours per day: "))

today = datetime.today()

for subject in subjects:
    exam = datetime.strptime(subject["exam_date"], "%Y-%m-%d")
    days_left = (exam - today).days

    if subject["difficulty"].lower() == "hard":
        priority = 3
    elif subject["difficulty"].lower() == "medium":
        priority = 2
    else:
        priority = 1

    subject["days_left"] = days_left
    subject["priority"] = priority

subjects.sort(key=lambda x: (x["days_left"], -x["priority"]))

print("\n===== SMART STUDY TIMETABLE =====")

for subject in subjects:
    if subject["priority"] == 3:
        hours = study_hours * 0.5
    elif subject["priority"] == 2:
        hours = study_hours * 0.3
    else:
        hours = study_hours * 0.2

    print(f"\nSubject      : {subject['name']}")
    print(f"Exam Date    : {subject['exam_date']}")
    print(f"Days Left    : {subject['days_left']}")
    print(f"Difficulty   : {subject['difficulty']}")
    print(f"Study Hours  : {hours:.1f} hrs/day")

print("\nBest of Luck for Your Exams!")
