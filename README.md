# RPi_PCA9685
A Python package for the Raspberry Pi to control the PCA9685 16 Channel 12-bit PWM driver.

![Image of PCA9685](https://github.com/Jgunde/RPi_PCA9685/blob/master/PCA9685%20Image.jpg)


## Dependencies:
pip install smbus


## Usage:

**See example.py for a more detailed usage example.**


Import the PCA9685 class:

`from RPi_PCA9685.PCA9685 import PCA9685`


Create a PCA9685 object:

`pca9685 = PCA9685(i2c_address, i2c_port_num)`


Set the PWM frequency:

`pca9685.set_frequency(frequency)`


You can set the pulse width on a specific channel:

`pca9685.set_pwm(channel, 1200)`


You can set the duty cycle on the specific channel:

`pca9685.set_duty_cycle(channel, 67)`



## Donate
If you'd like to help support my projects, please consider donating:
<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_donations" />
<input type="hidden" name="business" value="GYE58HUYS2PJS" />
<input type="hidden" name="item_name" value="To fund my ongoing engineering projects" />
<input type="hidden" name="currency_code" value="USD" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1" />
</form>


