n = int(input())
flag = False
for _ in range(n):

    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        flag = True
        break
if not flag:
    print(f"All numbers are even.")
