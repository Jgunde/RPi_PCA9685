# ----- User defined constants go below ------

i2c_address = 0x40  # This is the default I2C address for the PCA9685.
i2c_port_num = 1    # The I2C port is 0 for the Raspberry Pi 1 and 1 for all future models.
frequency = 50      # 50Hz is good for servos.
channel = 8         # This is the channel number that the servo is connected to (0 - 15).

# ----------------------------

from RPi_PCA9685.PCA9685 import PCA9685

pca9685 = PCA9685(i2c_address, i2c_port_num)
pca9685.set_frequency(frequency)

# ----------------------------


from time import sleep


# You can set the pulse width on a specific channel. This is needed for controlling servos.

pca9685.set_pwm(channel, 1000)  # sets the pulse width to 1000 microseconds (usually the minimum pulse width for a servo)
sleep(2)
pca9685.set_pwm(channel, 1500)  # sets the pulse width to 1500 microseconds
sleep(2)
pca9685.set_pwm(channel, 2000)  # sets the pulse width to 2000 microseconds (usually the maximum pulse width for a servo)
sleep(2)

pca9685.set_pwm(channel, 0)  # turns off the PWM output



# You can also set the duty cycle. This is useful for controlling DC motors or LEDs.

pca9685.set_duty_cycle(channel, 0)  # sets the duty cycle to 0% (the minimum duty cycle)
sleep(2)
pca9685.set_duty_cycle(channel, 50)  # sets the duty cycle to 50%
sleep(2)
pca9685.set_duty_cycle(channel, 100)  # sets the duty cycle to 100% (the maximum duty cycle)
sleep(2)


