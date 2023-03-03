n = int(input())
shirt_sizes = input().split()
m = int(input())
requests = input().split()

def convert_sizes(size):
    if size == 'S':
        return 1000
    elif size == 'M':
        return 1000 + 1
    elif size == 'L':
        return 1000 + 2
    else:
        last_char = size[-1]
        rest = size[:-1]
        #check what is the last
        if last_char == 'L':
            return 1002 + len(rest)
        elif last_char == 'S':
            return 1000 - len(rest)


shirt_sizes = [convert_sizes(s) for s in shirt_sizes]

# Sort T-shirt sizes in ascending order
shirt_sizes.sort()

# Process the requests
for request in requests:
    size = convert_sizes(request)
    i = 0
    while i < len(shirt_sizes) and size > shirt_sizes[i]:
        i += 1
    if i == len(shirt_sizes):
        print('No')
        break
    shirt_sizes = shirt_sizes[i:]
    print(shirt_sizes, "t-shirt", i, "i")
else:
    print('Yes')