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
    #sudo killall srsepc
    #sudo echo "ue1,xor,001010123456789,00112233445566778899aabbccddeeff,opc,63bfa50ee6523365ff14c1f45f88737d,9001,000000001234,7,dynamic
    #ue2,xor,001010123456790,00112233445566778899aabbccddeeee,opc,63bfa50ee6523365ff14c1f45f88737d,8000,000000001235,7,dynamic
    #ue3,xor,001010123456791,00112233445566778899aabbccddffff,opc,63bfa50ee6523365ff14c1f45f88737d,7000,000000001236,7,dynamic" > /etc/srslte/user_db.csv
    #echo "Text successfully written to user_db.csv"
    chmod +x /local/repository/update_user_db.sh
    sudo /local/repository/update_user_db.sh
    chmod +x /local/repository/start-epc.sh
    /local/repository/start-epc.sh
else
    echo "no setup necessary"
fi
