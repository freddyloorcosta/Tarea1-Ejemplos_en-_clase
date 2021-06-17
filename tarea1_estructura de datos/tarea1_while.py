vocal = input("Digite vocal:")
while vocal not in('a','e','i','o','u'):
    if vocal == '.':
        break
    vocal = input("vocal:")
print('Su vocal o punto es:{}'.format(vocal))

