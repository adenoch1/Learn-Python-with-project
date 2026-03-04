# Python Log Analyzer

A simple Python command-line tool that analyzes web server logs and produces useful metrics.

This project is designed to demonstrate how Python can be used in **DevOps and SRE environments** to process logs and extract operational insights.

It is also used in my YouTube tutorial:

**Python Log Analyzer Project | Optional, Dataclass, Counter & argparse**

---

# Features

This tool analyzes a log file and calculates:

- Total number of requests
- Error rate
- Top 5 IP addresses by request count
- Average latency per endpoint

---

# Technologies Used

The project demonstrates the use of several important Python modules:

- `typing.Optional` – safe return values
- `dataclasses.dataclass` – structured data modeling
- `collections.Counter` – counting frequencies
- `collections.defaultdict` – aggregating metrics
- `argparse` – building command line tools

---

# Log Format

The script expects logs in the following format:


METHOD PATH STATUS LATENCY_MS IP


Example:


GET / 200 12 10.0.0.1
GET /health 200 2 10.0.0.2
POST /login 401 15 10.0.0.3
GET /products 200 35 10.0.0.4


---

# Installation

Clone the repository:


git clone https://github.com/adenoch1/Learn-Python-with-project.git


Navigate to the project directory:


cd log_analyzer


---

# Running the Log Analyzer

Run the script with a log file:


python3 log_analyzer.py access.log


Example output:


Total Requests: 20
Error Rate: 0.15

Top 5 IPs:
10.0.0.1 5
10.0.0.4 4

Average Latency per Endpoint:
/ 10.5
/products 40.0
/orders 120.0


---

# Project Structure


python-log-analyzer/
│
├── log_analyzer.py
├── access.log
├── README.md


---

# Learning Objectives

This project helps demonstrate:

- Log parsing techniques
- Defensive programming
- Data aggregation
- Building CLI tools in Python
- Basic observability metrics

---

# Future Improvements

Possible improvements for this project:

- Calculate **p95 latency**
- Filter endpoints such as `/health`
- Detect suspicious IP activity
- Export metrics as JSON
- Add real Nginx log parsing

---

# Author

**Enoch Adekanye**

DevOps Engineer | AWS Architect | Python Educator

YouTube Channel: *Enoch Platform*

---

# License

This project is open source and available under the MIT License.