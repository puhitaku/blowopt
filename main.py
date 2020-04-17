import json
import utime
from machine import Pin, PWM

import wifi


def main():
    pwm = PWM(Pin(4), freq=10000)
    pwm.duty(400)
    while True:
        utime.sleep(999)


def entrypoint():
    with open('config.json', 'r') as f:
        conf = json.load(f)

    while True:
        wifi.up(conf['ssid'], conf['psk'])
        wifi.show_ifconfig()
        main()


entrypoint()
