# Pascal's Triangle in Python

Pascal's Triangle is a triangular array of numbers where each number is the sum of the two numbers directly above it. In this project, we will discuss how to create Pascal's Triangle using Python.

## Algorithm

To create Pascal's Triangle, we can use a nested loop. Here's the algorithm:

1. Ensure the function return an empty list  if n <= 0
2. Initialize the triangle. starts with the first row [1]
3. Generate each row
    - start each row with [1] and use the last row `previous_row`. to compute the middle elements
      - .
4. Print `triangle` to display Pascal's Triangle.

## Implementation

Here's the Python code to create Pascal's Triangle:

```python

```

## Example Output

For example, if the user enters `5` as the number of rows, the output will be:

```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

This represents Pascal's Triangle with 5 rows.
