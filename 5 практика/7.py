def F(prev):
    answer = 0
    while prev != 0:
        next = int(input())
        if next != 0 and prev < next:
            answer += 1
        prev = next
    print(answer)
print(F(3))