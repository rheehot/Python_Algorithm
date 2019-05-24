text = input()
count = 0
for i in range(len(text)):
    print(text[i],end='')
    count += 1
    if count%10==0:
        print()