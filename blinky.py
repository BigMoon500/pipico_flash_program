import machine
import utime

led_pin = machine.Pin(25, machine.Pin.OUT)  # GPIO Pin 25 for the LED

# Figures out how fast and long to bink for based on the inputed values
def blink_led(flash_speed, flash_duration):
    while True:
        if flash_duration <= 0:
            break
        led_pin.on()
        utime.sleep(0.5 / flash_speed)
        led_pin.off()
        utime.sleep(0.5 / flash_speed)
        flash_duration = flash_duration - (1 / flash_speed)

# Prompts how many times the light should blink per second
def get_flash_speed():
    while True:
        try:
            speed = float(input("Enter the number of blinks per second: "))
            if speed > 0:
                return int(speed)
            else:
                print("Invalid input. Please enter a positive value.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")  

# Prompts how long the light should be blinking for
def get_flash_duration():
    while True:
        try:  
            time = float(input("Enter how long to blink for: "))
            if time > 0:
                return int(time)
            else:
                print("Invalid input. Please enter a positive value.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")  

# Converts the inputed values to be used by the first part of the program
while True:
    current_speed = get_flash_speed()
    current_duration = get_flash_duration()
    print("Blinks per second: {} - Blink time: {}".format(current_speed, current_duration))
    blink_led(current_speed, current_duration)
