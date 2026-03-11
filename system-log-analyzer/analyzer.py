import re
import json
import argparse
from collections import Counter


def analyze_log(file_path):

    total_lines = 0
    errors = 0
    warnings = 0
    infos = 0

    error_messages = []

    error_pattern = re.compile(r"ERROR (.*)")

    with open(file_path, "r", encoding="utf-8") as file:

        for line in file:

            total_lines += 1

            if "ERROR" in line:
                errors += 1

                match = error_pattern.search(line)

                if match:
                    error_messages.append(match.group(1).strip())

            elif "WARNING" in line:
                warnings += 1

            elif "INFO" in line:
                infos += 1

    error_percentage = (errors / total_lines) * 100 if total_lines > 0 else 0

    print("\nLog Analysis Report")
    print("-------------------")
    print("Total lines:", total_lines)
    print("Errors:", errors)
    print("Warnings:", warnings)
    print("Info:", infos)
    print("Error percentage:", round(error_percentage, 2), "%")

    top_errors = {}

    if error_messages:

        print("\nMost common errors:")

        counter = Counter(error_messages)

        for error, count in counter.most_common(5):
            print(error, ":", count)
            top_errors[error] = count

    report = {
        "total_lines": total_lines,
        "errors": errors,
        "warnings": warnings,
        "info": infos,
        "error_percentage": error_percentage,
        "top_errors": top_errors
    }

    with open("report.json", "w") as outfile:
        json.dump(report, outfile, indent=4)

    print("\nJSON report saved as report.json")


def main():

    parser = argparse.ArgumentParser(description="System Log Analyzer")

    parser.add_argument("logfile", help="Path to log file")

    args = parser.parse_args()

    analyze_log(args.logfile)


if __name__ == "__main__":
    main()