# System Log Analyzer

This is a small Python tool that analyzes system log files and extracts basic statistics such as error counts, warning counts and the most common error messages.

I built this project to practice working with log files, pattern matching and simple data analysis in Python.

## Features

- Reads and parses log files
- Detects **ERROR**, **WARNING** and **INFO** entries
- Counts how many times each type appears
- Finds the most common error messages
- Generates a JSON report with the results

## How to Run

Run the script and provide the log file as an argument.

Example:

python analyzer.py sample.log

## Example Output

Log Analysis Report
-------------------
Total lines: 7  
Errors: 3  
Warnings: 2  
Info: 2  

Most common errors:
Database connection failed : 2  
Timeout error : 1  

A JSON report will also be generated as `report.json`.

## Example Log Format

2026-03-10 INFO Server started  
2026-03-10 WARNING Disk usage high  
2026-03-10 ERROR Database connection failed  
2026-03-10 ERROR Timeout error  

## Project Structure

system-log-analyzer  
├ analyzer.py  
├ sample.log  
├ report.json  
└ README.md  

## Notes

This project is mainly intended as a simple tool for practicing log parsing and basic data processing in Python.
