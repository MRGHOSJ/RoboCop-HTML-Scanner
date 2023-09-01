# RoboCop Python Script for .robot Files

This repository contains Python scripts for scanning .robot files using RoboCop and converting the scan results into an HTML report.

## Prerequisites

Before running the scripts, ensure you have the following prerequisites installed:

1. [RoboCop](https://github.com/MarketSquare/robotframework-robocop): Ensure that RoboCop is installed and available in your system's PATH.

2. Python: You'll need Python 3.8 installed on your system to execute the provided Python scripts. You can download Python from [python.org](https://www.python.org/downloads/).

## How to Use

Follow these steps to use the provided scripts:

1. **Clone the Repository**

   Clone this repository to your local machine using the following command:

   ```shell
   git clone https://github.com/your-username/RoboCop-HTML-Scanner.git

2. **Run RoboCop Scan**

Navigate to the repository folder:


   ```shell
   cd RoboCop-HTML-Scanner
```

Run the robocop_scan.py script to scan .robot files in the current directory and its subdirectories. The scan results will be saved in robocop_output.txt and in robocop_output.html format.

   ```shell
python robocop_scan.py
```

4. **View the HTML Report**

You can now open robocop_output.html in your web browser to view the scan results in a user-friendly HTML format.

## Example HTML Report

The HTML report will include information about the scanned .robot files, detected issues, and scan statistics. Issues are categorized and listed along with the line numbers where they were found.

## Scan Time and Issue Statistics

The HTML report will also display the total scan time and provide issue statistics by ID, making it easier to identify common issues.

- W0508 (line-too-long): 4
- W1001 (trailing-whitespace): 2
- W0302 (wrong-case-in-keyword-name): 2
- W0203 (missing-doc-suite): 1
- W1003 (empty-lines-between-sections): 1
