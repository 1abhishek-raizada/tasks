from pynput.mouse import Button,Controller

mouse=Controller()
print('the current position is {0}'.format(mouse.position))
mouse.position=(20,310)
print('current  position is {0}'.format(mouse.position))
mouse.move(500,120)
print('current  position is {0}'.format(mouse.position))
