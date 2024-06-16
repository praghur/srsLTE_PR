#!/bin/bash

# Define the list of nodes
nodes=("pc829" "pc830" "pc833" "pc828" "pc826")

# Define the corresponding window titles
#window_titles=("epc" "enb1" "ue1" "enb2" "ue2" "uet1" "uet2" "enb3" "ue3")

# SSH username and hostname
username="praghur"
host_suffix=".emulab.net"
#k=1;
# Loop through the nodes and open Terminator windows with custom titles
for i in "${!nodes[@]}"; do
#	for k in "${!window_titles[@]}"; do
    node="${nodes[$i]}"
    num_windows=1

    # Set the number of windows based on the index
    if [ $i -eq 1 ]; then
        num_windows=2
    elif [ $i -eq 2 ]; then
        num_windows=2
    elif [ $i -eq 3 ]; then
        num_windows=1
    elif [ $i -eq 4 ]; then
        num_windows=1
    #elif [ $i -eq 5 ]; then
    #    num_windows=2
    fi

    # Open the specified number of Terminator windows with custom titles
    for ((j=1; j<=$num_windows; j++)); do
#        title="${window_titles[k]}"
        terminator -e "ssh -o StrictHostKeyChecking=no ${username}@${node}${host_suffix}" --title="${title}" &
 #   done
    	done
done
