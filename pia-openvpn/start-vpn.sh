#! /bin/sh

openvpn "$(ls -1 *ovpn | shuf -n 1)" &
VPN_PID=$!
trap "kill -s TERM ${VPN_PID}; exit 0" TERM
while true; do :; done
