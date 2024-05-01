#!/bin/bash
systemctl status telex-wrapperd.service &>/dev/null
if [ $? != 0 ]
then
    echo "[CREATE] telex-wrapperd.service"
    echo "ExecStart=/usr/bin/bash ${0}" >> ./telex-wrapperd.service
    echo "" >> ./telex-wrapperd.service
    echo "[Install]" >> ./telex-wrapperd.service
    echo "WantedBy=multi-user.target" >> ./telex-wrapperd.service
    cp telex-wrapperd.service /etc/systemd/system &>/dev/null
    systemctl enable telex-wrapperd.service
    echo "[CREATE] telex-wrapperd.service - Done"
fi
echo "[UPDATE] Checking for Updates..."
echo "[CLONE] Cloning Repository https://github.com/RPi2User/telex-terminal.git"
git clone https://github.com/RPi2User/telex-terminal.git
systemctl restart telex-wrapperd.service 