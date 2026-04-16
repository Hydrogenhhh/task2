# Logistics Data Sorter - Heap Sort Implementation
## Video Link: https://youtu.be/n1lISAj98iU

A specialized implementation of the **Heap Sort** algorithm using Python and NumPy, designed to synchronize dual-matrix datasets. This tool is ideal for logistics scenarios where shipment metrics must remain linked to specific warehouse metadata during sorting.

## Features

- **Dual-Matrix Synchronization**: Automatically keeps `warehouse_data` in sync while sorting `shipment_data`.
- **In-Place Sorting**: Efficiently sorts data with $O(1)$ auxiliary space complexity (excluding NumPy overhead).
- **NumPy Optimized**: Utilizes fancy indexing for rapid row swapping across multi-dimensional arrays.
- **Complexity**: Guarantees $O(n \log n)$ performance for best, average, and worst-case scenarios.

## Algorithm Overview: Heap Sort

The system organizes data by treating the array as a Binary Heap.

1. **Build Heap**: Rearranges the input arrays into a Max-Heap structure where the parent node is always greater than its children.
2. **Extraction**: Repeatedly swaps the maximum element (root) with the last element of the heap and shrinks the heap size.
3. **Heapify**: Restores the heap property after each swap to ensure the next largest value moves to the root.

## Getting Started

### Prerequisites
- Python 3.x
- NumPy

### Installation
```bash
pip install numpy
