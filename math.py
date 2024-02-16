
def shift(x, n):
  shifted_x = [1] * len(x)
  for i in range(len(x)):
    shifted_index = (i + n) % len(x)
    shifted_x[shifted_index] = x[i]
  return shifted_x

# Example usage:
original_list = [1, 2, 3, 4, 5]
shifted_list = shift(original_list, 4)

print("Original list:", original_list)
print("Shifted list:", shifted_list)