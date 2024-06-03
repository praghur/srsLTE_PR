#!/usr/bin/env bash

# Run appropriate setup script

NODE_ID=$(geni-get client_id)

if [ $NODE_ID = "rue1" ]; then
    chmod +x /local/repository/start-ue1.sh
    /local/repository/start-ue1.sh
elif [ $NODE_ID = "rue2" ]; then
    chmod +x /local/repository/start-ue2.sh
   /local/repository/start-ue2.sh
elif [ $NODE_ID = "rue3" ]; then
    chmod +x /local/repository/start-ue3.sh
   /local/repository/start-ue3.sh
elif [ $NODE_ID = "enb1" ]; then
    chmod +x /local/repository/start-enb1.sh
    /local/repository/start-enb1.sh
elif [ $NODE_ID = "enb2" ]; then
    chmod +x /local/repository/start-enb2.sh
    /local/repository/start-enb2.sh
elif [ $NODE_ID = "enb3r" ]; then
    chmod +x /local/repository/start-enb3r.sh
    /local/repository/start-enb3r.sh
elif [ $NODE_ID = "epc" ]; then
    chmod +x /local/repository/update_user_db.sh
    sudo /local/repository/update_user_db.sh
    chmod +x /local/repository/start-epc.sh
    /local/repository/start-epc.sh
else
    echo "no setup necessary"
fi
