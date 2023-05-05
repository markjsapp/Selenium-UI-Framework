import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

generate_reports = os.getenv("GENERATE_REPORTS", "true").lower() == "true"

pytest_args = ["pytest"]
behave_args = ["behave"]

if generate_reports:
    pytest_args.extend([
        "--html=report_pytest.html",
        "--self-contained-html",
        "--junitxml=junit_pytest_report.xml",
        "tests/"
    ])
    behave_args.extend([
        "--format", "pretty",
        "--format", "junit",
        "--outfile", "junit_behave_report.xml",
        "--format", "html",
        "--outfile", "report_behave.html",
        "features/"
    ])

subprocess.run(pytest_args)
subprocess.run(behave_args)