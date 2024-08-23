import string,time

a = 'hello world'

b = []

for i in a:
    for j in string.ascii_lowercase:
        if j == i:
            b.append(j)
            break
        time.sleep(0.2)
        print(''.join(b),j)
    print()


