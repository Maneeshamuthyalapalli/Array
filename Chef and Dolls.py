def find_missing_doll():
    t = int(input())
    for _ in range(t):
        n = int(input())
        doll_count = {}
        for _ in range(n):
            doll_type = int(input())
            doll_count[doll_type] = doll_count.get(doll_type, 0) + 1
        for doll_type, count in doll_count.items():
            if count % 2 != 0:
                print(doll_type)
                break
find_missing_doll()
