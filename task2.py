import numpy as np


def heapify(shipments, warehouse, n, i, col):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Logic: If child is larger than parent, update largest
    if left < n and shipments[left, col] > shipments[largest, col]:
        largest = left

    if right < n and shipments[right, col] > shipments[largest, col]:
        largest = right

    if largest != i:
        # Swap rows in BOTH matrices using NumPy slicing
        shipments[[i, largest]] = shipments[[largest, i]]
        warehouse[[i, largest]] = warehouse[[largest, i]]
        # Recursively heapify the affected sub-tree
        heapify(shipments, warehouse, n, largest, col)


def heap_sort(shipments, warehouse, col):
    n = len(shipments)

    # 1. Build Max Heap (Rearrange matrix)
    for i in range(n // 2 - 1, -1, -1):
        heapify(shipments, warehouse, n, i, col)

    # 2. Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        shipments[[i, 0]] = shipments[[0, i]]
        warehouse[[i, 0]] = warehouse[[0, i]]
        # Call heapify on the reduced heap
        heapify(shipments, warehouse, i, 0, col)

    return shipments, warehouse


# --- Data Setup ---

# Shipment Matrix: [Distance (km), Weight (kg), Delivery Priority (1-5)]
shipment_data = np.array([
    [850, 200, 3],  # ID 0
    [120, 50, 1],  # ID 1
    [430, 150, 5],  # ID 2
    [990, 400, 2],  # ID 3
    [310, 80, 4],  # ID 4
    [550, 220, 3],  # ID 5
    [720, 110, 1],  # ID 6
    [215, 300, 2]  # ID 7
])

# Warehouse Matrix: [Aisle Number, Bin Number, Staff ID]
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

# Let's sort by Distance (Column 0)
sorted_ships, sorted_ware = heap_sort(shipment_data.copy(), warehouse_data.copy(), 0)

print("--- SHIPMENTS SORTED BY DISTANCE ---")
print("Distance | Weight | Priority")
print(sorted_ships)

print("\n--- SYNCED WAREHOUSE LOCATIONS ---")
print("Aisle | Bin | Staff ID")
print(sorted_ware)