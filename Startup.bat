@ECHO OFF
color 2
netsh wlan set hostednetwork mode=allow ssid="VIT5G"
netsh wlan connect ssid=VIT2.4G name=VIT5G
netsh wlan set hostednetwork mode=allow ssid="VIT2.4G"
netsh wlan connect ssid=VIT2.4G name=VIT2.4G
netsh wlan set hostednetwork mode=allow ssid="VIT5"
netsh wlan connect ssid=VIT2.4G name=VIT5
netsh wlan set hostednetwork mode=allow ssid="VIT2.4"
netsh wlan connect ssid=VIT2.4G name=VIT2.4
exit
