from PyQt5 import QtWidgets
from controller import MainWindow_controller
import sys
from PyQt5.QtCore import QTimer
import threading
import time
import serial

def read_value(window):
    ser = serial.Serial('COM4', 9600,timeout=0.1)
    while True:
        data = ser.readline()
        print(data)
        if 50< len(data) < 60:
            data = str(data).split("~")[1]
            print('in')
            v_1 = str(data).split(":")[1]
            v_2 = str(data).split(":")[3]
            v_3 = str(data).split(":")[5]
            print(f'v_1:{v_1},v_2:{v_2},v_3:{v_3}')
            window.send_signal(v_1,v_2,v_3)

        else:
            print("data is out")


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    thread1 = threading.Thread(target=read_value, args=(window,))
    thread1.start()

    sys.exit(app.exec_())
