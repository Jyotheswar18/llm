items = []
while True:
    try:
        line = input()
        if not line:
            break
        items.append(tuple(line.split(",")))
    except:
        break

items.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))
print(items)
