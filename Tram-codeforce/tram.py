n = int(input())
answer = 0
current_passengers = 0

for _ in range(n):
    exit, enter = map(int, input().split(" "))
    current_passengers += enter - exit
    answer = max(answer, current_passengers)

print(answer)
