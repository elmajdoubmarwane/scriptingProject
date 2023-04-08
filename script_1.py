import pandas as pd

# Prompt user for IP address
ip_address = input("Please enter an IP address: ")

# Split the IP address into octets
octets = ip_address.split(".")

# Create an empty Pandas DataFrame
df = pd.DataFrame()

# Loop through the octets and add data to the DataFrame
for i, octet in enumerate(octets):
    decimal = int(octet)
    binary = bin(decimal)
    hexadecimal = hex(decimal)
    df = pd.concat([df, pd.DataFrame({f"Octet{i+1}": [decimal, binary, hexadecimal]})], axis=1)

# Set the row labels
df.index = ["decimal", "binary", "hexadecimal"]

# Print the resulting DataFrame
print(df)
