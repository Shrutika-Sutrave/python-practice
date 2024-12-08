def lcm(a, b):
    larger = max(a, b)  # Start with the larger number
    while True:  # Infinite loop
        if larger % a == 0 and larger % b == 0:  # Check if 'larger' is divisible by both
            return larger  # If true, return 'larger' as the LCM and exit the loop
        larger += 1  # If not, increment 'larger' and check again
result = lcm(12,15)
print(result)

