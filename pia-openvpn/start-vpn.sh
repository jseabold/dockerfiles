#! /bin/sh

openvpn "$(ls -1 *ovpn | shuf -n 1)"
