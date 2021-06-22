
ip a > ip.txt

sleep 1

sudo service motion start
sleep 1

python3 /home/pi/Documents/baby_live/pyserver/indication.py
sleep 1
python3 /home/pi/message.py
sleep 1
python3 /home/pi/Documents/baby_live/pyserver/main.py



