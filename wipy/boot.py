# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

# enable REPL duplication on UART0 (the one accessible via the expansion board)
import os
import machine
uart = machine.UART(0, 115200)
os.dupterm(uart)

