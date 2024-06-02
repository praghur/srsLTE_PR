#!/bin/bash

# Path to the user_db.csv file
USER_DB_FILE="/etc/srslte/user_db.csv"

# Define the data to be added (replace with your actual data)
DATA="ue1,xor,001010123456789,00112233445566778899aabbccddeeff,opc,63bfa50ee6523365ff14c1f45f88737d,9001,000000001234,7,dynamic
ue2,xor,001010123456790,00112233445566778899aabbccddeeee,opc,63bfa50ee6523365ff14c1f45f88737d,8000,000000001235,7,dynamic
ue3,xor,001010123456791,00112233445566778899aabbccddffff,opc,63bfa50ee6523365ff14c1f45f88737d,7000,000000001236,7,dynamic"

# Append the data to the user_db.csv file
echo "$DATA" >> "$USER_DB_FILE"

echo "Data added successfully to $USER_DB_FILE"
