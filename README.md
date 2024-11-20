# Flask-based Interactive Weekly Schedule Manager By Bismaya

This is a simple web-based application built using **Flask** that allows users to manage and edit their weekly schedule. The application loads the schedule from a `schedule.json` file and presents it on a webpage where users can edit, update, and save their timetable.

## Features

- **Dynamic Schedule**: Load your weekly schedule from a JSON file (`schedule.json`).
- **Edit and Customize**: Users can edit the schedule in real-time via the web interface.
- **Local Web Server**: The application runs on a local server (`http://127.0.0.1:5000`) where the schedule can be viewed and modified.

---

## Requirements

To run the project, you'll need to have the following installed:

- **Python 3.x** (preferably 3.7+)
- **Flask** (Python web framework)

You can install Flask by running:

```bash
pip install flask
```

---

## How to Run

### 1. Clone the Repository or Download the Files

Download or clone the repository to your local machine.

```bash
git clone https://github.com/HunterOfGalaxy/Student-Interactive-Schedule.git
```

### 2. Prepare `schedule.json`

The application uses a `schedule.json` file to store the weekly timetable. You can either create a new file, or use an existing one.

Here is an example of the JSON structure used for the schedule:

```json
{
  "Sunday": [],
  "Monday": [],
  "Tuesday": [],
  "Wednesday": [],
  "Thursday": [],
  "Friday": [],
  "Saturday": []
}
```

You will be prompted to provide the full path to this file when running the program for the first time.

### 3. Run the Application

Open your terminal or command prompt, navigate to the project directory, and run the following command:

```bash
python my_timetable.py
```

This will start the Flask development server. If you are using Flask's default configuration, the server will be accessible at `http://127.0.0.1:5000` or `http://localhost:5000`.

### 4. Access the Application

After running the application, open your browser and go to the following URL:

```
http://127.0.0.1:5000
```

You will see a webpage displaying your current weekly schedule. You can now edit the timetable directly through the web interface. Any changes made will automatically be saved back to your `schedule.json` file.

### 5. Edit the Schedule

- The schedule is displayed for each day of the week (Sunday to Saturday).
- Users can edit the schedule by filling out the form fields for each session, including time, subject, course code, room, teacher, and details.
- After editing, click the **Save** button to update the `schedule.json` file.

### 6. Customize the HTML Template

If you want to change the layout or design of the schedule, you can edit the `schedule.html` template located in the `templates/` folder. This HTML file controls the structure of the web page, and you can modify it according to your preferences.

---

## How to Customize the Schedule

1. **Modify the `schedule.json` File**:
   - You can manually edit the `schedule.json` file at any time to change the schedule data (e.g., change course names, times, etc.).
   - Each day of the week has an array of sessions that can be modified.

2. **Edit the HTML Template**:
   - Open the `templates/schedule.html` file.
   - You can change how the schedule is displayed, such as adding styles or adjusting the layout.
   - For example, you could change the form fields or add additional input fields.

---

## Troubleshooting

### 1. **File Not Found Error**

If you get an error about the `schedule.json` file not being found, make sure that:
- You provide the **correct path** to the file when prompted.
- The file is properly formatted as a valid JSON file.
- The path is accessible (not blocked or located in a restricted directory).

### 2. **Permission Issues**

If you encounter permissions issues when saving the file, ensure that the directory where `schedule.json` is stored is writeable.

---

## Additional Notes

- **Flask Development Server**: This application uses Flask's built-in development server, which should only be used for development and testing. For production use, consider deploying with a production-grade WSGI server like **Gunicorn**.
- **Automatic File Path**: The application asks for the path to your `schedule.json` file on the first run. This path is then stored in the environment variable `SCHEDULE_FILE_PATH` to avoid asking again on subsequent Flask restarts during development.

---

## License

This project is licensed under the MIT License.

---

### Example Usage

1. Run the application with the command:

   ```bash
   python my_timetable.py
   ```

2. Provide the full path to your `schedule.json` file when prompted:

   ```bash
   Enter the full path to your schedule.json file: e.g. "D:\Timetable\schedule.json"
   ```

3. The application will open in your browser at `http://127.0.0.1:5000`, where you can view and edit your schedule.

---

This `README.md` file provides instructions on running, editing, and customizing the application. The key focus is on how to interact with the `schedule.json` file and how to start the Flask app to manage your weekly timetable.
