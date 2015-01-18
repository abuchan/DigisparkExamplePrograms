from send import *


def digiusb_pwm(d,value):
  if value < 0:
    value = -value
    direction = 1
  else:
    direction = 0

  if value > 255:
    value = 255
  
  digiusb_send(d,[direction, value])

if __name__ == '__main__':
  d = digiusb_init()

  ui = '0'

  while ui[0].lower() != 'q':
    ui = raw_input('Enter command:')
    
    try:
      digiusb_pwm(d,int(ui))
      
    except:
      pass
