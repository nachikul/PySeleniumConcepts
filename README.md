# Selenium with Python - Teaching Examples

This repository contains multiple examples of Selenium scripts written in Python. These scripts are designed to teach important Selenium concepts to Computer Engineering students, covering a wide range of topics like basic web navigation, element location, form handling, handling alerts, and using explicit waits.

## Prerequisites

Before running the scripts, make sure you have the following installed:

1. **Python 3.x**: You can download it from [here](https://www.python.org/downloads/).
2. **Selenium**: Install Selenium using the following command:
    ```bash
    pip install selenium
    ```
3. **ChromeDriver**: Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to your system's PATH or provide the path in the scripts.

## Repository Structure

This repository includes one combined script that demonstrates all key Selenium concepts and five individual scripts that break these concepts down:

### Combined Script:
- **`selenium_combined.py`**: This script showcases all important Selenium features in one file, including:
  - Basic Web Navigation
  - Locating Elements
  - Handling Forms and Input
  - Handling Alerts and Frames
  - Using Explicit Waits

### Individual Concept Scripts:
1. **`basic_navigation.py`**: Demonstrates how to open a webpage and navigate through links.
2. **`locating_elements.py`**: Shows how to find web elements using various strategies such as ID, Name, XPath, etc.
3. **`handling_forms.py`**: Illustrates form handling by inputting data into text fields and submitting forms.
4. **`alerts_and_frames.py`**: Covers interacting with JavaScript alerts and handling iframe switching.
5. **`explicit_wait.py`**: Demonstrates how to use WebDriverWait to wait until an element is visible or clickable.

## How to Run the Scripts

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/selenium-python-teaching.git
    cd selenium-python-teaching
    ```

2. Ensure that you have the required packages installed by running:
    ```bash
    pip install -r requirements.txt
    ```

3. Download and set up ChromeDriver:
   - Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   - Make sure it matches your Chrome browser version.
   - Either place it in your system’s PATH or provide the path in the Python scripts.

4. Run the combined example:
    ```bash
    python selenium_combined.py
    ```

5. Or run any of the individual concept scripts:
    ```bash
    python basic_navigation.py
    python locating_elements.py
    python handling_forms.py
    python alerts_and_frames.py
    python explicit_wait.py
    ```

## Customization

To log in to your own Amazon account and perform searches, you’ll need to update the email and password in the `selenium_combined.py` script:

```python
email_input.send_keys("your-email@example.com")
password_input.send_keys("your-password")