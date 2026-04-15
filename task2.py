import numpy as np

def heapify(shipments, warehouse, n, i, col):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and shipments[left, col] > shipments[largest, col]:
        largest = left

    if right < n and shipments[right, col] > shipments[largest, col]:
        largest = right

    if largest != i:
        shipments[[i, largest]] = shipments[[largest, i]]
        warehouse[[i, largest]] = warehouse[[largest, i]]
        heapify(shipments, warehouse, n, largest, col)

def heap_sort(shipments, warehouse, col):
    n = len(shipments)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(shipments, warehouse, n, i, col)

    for i in range(n - 1, 0, -1):
        shipments[[i, 0]] = shipments[[0, i]]
        warehouse[[i, 0]] = warehouse[[0, i]]
        heapify(shipments, warehouse, i, 0, col)
    
    return shipments, warehouse

shipment_data = np.array([
    [850, 200, 3],
    [120, 50,  1],
    [430, 150, 5],
    [990, 400, 2],
    [310, 80,  4],
    [550, 220, 3],
    [720, 110, 1],
    [215, 300, 2]
])

warehouse_data = np.array([
    [10, 101, 5001],
    [12, 205, 5002],
    [15, 309, 5003],
    [11, 402, 5004],
    [14, 505, 5005],
    [10, 601, 5006],
    [13, 708, 5007],
    [12, 802, 5008]
])

sorted_ships, sorted_ware = heap_sort(shipment_data.copy(), warehouse_data.copy(), 0)

print("Shipments sorted by distance:")
print(sorted_ships)
print("Synced warehouse locations:")
print(sorted_ware)
