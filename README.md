# baby_live server

Raspberry Pi based Server for real time monitoring of baby in a cradle.
> All sensor readings are taken through arduino board. So make sure it is connected before starting the server.
> Real time video input is accomplished using PiCam and Motion library. 

# Frontend App

Frontend Application is built using React.js & Ionic-Capacitor 
https://github.com/AshiqMehmood/babyMonitor/

# Setup
1) change 'message.py' to add your email, if you want to know the ip_address without an ip_scanner. (optional step to get ip address.)
2) Add your ''SSID name and passwd'' of your network to wpa_supplicant.conf before initial bootup.
3) Ensure arduino is connected to any usb port of pi. (This step is necessary for server to start).
4) Start raspberry pi. This will auto connect to network on bootup.
5) You will recieve an email with ip_addresses around 90 secs after bootup. (only if you completed step 1)
6) A python server should be up automatically. It will be live at ''localhost:5000/ ''.
7) Real time camera feed is up at  ''localhost:8081/''.
8) You can now connect to pi from client.
