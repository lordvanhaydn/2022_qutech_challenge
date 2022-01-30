base_a = [0, 1, 1, 1, 0, 0, 1, 0]
base_b = [1, 0, 1, 1, 1, 0, 1, 0]

raw_key = [1, 0, 0, 1, 0, 1, 0, 1]

final_key = []
for i, (a, b) in enumerate(list(zip(base_a, base_b))):
    if a == b:
        final_key.append(raw_key[i])
