import json
import utime
from machine import Pin, PWM, ADC

import wifi


def main(conf):
    adc = ADC(0)
    pwm = PWM(Pin(4), freq=10000)

    while True:
        raw = adc.read()

        raw -= conf['vol_range_min']
        if raw < 0:
            raw = 0

        raw /= conf['vol_range_max']
        if raw > 1.0:
            raw = 1.0

        raw = 1.0 - raw

        print(1024 * raw)
        pwm.duty(int(1024 * raw))
        utime.sleep(0.1)


def entrypoint():
    with open('config.json', 'r') as f:
        conf = json.load(f)

    while True:
        wifi.up(conf['ssid'], conf['psk'])
        wifi.show_ifconfig()
        main(conf)


entrypoint()
