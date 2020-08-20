import board
import digitalio
 
led = digitalio.DigitalInOut(board.C0)
led.direction = digitalio.Direction.OUTPUT
 
button = digitalio.DigitalInOut(board.C1)
button.direction = digitalio.Direction.INPUT
 
while True:
    led.value = button.value