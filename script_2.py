show_version = "*0 CISCO3750-SEC-K9 FTX0003877X "

# Remove leading and trailing whitespace
show_version = show_version.strip()

# Split the string to extract model and serial_number
parts = show_version.split()
model = parts[1]
serial_number = parts[2]

# Check if 'Cisco' is contained in the model string (ignore capitalization)
if 'cisco' in model.lower():
    print("Model: ", model)

# Check if '3750' is in the model string
if '3750' in model:
    print("Serial Number: ", serial_number)
