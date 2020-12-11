from sugarcube import Volume, Mass, Sugar

print((4 * Volume.cup).to(Volume.gallon))

print((2 * Volume.cup * Sugar).to(Mass.gram))
