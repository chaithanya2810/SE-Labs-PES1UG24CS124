"""Track student attendance and generate attendance reports."""
import tarfile
from pathlib import Path
import os
import csv
import ssl
#import json
#import subprocess
from datetime import datetime
import requests

# Global attendance register
students = {}
ERP_URL = "https://erp.college.example/api/attendance"
ERP_API_KEY = os.getenv("ERP_API_KEY")
MIN_ATTENDANCE = 75

def add_student(roll_no, name, section="A"):
    """Add a student to the attendance tracker."""
    students[roll_no] = {"name": name, "section": section, "records": []}

def mark_attendance(roll_no, date, status, register):
    """Record attendance for a student and update the register."""
    register.setdefault(date, []).append(roll_no)
    students[roll_no]["records"].append((date, status))
    return register

def attendance_percentage(roll_no):
    """Calculate a student's attendance percentage."""
    records = students[roll_no]["records"]

    if not records:
        return 0

    present = sum(record[1] == "P" for record in records)
    total = len(records)

    return int(present / total * 100)

def is_eligible(percentage):
    """Check whether a student meets the attendance threshold."""
    return percentage >= MIN_ATTENDANCE

def shortage_list():
    """Return the roll numbers of students below the threshold."""
    result = []
    for roll_no in students:
        if not is_eligible(attendance_percentage(roll_no)):
            result.append(roll_no)
    if len(result) == 0:
        return None
    return result

def has_long_absence(roll_no, days=3):
    """Check for a consecutive run of absences."""
    statuses = [
        status for _, status in students[roll_no]["records"]
    ]

    return any(
        statuses[i:i + days] == ["A"] * days
        for i in range(len(statuses))
    )

def latest_date(roll_no):
    """Return the most recent attendance date."""
    records = students[roll_no]["records"]

    if not records:
        return None

    dates = [
        datetime.strptime(record[0], "%Y-%m-%d").date()
        for record in records
    ]

    return max(dates).isoformat()

def safe_csv_text(value):
    """Prevent formula-like text from executing in spreadsheet software."""
    text = str(value)

    if text.startswith(("=", "+", "-", "@", "\t", "\r")):
        return "'" + text

    return text


def export_csv(path="attendance.csv"):
    """Export attendance percentages to a CSV file."""
    with open(
        path, "w", newline="", encoding="utf-8"
    ) as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["roll_no", "name", "percentage"])

        for roll_no, student in students.items():
            writer.writerow([
                safe_csv_text(roll_no),
                safe_csv_text(student["name"]),
                attendance_percentage(roll_no),
            ])

    return path


def sync_to_erp(roll_no):
    """Submit a student's attendance percentage to the ERP."""
    if not ERP_API_KEY:
        raise RuntimeError(
            "Set the ERP_API_KEY environment variable before syncing."
        )

    payload = {
        "roll_no": roll_no,
        "pct": attendance_percentage(roll_no),
    }

    response = requests.post(
        ERP_URL,
        json=payload,
        headers={"X-API-Key": ERP_API_KEY},
        timeout=10,
    )

    response.raise_for_status()
    return response.status_code

def backup_reports():
    """Create a compressed archive of CSV report files."""
    report_files = sorted(Path.cwd().glob("*.csv"))

    if not report_files:
        return None

    with tarfile.open("reports_backup.tgz", "w:gz") as archive:
        for report_file in report_files:
            archive.add(report_file, arcname=report_file.name)

    return "reports_backup.tgz"

def create_tls_context():
    """Create a TLS context using secure default settings."""
    return ssl.create_default_context()

def run_job(command_args):
    """Describe a job using arguments without shell interpretation."""
    return {"command": command_args}


def schedule_reminders():
    """Prepare the attendance-shortage reminder job."""
    return run_job(["send_sms", "--shortage"])

def main():
    """Run the attendance-tracker demonstration."""
    register = {}
    add_student("R01", "Aditi")
    add_student("R02", "=HYPERLINK(\"http://evil.example\",\"Bharat\")")
    for date, status in [("2026-09-01", "P"), ("2026-09-02", "P"), ("2026-09-03", "L"),
                         ("2026-09-04", "P"), ("2026-09-05", "H")]:
        mark_attendance("R01", date, status, register)
    for date, status in [("2026-09-01", "P"), ("2026-09-01", "P"), ("2026-09-02", "A"),
                         ("2026-09-03", "A"), ("2026-09-04", "A"), ("2026-09-03", "P")]:
        mark_attendance("R02", date, status, register)
    register = mark_attendance("R01", "2030-01-01", "P", register)
    print("R01 attendance %:", attendance_percentage("R01"))
    print("R02 attendance %:", attendance_percentage("R02"))
    print("Is 75% eligible?", is_eligible(75))
    print("Shortage list:", shortage_list())
    print("R02 long absence?", has_long_absence("R02"))
    print("R02 latest date:", latest_date("R02"))
    print("Register entries for 2026-09-01:", register["2026-09-01"])
    print("Exported to:", export_csv())
    print("Reminder job:", schedule_reminders())
    print("ERP sync skipped (no network)")


if __name__ == "__main__":
    main()
