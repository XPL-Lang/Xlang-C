import os

print("XLang 0.0.1 Alpha")
print("type `help@' for more info")
while True:
  request = input(">>> ")
  if request.startswith("PRINT >"):
    print = request.replace("PRINT  >","",1)
    print(print)
  elif request.startswith("external@"):
    com = request.replace("external@","",1)
    import os
    os.system(com
