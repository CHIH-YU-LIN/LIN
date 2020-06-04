city = input("請輸入您所在的城市：")
weather = input("請輸入現在的天氣：")
print("我在{}，天氣{}".format(city, weather))

id_last_digit = input("請輸入您身分證字號的尾數：")
id_last_digit = int(id_last_digit)
print(id_last_digit)
print(type(id_last_digit))
modulo = id_last_digit % 2
ans = modulo == 1
print(ans)