export DISPLAY=:0
iptables -I INPUT -p tcp --dport 5000 -j ACCEPT
