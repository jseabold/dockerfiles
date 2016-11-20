#! /usr/bin/env bash

wget http://www.privateinternetaccess.com/openvpn/openvpn.zip
unzip openvpn.zip -d pia/
rm openvpn.zip

for f in ls pia/*.ovpn; do
    echo "auth-user-pass auth.conf" >> "$f";
done
