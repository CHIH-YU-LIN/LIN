player_height = float(input("請輸入球員身高(公尺):"))
player_weight = float(input("請輸入球員體重(公斤):"))
player_bmi = player_weight / player_height**2
bmi_label = None
if player_bmi > 30:
    bmi_label = 'Obese'
if player_bmi <= 30 and player_bmi > 25:
    bmi_label = 'Overweight'
if player_bmi <= 25 and player_bmi > 18.5:
    bmi_label = 'Normal weight'
if player_bmi <= 18.5:
    bmi_label = 'Underweight'
print(player_bmi)
print(bmi_label)


player_height = float(input("請輸入球員身高(公尺):"))
player_weight = float(input("請輸入球員體重(公斤):"))
player_bmi = player_weight / player_height**2
bmi_label = None
if player_bmi > 30:
    bmi_label = 'Obese'
if player_bmi <= 30 and player_bmi > 25:
    bmi_label = 'Overweight'
if player_bmi <= 25 and player_bmi > 18.5:
    bmi_label = 'Normal weight'
if player_bmi <= 18.5:
    bmi_label = 'Underweight'
print(player_bmi)
print(bmi_label)

user_int = int(input("請輸入一個正整數:"))
if user_int % 3 == 0:
    print("Fizz")
if user_int % 5 == 0:
    print("Buzz")

user_int = int(input("請輸入一個正整數:"))
if user_int % 3 == 0:
    print("Fizz")
if user_int % 5 == 0:
    print("Buzz")

user_int = int(input("請輸入一個正整數:"))
if user_int % 3 == 0:
    print("Fizz")
if user_int % 5 == 0:
    print("Buzz")

user_int = int(input("請輸入一個正整數:"))
if user_int % 15 == 0:
    print("Fizz Buzz")
elif user_int % 5 == 0:
    print("Buzz")
elif user_int % 3 == 0:
    print("Fizz")
else:
    print(user_int)

x = int(input("請輸入起始的整數:"))
y = int(input("請輸入終止的整數:"))
i = x # start
while i <= y: # stop
    # task
    if i % 2 == 1:
        print(i)
    i += 1 # step