# cook your dish here

l, w, h, a = map(int, input().split())

volCuboid = l * w * h 
volCube = a**3

if volCuboid > volCube :
    print("Cuboid")
elif volCube > volCuboid :
    print("Cube")
else:
    print("Equal")
