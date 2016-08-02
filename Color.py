# coding: utf-8
# DrawBot requiress floats from 0–1, so I use a class to adapt 8-bit hex (#ffffff) formats and provide properties like bg.r, bg.g, bg.b
import math
class Hex:
    def __init__(self, hexCode):
        hexa = hexCode.strip('#')
        alphaGiven = len(hexa) % 4 == 0
        divisor = 4 if (alphaGiven == True) else 3
        bitDepth = int(len(hexa) / divisor)

        self.r = self.hexToFloat(hexa, 0, bitDepth)
        self.g = self.hexToFloat(hexa, 1, bitDepth)
        self.b = self.hexToFloat(hexa, 2, bitDepth)
        self.a = self.hexToFloat(hexa, 3, bitDepth)
        self.tuple = tuple((self.r, self.g, self.b, self.a))

    def hexToFloat(self, hexa, offset, bitDepth):
        hexValue = hexa[(offset*bitDepth):(offset*bitDepth + bitDepth)]
        floatValue = (int(hexValue, 16) / (16.0 ** bitDepth - 1)) if hexValue else 1
        return floatValue
