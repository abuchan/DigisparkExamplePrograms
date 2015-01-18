#/usr/bin/python

#
# Written for PyUSB 1.0 (w/libusb 1.0.3)
#


import usb, sys # 1.0 not 0.4
sys.path.append("..")

from arduino.usbdevice import ArduinoUsbDevice

def digiusb_init():
   try:
      return ArduinoUsbDevice(idVendor=0x16c0, idProduct=0x05df)
   except:
      sys.exit("No DigiUSB Device Found")

def digiusb_send(device, data):
  for d in data:
    device.write(d)
  
if __name__ == "__main__":
  theDevice = digiusb_init()


  try:
    user_input = sys.argv[1]+"\n"
  except:
    exit("No data to send")
  
  digiusb_send(theDevice, map(ord,user_input))
