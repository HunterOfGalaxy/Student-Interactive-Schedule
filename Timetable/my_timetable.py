# By Bismaya
from flask import Flask, render_template, request, redirect, url_for
import json
import os
from pathlib import Path

app = Flask(__name__)

resolved_file_path = None

def get_file_location():
    """Locate schedule.json dynamically or prompt the user for a valid path."""
    # Check if the path is already set in the environment
    if "SCHEDULE_FILE_PATH" in os.environ:
        return Path(os.environ["SCHEDULE_FILE_PATH"])

    # Check for the default file in the current working directory
    default_file = Path("schedule.json")
    if default_file.exists():
        os.environ["SCHEDULE_FILE_PATH"] = str(default_file.resolve())
        return default_file.resolve()

    # Prompt user for file path if not found
    while True:
        user_file = input("Enter the full path to your schedule.json file: ").strip().strip('"')
        try:
            user_file_path = Path(user_file).expanduser().resolve()
            if user_file_path.exists():
                os.environ["SCHEDULE_FILE_PATH"] = str(user_file_path)
                return user_file_path
            else:
                print(f"File not found at {user_file_path}. Please try again.")
        except Exception as e:
            print(f"Invalid path provided. Error: {e}. Please try again.")


# Load JSON file location from user or current directory
user_directory = get_file_location()

# Load schedule from a file
def load_schedule():
    try:
        with open(user_directory, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error loading the schedule file. Starting with an empty schedule.")
        return {
            "Sunday": [], "Monday": [], "Tuesday": [], "Wednesday": [],
            "Thursday": [], "Friday": [], "Saturday": []
        }

# Save schedule to a file
def save_schedule(schedule):
    try:
        with open(user_directory, "w") as file:
            json.dump(schedule, file, indent=4)
    except Exception as e:
        print(f"Failed to save schedule: {e}")

# Initialize schedule
schedule = load_schedule()

@app.route("/")
def index():
    return render_template("schedule.html", schedule=schedule, enumerate=enumerate)

@app.route("/update_schedule", methods=["POST"])
def update_schedule():
    global schedule
    for day, sessions in schedule.items():
        for i in range(len(sessions)):
            # Fetch updated schedule data from form
            schedule[day][i]["time"] = request.form.get(f"{day}-time-{i}", "")
            schedule[day][i]["subject"] = request.form.get(f"{day}-subject-{i}", "")
            schedule[day][i]["course_code"] = request.form.get(f"{day}-course_code-{i}", "")
            schedule[day][i]["room"] = request.form.get(f"{day}-room-{i}", "")
            schedule[day][i]["teacher"] = request.form.get(f"{day}-teacher-{i}", "")
            schedule[day][i]["details"] = request.form.get(f"{day}-details-{i}", "")
    save_schedule(schedule)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
