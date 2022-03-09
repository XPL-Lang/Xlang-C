import os

print("XLang Developer Release")
print("type `help@' for more info")
while True:
  request = input("xlang>")
  if request.startswith("+"):
    print = request.replace("PRINT>","",1)
    print(print)
  elif request.startswith("external@"):
    com = request.replace("external@","",1)
    print(f"> {com}")
    os.system(com)
  else:
    print(f"Error: undefined Xscript '{request}'")
