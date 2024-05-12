speed = 12

def on_button_pressed_a():
    global speed
    speed += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global speed
    speed += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.clear_screen()
    pins.servo_write_pin(AnalogPin.P0, 6+(7 * speed))
    y = speed // 5
    x = speed % 5
    led.plot(x, y)
    
basic.forever(on_forever)
