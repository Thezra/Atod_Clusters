# Read and transform input
N, M = map(int, input().split())
connections = [list(map(int, input().split())) for _ in range(M)]
zeros_list = [0] * N
results_list = []

# Initial values and firts call to check left
def check_clusters():
    n = 1
    count = 0
    row = 0
    check_left(n, count, row)

# Check position and existence of each number
def check_left(n, count, row):
    if (n == connections[row][0]):
        count += 1
        zeros_list.pop()
        n += 1
        if row + 1 < M:
            row += 1
            check_left(n, count, row)
        else:
            results_list.append(count)
            zeros_list.pop()
            answer = sorted(results_list + zeros_list)
            showAns(answer)
    else:
        results_list.append(count)
        count = 0
        zeros_list.pop()
        n += 1
        check_left(n, count, row)

# Print the numbers one by one
def showAns(answer):
    print(len(answer))
    for num in answer:
        print(num)

check_clusters()