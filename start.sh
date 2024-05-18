#!/usr/bin/env bash

# Run appropriate setup script

NODE_ID=$(geni-get client_id)

if [ $NODE_ID = "rue1" ]; then
    /local/repository/start-ue1.sh
elif [ $NODE_ID = "rue2" ]; then
   /local/repository/start-ue2.sh
elif [ $NODE_ID = "enb1" ]; then
    /local/repository/start-enb1.sh
elif [ $NODE_ID = "enb2" ]; then
    /local/repository/start-enb2.sh
elif [ $NODE_ID = "enb3r" ]; then
    /local/repository/start-enb3r.sh
elif [ $NODE_ID = "epc" ]; then
    /local/repository/start-epc.sh
else
    echo "no setup necessary"
fi
