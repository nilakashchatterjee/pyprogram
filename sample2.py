import sys
if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")
ords = [73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
print("".join(chr(hex(o)) for o in ords))