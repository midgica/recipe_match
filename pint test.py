from pint import UnitRegistry
ureg = UnitRegistry()

def convert(msrmt, unit, new_unit):
    return ((msrmt * getattr(ureg, unit)).to(getattr(ureg, new_unit)))

print("msrmt: 6")
print("unit: cup")
print("new_unit: gallon")

conversion = convert(6, "cup", "gallon")
print(conversion)


