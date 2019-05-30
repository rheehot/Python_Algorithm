n = int(input()); copy_n = n; count = 0; minus_count = 1
while copy_n > 0:
    copy_n -= minus_count
    count += 1
    minus_count += 1
print(str(n//count)+'/'+str(n%count))