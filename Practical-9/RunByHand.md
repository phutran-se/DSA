

### 1. MergeSort
**MergeSort** is a **divide-and-conquer** sorting algorithm. It divides the array into smaller subarrays, sorts them, and then merges them back into a sorted array.

#### How it works:
1. **Divide**: Split the array into two halves recursively until each subarray has only one element (a single-element array is considered sorted).
2. **Conquer**: Merge the sorted subarrays into larger sorted arrays, ensuring ascending order.
3. **Combine**: Continue merging until the entire array is sorted.

#### Time Complexity:
- **Best, Average, Worst Case**: \(O(N \log N)\).
- **Stable**: Yes (preserves the relative order of equal elements).
- **In-place**: No (requires a temporary array for merging).

#### Example with array `[5, 2, 8, 1, 9]`:
**Step 1: Divide**
- Initial array: `[5, 2, 8, 1, 9]`
- Split into two halves:
  - Left: `[5, 2]`
  - Right: `[8, 1, 9]`
- Split further:
  - `[5, 2]` → `[5]` and `[2]`
  - `[8, 1, 9]` → `[8]` and `[1, 9]`
  - `[1, 9]` → `[1]` and `[9]`
- Result: Subarrays `[5]`, `[2]`, `[8]`, `[1]`, `[9]` (each is sorted as it has one element).

**Step 2: Merge**
- Merge `[5]` and `[2]`:
  - Compare: 5 > 2 → Take 2 first, then 5.
  - Result: `[2, 5]`
- Merge `[8]` and `[1, 9]`:
  - Merge `[1]` and `[9]`: 1 < 9 → `[1, 9]`.
  - Merge `[8]` and `[1, 9]`: Compare 8 with 1 (take 1), 8 with 9 (take 8, then 9) → `[1, 8, 9]`.
- Merge `[2, 5]` and `[1, 8, 9]`:
  - Compare pairs: 2 with 1 (take 1), 2 with 8 (take 2), 5 with 8 (take 5), then take 8, 9.
  - Result: `[1, 2, 5, 8, 9]`.

**Final Result**: `[1, 2, 5, 8, 9]`

#### Illustration:
```
[5, 2, 8, 1, 9]
   /         \
[5, 2]     [8, 1, 9]
 /  \       /     \
[5] [2]   [8]   [1, 9]
                /   \
               [1]  [9]
Merge: [2, 5]    [1, 8, 9]
       \         /
       [1, 2, 5, 8, 9]
```

---

### 2. QuickSort
**QuickSort** is also a **divide-and-conquer** algorithm, but instead of splitting the array evenly, it selects a **pivot** and partitions the array into two parts: elements less than the pivot and elements greater than the pivot. It then recursively sorts the two parts.

#### How it works:
1. **Choose a pivot**: Can be the first, last, middle, random element, or median of three elements.
2. **Partition**: Rearrange the array so that:
   - Elements less than the pivot are on the left.
   - Elements greater than the pivot are on the right.
   - The pivot is placed in its final sorted position.
3. **Recurse**: Apply QuickSort to the left and right subarrays.

#### Time Complexity:
- **Best Case**: \(O(N \log N)\) (pivot splits array evenly).
- **Average Case**: \(O(N \log N)\).
- **Worst Case**: \(O(N^2)\) (pivot is the smallest/largest element, e.g., sorted array with first pivot).
- **Stable**: No (may swap equal elements).
- **In-place**: Yes (requires minimal extra memory).

#### Example with array `[5, 2, 8, 1, 9]`:
Assume we choose the **first element as pivot** (as in `quickSort` from your `DSAsorts.py`).

**Step 1: First iteration**
- Array: `[5, 2, 8, 1, 9]`
- Pivot: 5
- Partition:
  - Compare elements with 5:
    - 2 < 5 → Move 2 to the left.
    - 8 > 5 → Keep 8 on the right.
    - 1 < 5 → Move 1 to the left.
    - 9 > 5 → Keep 9 on the right.
  - Result: `[2, 1, 5, 8, 9]` (5 is in its final position, index 2).
- Subarrays:
  - Left: `[2, 1]` (less than 5).
  - Right: `[8, 9]` (greater than 5).

**Step 2: Recurse on left subarray `[2, 1]`**
- Pivot: 2
- Partition:
  - 1 < 2 → Move 1 to the left.
  - Result: `[1, 2]` (2 is in its final position).
- Subarrays:
  - Left: `[]` (empty).
  - Right: `[]` (empty).
- Stop as subarrays are empty.

**Step 3: Recurse on right subarray `[8, 9]`**
- Pivot: 8
- Partition:
  - 9 > 8 → Keep 9 on the right.
  - Result: `[8, 9]` (8 is in its final position).
- Subarrays:
  - Left: `[]` (empty).
  - Right: `[9]` (single element, already sorted).
- Stop.

**Final Result**: `[1, 2, 5, 8, 9]`

#### Illustration:
```
[5, 2, 8, 1, 9]
  |pivot=5
[2, 1] [5] [8, 9]
  |pivot=2    |pivot=8
[1] [2]      [8] [9]
  |          |
[1, 2]      [8, 9]
    \        /
  [1, 2, 5, 8, 9]
```

#### QuickSort Variants:
- **QuickSortMedian3**: Chooses the pivot as the median of the first, middle, and last elements (e.g., median of 5, 8, 9 is 8). Reduces the chance of worst-case scenarios.
- **QuickSortRandom**: Chooses a random pivot, achieving good average performance.

---

### Comparison of MergeSort and QuickSort
| Feature             | MergeSort                     | QuickSort                     |
|---------------------|-------------------------------|-------------------------------|
| **Time Complexity** | \(O(N \log N)\) (always)      | \(O(N \log N)\) average, \(O(N^2)\) worst case |
| **Stable**          | Yes                           | No                            |
| **In-place**        | No (needs temporary array)    | Yes (minimal extra memory)    |
| **Practical Performance** | Consistent, but slower than QuickSort on random data | Faster on random data, but slow in worst case |
| **Use Cases**       | Large datasets, needs stability | Random data, prioritizes speed |
