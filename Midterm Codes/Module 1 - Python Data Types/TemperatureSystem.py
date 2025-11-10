#Simulating a Day's Temperature
#BCS13 - Ubungen
Reading = {
    'Temperature readings': (15.2, 16.8, 18.4, 20.1, 21.5, 23.0, 19.8, 17.6)
}

temperatures = Reading['Temperature readings']
highest = max(temperatures)
lowest = min(temperatures)

print(f"Temperature readings: {temperatures}")
print(f"Maximum Temperature: {highest}Â°C")
print(f"Minimum Temperature: {lowest}Â°C")
