from unit_converter.converter import convert, converts
import pint

u = pint.UnitRegistry()
Q = u.Quantity
num = 10
speed = Q(num,'grad')
# num = speed.to('in')

print(speed.units)
# print(num)

