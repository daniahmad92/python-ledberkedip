#!C:\Python27\python
import pyfirmata
import time

port='COM4'
board=pyfirmata.Arduino(port)
ledpin= 13

#fugsi untuk inisialisasi
def setup():
    board.digital[ledpin].mode=pyfirmata.OUTPUT
#fungsi utama
def main():
    while True:
        board.digital[ledpin].write(1) #menyalakan led
        time.sleep(1)# jeda 1 detik
        board.digital[ledpin].write(0) #mematikan led
        time.sleep(1)
    board.exit()
# memanggil fungsi setup dan main
if __name__== '__main__':
    setup()
    main()
