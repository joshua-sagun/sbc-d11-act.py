arr = ["D","S","M","R","A","E"]

print(f"Unsorted: {arr}")

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            print(f"process: {arr}")
        print(f"process: {arr}")
print("Final sort is:", arr)