# Air-Pollution-Predictor

City Air Quality Index (AQI) Checker
This Python script fetches and displays the Air Quality Index (AQI) and individual pollutant levels for a specified city using the World Air Quality Index project API. Additionally, it visualizes the pollutant levels in a pie chart using Matplotlib.

Features:
● Fetches AQI data for a specified city.
● Displays individual pollutant levels.
● Visualizes pollutant levels in a pie chart.

Requirements:
● Python 3.x
● requests library
● matplotlib library

You can install the required libraries using pip:

bashcode: 
pip install requests matplotlib

Usage
1. Clone the repository:
bash code:
git clone https://github.com/yourusername/aqi-checker.git
cd aqi-checker

2. Run the script:
bash code:
python aqi_checker.py

3. Enter the required inputs when prompted:
● City name: The name of the city for which you want to check the AQI.
● API key: Your API key for the World Air Quality Index project. You can obtain an API key by signing up on the World Air Quality Index website.

Example
When you run the script, it will prompt you to enter your city and API key. For example:

Enter your city: Kanpur
Enter your API key: your_api_key_here

The script will then output the AQI and individual pollutant levels for the specified city and display a pie chart of the pollutant levels.

Script Details:
● Fetching Data: The script constructs the API request URL using the entered city name and API key, sends a request to the World Air Quality Index API, and parses the JSON response.
● Displaying Data: It prints the AQI and individual pollutant levels.
● Visualizing Data: It creates a pie chart of the pollutant levels, highlighting the pollutant with the highest value.

Author: Nilesh Parmar https://www.linkedin.com/in/nilesh-parmar-/
