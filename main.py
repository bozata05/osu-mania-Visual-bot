from pynput import mouse

amount = int(input("Enter number >> "))
coords = []

def on_click(x, y, button, pressed):
    global amount
    if pressed and button == mouse.Button.left and amount > 0:
        amount -= 1
        coords.append((x, y))
    if amount == 0:
        return False

with mouse.Listener(on_click=on_click) as listener:
    listener.join()

print(coords)