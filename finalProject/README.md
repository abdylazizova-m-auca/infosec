# Disk Analyzer

This project is a utility that analyzes the sizes of all directories on a Linux-based machine and sends a report to an email daily.

## Features

- Scans all directories recursively from the root `/`
- Calculates size of each directory
- Saves a report to a file
- Sends the report via email
- Can be scheduled to run automatically every day

## Requirements

- Python 3
- An internet connection
- Access to an SMTP server (e.g., Gmail)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/abdylazizova_m/finalProject.git
    cd finalProject
    ```

2. Install Python if not installed.

3. Set up your SMTP email credentials in `disk_analyzer.py`.

4. Run the script:
    ```bash
    python3 disk_analyzer.py
    ```

5. Set up a cron job to run the script daily (see below).

## Schedule with Cron

Run:

```bash
crontab -e

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Demo Video

You can view the demo video of the project here: [Demo Video](https://drive.google.com/drive/folders/1i7dMmZo7aeff2ZvJ1ATXNzSsk9ecy2Ft?usp=drive_link)
