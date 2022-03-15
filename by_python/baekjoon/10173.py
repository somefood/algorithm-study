while True:
    words = input()
    if words == "EOI":
        break
    if "nemo" in words.lower():
        print("Found")
    else:
        print("Missing")
