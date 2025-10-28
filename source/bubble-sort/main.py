def bubble_sort(d):
    for i in range(len(d)):
        for j in range(len(d) - i -1):
            if d[j] > d[j + 1]: d[j], d[j + 1] = d[j + 1], d[j]

        print(f"[sort] {d}")

    return d

if __name__ == '__main__':
    data = [ 6, 21, 27, 17, 24, 14, 1, 10, 20, 29, 8, 16 ]

    sorted_data = bubble_sort(data.copy())

    print(f"[main] {data} -> {sorted_data}")