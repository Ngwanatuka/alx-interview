#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ UTF-8 Validation """
    def validate_byte(byte, num_bytes):
        if num_bytes == 0:
            if byte >> 7 == 0:
                return True
            elif byte >> 5 == 0b110:
                return validate_byte(data.pop(0), 1)
            elif byte >> 4 == 0b1110:
                return validate_byte(data.pop(0), 2)
            elif byte >> 3 == 0b11110:
                return validate_byte(data.pop(0), 3)
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            return validate_byte(data.pop(0), num_bytes - 1)

    while len(data) > 0:
        if not validate_byte(data.pop(0), 0):
            return False

    return True
