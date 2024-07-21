import requests
import matplotlib.pyplot as plt

# Prompt the user to enter the name of their city
city = input("Enter your city: ")

# Construct the base URL for the API request
url = 'http://api.waqi.info/feed/' + city + '/?token='

# Prompt the user to enter their API key
api_key = input("Enter your API key: ")

# Construct the full URL by appending the API key to the base URL
main_url = url + api_key

# Send a GET request to the API and store the response
r = requests.get(main_url)

# Parse the response JSON data
data = r.json()['data']

# Extract the Air Quality Index (AQI) from the data
aqi = data['aqi']

# Extract individual air quality indices (IAQI) from the data
iaqi = data['iaqi']

# Print each pollutant and its value
for i in iaqi.items():
    print(i[0], ':', i[1]['v'])

# Extract specific pollutants from the IAQI data
dew = iaqi.get('dew', 'Nil')
no2 = iaqi.get('no2', 'Nil')
o3 = iaqi.get('o3', 'Nil')
so2 = iaqi.get('so2', 'Nil')
pm10 = iaqi.get('pm10', 'Nil')
pm25 = iaqi.get('pm25', 'Nil')

# Print the AQI and individual pollutant levels
print(f'{city} AQI:', aqi, '\n')
print('Individual Air Quality:')
print('Dew:', dew)
print('NO2:', no2)
print('Ozone:', o3)
print('Sulphur:', so2)
print('PM10:', pm10)
print('PM25:', pm25)

# Create lists for the pollutants and their values
pollutants = [i for i in iaqi]
values = [i['v'] for i in iaqi.values()]

# Create a list to determine which slice of the pie chart to "explode"
explode = [0 for i in pollutants]
# Find the index of the maximum value to highlight it in the pie chart
mx = values.index(max(values))
explode[mx] = 0.1  # Set the explode value for the maximum slice

# Plot a pie chart of the pollutants and their values
plt.figure(figsize=(8, 6))
plt.pie(values, labels=pollutants, explode=explode, autopct='%1.1f%%', shadow=True)

# Set the title of the pie chart
plt.title(f'Air Pollutants and Their Probable Amount in Atmosphere [{city}]')

# Ensure the pie chart is drawn as a circle
plt.axis('equal')

# Display the pie chart
plt.show()
