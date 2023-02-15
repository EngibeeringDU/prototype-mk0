from machine import Timer, Pin

led = machine.Pin(25, machine.Pin.OUT)

timer = Timer()

def blink(timer):
    led.toggle()
    
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)