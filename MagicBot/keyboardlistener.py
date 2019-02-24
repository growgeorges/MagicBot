from pynput import keyboard

class myKeyboardListener:
    def __init__(self, monAppli):
        self.monAppli = monAppli

   # Collect events until released
    def startTheListener(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()


    def on_press(self, key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

        if key == keyboard.Key.pause:
            if self.monAppli.isStartClicked:
                self.monAppli.button_stop_clicked()
            else:
                self.monAppli.button_start_clicked()

        if self.monAppli.isWaitingforCursorPos and key == keyboard.Key.space:
            self.monAppli.resolve_cursor_pos()



    def on_release(self, key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

