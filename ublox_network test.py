#SARA R4 attempt
import serial
import u-blox
import socket
import sys 

#Create Module, serial port name is ?
module = SaraR4Module(serial_port='/dev/tty.usbmodem14111')
#Configure Module, AT command is ?
module._at_action('AT+CFUN=1')
#Connect to network, operator is ?
module.connect(operator=24001, roaming=True)
#Socket, port is ?, testdata is ?, ip address is ?
sock = module.create_socket(socket_type='UDP', port=1337)
sock.sendto(b'mytestdata', ('195.34.89.241', 7))
sock.close()
module.update_radio_statistics()
print(module.radio_rsrq)
print(module.radio_rsrq)