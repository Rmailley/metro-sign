#!/bin/bash
cd /home/dietpi/metro-sign
sleep 10  # Wait for network to be fully ready
git pull --ff-only || true  # Don't fail if pull fails
python3 /home/dietpi/metro-sign/rpi-metro-display/rpi-metro-display.py \
  /home/dietpi/metro-sign/rpi-metro-display/log.txt \
  e28810b76b054f1d9b49eeb67548d077 \
  E04 \
  2 \
  /home/dietpi/metro-sign/rpi-metro-display/fonts/6x10.bdf \
  /home/dietpi/metro-sign/rpi-metro-display/lines.json \
  /home/dietpi/metro-sign/rpi-metro-display/stations.json
