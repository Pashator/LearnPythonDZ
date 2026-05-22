# ЮНУСОВ ПАВЕЛ ИИАД 1

s = input("Введите строку: ")

first = s.find('h')
last = s.rfind('h')

between = s[first+1:last]

reversed_between = between[::-1]

print("Развёрнутая последовательность между первым и последним h:", reversed_between)
