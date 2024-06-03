#!/bin/bash

# Define your SSH username
USERNAME="praghur"

# List of user-defined node names (modify as needed)
NODES=("pc759" "pc829" "pc827" "pc758" "pc828" "pc830" "pc826")

# Loop through each node and open a detached terminal window
for NODE in "${NODES[@]}"; do
    # Construct the full hostname (e.g., pc425.emulab.net)
    HOSTNAME="${NODE}.emulab.net"
    
    # Open a detached terminal window and SSH into the node
    gnome-terminal --title="${NODE}" -- bash -c "ssh -o StrictHostKeyChecking=no ${USERNAME}@${HOSTNAME}; exec bash"
done
