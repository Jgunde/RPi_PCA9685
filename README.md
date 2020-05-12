# RPi_PCA9685
A Python package for the Raspberry Pi to control the PCA9685 16 Channel 12-bit PWM driver.

![Image of PCA9685](https://github.com/Jgunde/RPi_PCA9685/blob/master/PCA9685%20Image.jpg)


## Dependencies:
sudo apt-get install python-smbus
<br/><br/>


## Usage:

**See examples/example.py for a more detailed usage example.**
<br/><br/>

Import the PCA9685 class:

`from RPiPCA9685 import RPiPCA9685`
<br/><br/>

Create a PCA9685 object:

`pca9685 = RPiPCA9685.PCA9685(i2c_address, i2c_port_num)`
<br/><br/>

Set the PWM frequency:

`pca9685.set_frequency(frequency)`
<br/><br/>

You can set the pulse width on a specific channel:

`pca9685.set_pwm(channel, 1200)`
<br/><br/>

You can set the duty cycle on the specific channel:

`pca9685.set_duty_cycle(channel, 67)`

