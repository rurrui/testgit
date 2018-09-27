with open('hello.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    print(repr(data))
    with open('hello2.txt', 'w', encoding='utf-8') as f2:
        f2.write(data)
with open('city.jpg', 'rb') as f1:
    data = f1.read()
    print(repr(data))
    print(data)
    with open('city2.jpg', 'wb') as f3:
        f3.write(data)
