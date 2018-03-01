import numpy as np

def crc16(data: bytes):

    data = bytearray(data)
    poly = 0x8408
    crc = 0xFFFF
    for b in data:
        cur_byte = 0xFF & b
        for _ in range(0, 8):
            if (crc & 0x0001) ^ (cur_byte & 0x0001):
                crc = (crc >> 1) ^ poly
            else:
                crc >>= 1

            cur_byte >>= 1

    crc = (~crc & 0xFFFF)
    crc = (crc << 8) | ((crc >> 8) & 0xFF)
    print(np.uint16(crc))




crc_calc = crc16(12)
#int(bin(crc_calc)[2:])

print("{0:b}".format(56928))
print("{0:b}".format(crc_calc))




