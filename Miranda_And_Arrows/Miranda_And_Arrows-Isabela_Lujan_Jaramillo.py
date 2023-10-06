# Read and transform input
N, K = map(int, input().split())
distances = list(map(int, input().split()))

# Initial values and firts call to compare
def find_max():
    n = 0
    current_max = 0
    compare(n, current_max)

# Compare the sums taking max+1 amount of numbers
def compare(n, current_max):
    ans = sum(distances[n:current_max+n+1])
    if (ans <= K):
        current_max += 1
        check_n(n, current_max)
    else:
        n += 1
        check_n(n,current_max)

# Check if the calls are still inside the range of the list
def check_n(n, current_max):
    print(n, N)
    if (current_max+n < N):
        compare(n, current_max)
    else:
        print(current_max)

find_max()