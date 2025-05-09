import os
import smtplib
import subprocess
from datetime import datetime
from email.message import EmailMessage

today = datetime.now().strftime("%Y-%m-%d")

def get_directory_report():
    try:
        # List of directories
        directories = ["/home", "/var", "/usr", "/tmp", "/etc", "/opt"]

        full_report = ""
        
        for directory in directories:
            full_report += f"\nDisk usage for {directory}:\n"
            
            try:
                result = subprocess.run(
                    ["du", "-h", "--max-depth=1", directory],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                
                if result.stderr:
                    # Skip the directory if there is an error(permission denied)
                    full_report += f"Error: Cannot read {directory}. Skipping...\n"
                else:
                    full_report += result.stdout + "\n"
            except Exception as e:
                full_report += f"Error: Could not analyze {directory} due to: {str(e)}\n"
        
        return full_report
    except Exception as e:
        return f"Error during analysis: {str(e)}"

# Send the report via email
def send_email(report):
    sender_email = "abdylazizova_m@auca.kg"
    receiver_email = "abdylazizova_m@auca.kg"
    email_password = os.getenv("EMAIL_PASSWORD")

    if not email_password:
        print("EMAIL_PASSWORD environment variable not set.")
        return

    msg = EmailMessage()
    msg["Subject"] = f"Disk Usage Report - {today}"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(report)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, email_password)
            smtp.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    report = get_directory_report()
    send_email(report)

