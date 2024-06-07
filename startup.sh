#!/bin/bash
#Revision #1
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


####Revision #2
#!/bin/bash

# Define your SSH username
USERNAME="praghur"

# List of user-defined node names and the corresponding number of windows (modify as needed)
NODES=("pc756" "pc745" "pc741" "pc753")
WINDOWS=(1 3 3 2)

# Loop through each node and open the specified number of detached terminal windows
for i in "${!NODES[@]}"; do
    NODE="${NODES[$i]}"
    NUM_WINDOWS="${WINDOWS[$i]}"
    
    # Construct the full hostname (e.g., pc425.emulab.net)
    HOSTNAME="${NODE}.emulab.net"
    
    # Open the specified number of detached terminal windows and SSH into the node
    for _ in $(seq "$NUM_WINDOWS"); do
        gnome-terminal --title="${NODE}" -- bash -c "ssh -o StrictHostKeyChecking=no ${USERNAME}@${HOSTNAME}; exec bash"
    done
done
