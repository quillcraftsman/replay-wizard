# """
# Main module
# """
# from pynput import keyboard
#
#
# def on_press(key, f):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#         f.write(f'{key.char} pressed\n')
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))
#
#
# def on_release(key, f):
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False
#     print('{0} released'.format(
#         key))
#     f.write(f'{key.char} released\n')
#
#
# def capture(name):
#     file_name = f'{name}.sequence'
#     with open(file_name, 'w', encoding='utf-8') as f:
#         on_press_handler = lambda key: on_press(key, f)
#         on_release_handler = lambda key: on_release(key, f)
#
#         with keyboard.Listener(
#                 on_press=on_press_handler,
#                 on_release=on_release_handler) as listener:
#             listener.join()
#
#     # ...or, in a non-blocking fashion:
#     # listener = keyboard.Listener(
#     #     on_press=on_press,
#     #     on_release=on_release)
#     # listener.start()
