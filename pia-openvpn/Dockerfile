FROM alpine:latest

RUN apk add --no-cache openvpn

COPY start-vpn.sh /etc/openvpn
COPY pia/ /etc/openvpn
WORKDIR /etc/openvpn
ENTRYPOINT ["./start-vpn.sh"]
