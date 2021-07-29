def sort(arr: list) -> list:
    stack = [[0, len(arr) - 1]]
    while stack:
        cur = stack.pop()

        if cur[0] < cur[1]:
            left, right, pivot = cur[0], cur[1], arr[(cur[0] + cur[1]) // 2]

            while left <= right:
                left = next(
                    ind for ind, val in enumerate(arr[left:], left) if val >= pivot
                )
                right = next(
                    -ind
                    for ind, val in enumerate(arr[: right + 1][::-1], -right)
                    if val <= pivot
                )
                if left <= right:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1

            stack.extend([[left, cur[1]], [cur[0], left - 1]])
    return arr


if __name__ == "__main__":
    import random

    assert sort(random.sample(range(20), k=20)) == list(range(20))
