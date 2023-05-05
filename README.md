# Selenium BDD Testing Framework
A Selenium-based web testing framework with BDD (Behavior-Driven Development) support using Gherkin language and the Page Object Model (POM) design pattern. This project is integrated with CI/CD capabilities, hosted on GitLab, and supports multiple web browsers.

## Features
- Selenium WebDriver for browser automation
- pytest for Python testing
- Behave for BDD and Gherkin support
- Page Object Model (POM) design pattern
- Cross-browser support (Chrome, Firefox)
- Browser version configuration via .env file
- Test reports (HTML, JUnit XML)
- CI/CD integration with GitLab

## Installation
1. Ensure you have Python 3.8 installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. Clone the repository:

```git clone https://github.com/markjsapp/Selenium-UI-Framework```

3. Install the required packages:

pip install -r requirements.txt

## Running the tests
1. Configure the desired browser and version in the `.env` file:

BROWSER=chrome
BROWSER=firefox

CHROME_VERSION=latest
CHROME_VERSION=93.0

FIREFOX_VERSION=latest
FIREFOX_VERSION=92.0

Uncomment the desired browser and version, and comment out the others.

2. Set the `BROWSER` environment variable:

export BROWSER=chrome
or
export BROWSER=firefox

On Windows, use `set` instead of `export`.

3. Run the tests:

pytest tests/
behave features/

4. Generate the test reports:
```
pytest --html=report_pytest.html --self-contained-html --junitxml=junit_pytest_report.xml tests/
behave --format pretty --format junit --outfile=junit_behave_report.xml --format html --outfile=report_behave.html features/
```

The test reports will be generated in the project's root directory.

## CI/CD
The project is set up with GitLab CI/CD. The `.gitlab-ci.yml` file defines the test stages and jobs for running the tests on Chrome and Firefox browsers. Test reports are generated and stored as artifacts in the GitLab pipeline.

## License
This project is released under the [MIT License](LICENSE).
