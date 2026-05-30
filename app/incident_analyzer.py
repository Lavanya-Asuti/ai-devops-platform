import os

def summarize_logs():

    log_file = "app/logs/app.log"

    if not os.path.exists(log_file):
        return "No logs found"

    with open(log_file, "r") as f:
        logs = f.readlines()

    recent_logs = logs[-20:]

    summary = "Incident Summary:\n"

    for log in recent_logs:
        summary += f"- {log}"

    return summary