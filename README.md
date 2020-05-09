# RPi_PCA9685
A Python package for the Raspberry Pi to control the PCA9685 16 Channel 12-bit PWM driver.


## Dependencies:
pip install smbus


## Usage:

** See example.py for a more detailed usage example.

Import the PCA9685 class:
'from RPi_PCA9685.PCA9685 import PCA9685'

Create a PCA9685 object:
'pca9685 = PCA9685(i2c_address, i2c_port_num)'

Set the PWM frequency:
'pca9685.set_frequency(frequency)'

You can set the pulse width on a specific channel:
'pca9685.set_pwm(channel, 1200)'

You can set the duty cycle on the specific channel:
'pca9685.set_duty_cycle(channel, 67)'
