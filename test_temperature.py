import unittest

from temperature import Temperature

class testTemperature(unittest.TestCase):
    def testInput(self):
        self.assertRaises(ValueError, Temperature, None)

    def testMoreInput(self):
        arguments = (2,2,2)
        self.assertRaises(ValueError, Temperature, *arguments)

    def testOuput(self):
        testFahrein = (4 - 32) * 5/9 + 273.15
        self.assertEqual(Temperature(5).kelvin, 5)
        self.assertEqual(Temperature(celcius=3).kelvin, 276.15)
        self.assertEqual(Temperature(fahrenheit=4).kelvin, testFahrein)

    def testNegInput(self):
        self.assertRaises(ValueError, Temperature, -1)