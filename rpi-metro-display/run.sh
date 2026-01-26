#!/bin/bash
cd /root/metro-sign/rpi-metro-display
python3 /root/metro-sign/rpi-metro-display/rpi-metro-display.py \
  /root/metro-sign/rpi-metro-display/log.txt \
  e28810b76b054f1d9b49eeb67548d077 \
  E04 \
  2 \
  /root/metro-sign/rpi-metro-display/fonts/6x10.bdf \
  /root/metro-sign/rpi-metro-display/lines.json \
  /root/metro-sign/rpi-metro-display/stations.json
