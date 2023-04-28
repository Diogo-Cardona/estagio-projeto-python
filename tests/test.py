import re

my_string = "Version : 0.0\nStatus : 0\nSOC : 5%\nCurrent : 2mA\nBAT1 : 0ºC\nBAT2 : 0ºC\nMOS : 0ºC\nRES : 0ºC\nVoltage : 3mV\nBattery off"

# Split the string into lines
lines = my_string.split("\n")

# Initialize an empty string to store the voltage value
voltage = []
percentage = []
current = []

# Loop through each line and extract the voltage value using regular expressions
for line in lines:
    # Extract the value for the Voltage key and remove the "mV" suffix
    match = re.search(r'^SOC\s*:\s*(\d+)%$', line)
    if match:
        percentage.append(match.group(1))
    match = re.search(r'^Voltage\s*:\s*(\d+)mV$', line)
    if match:
        voltage.append(match.group(1))
    match = re.search(r'^Current\s*:\s*(\d+)mA$', line)
    if match:
        current.append(match.group(1))
# Print the voltage value
print(percentage[0])
print(voltage[0])
print(current[0])
