a = 5
b = 10

# Step 2: Print original values
print("Before swapping:")
print("a =", a, "b =", b)
temp = a
a = b
b = temp

# Step 4: Print values after first swap
print("After swapping with temp variable:")
print("a =", a, "b =", b)

# Step 5: Swap again using Python shortcut (a, b = b, a)
a, b = b, a

# Step 6: Print values after second swap
print("After swapping again with one-line method:")
print("a =", a, "b =", b)

key_words = {1 : 'abcd',
             2 : 'avbd',
             3 : 'ebbf'}
print(key_words[1])