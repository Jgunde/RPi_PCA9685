# RPi_PCA9685
A Python package for the Raspberry Pi to control the PCA9685 16 Channel 12-bit PWM driver.


# Dependencies:
smbus
  pip install smbus


# Usage:

** See example.py for a more detailed usage example.

import the PCA9685 class

from RPi_PCA9685.PCA9685 import PCA9685


create a PCA9685 object

pca9685 = PCA9685(i2c_address, i2c_port_num)


set the PWM frequency

pca9685.set_frequency(frequency)


you can set the pulse width on a specific channel:

pca9685.set_pwm(channel, 1200)


you can set the duty cycle on the specific channel:

pca9685.set_duty_cycle(channel, 67)
