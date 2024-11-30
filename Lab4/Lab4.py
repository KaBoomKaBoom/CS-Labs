import random

# Permutation tables for DES
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# Shift schedule
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def left_shift(bits, shift):
    return bits[shift:] + bits[:shift]


def apply_permutation(bits, table):
    return ''.join(bits[i - 1] for i in table)


def generate_round_key(k_plus, round_index):
    # Step 1: Apply PC1 to the 64-bit key to reduce it to 56 bits
    permuted_key = apply_permutation(k_plus, PC1)
    print(f"Key after PC1 permutation (56 bits): {permuted_key}\n")

    # Step 2: Split into two halves (C and D)
    c, d = permuted_key[:28], permuted_key[28:]
    print(f"Initial C0: {c}")
    print(f"Initial D0: {d}\n")

    # Step 3: Perform left shifts as per the shift schedule
    for i in range(round_index):
        c = left_shift(c, SHIFT_SCHEDULE[i])
        d = left_shift(d, SHIFT_SCHEDULE[i])
        print(f"After round {i + 1} shift:")
        print(f"C{i + 1}: {c}")
        print(f"D{i + 1}: {d}\n")

    # Step 4: Combine C and D after the final shift
    combined_key = c + d
    print(f"Combined key after final shift (56 bits): {combined_key}\n")

    # Step 5: Apply PC2 to derive the 48-bit round key
    round_key = apply_permutation(combined_key, PC2)
    print(f"Round Key K{round_index} after PC2 permutation (48 bits): {round_key}\n")

    return round_key


def main():
    # Input: K+ (64-bit key with parity bits)
    user_input = input("Enter 64-bit K+ (leave blank to generate randomly): ")
    if not user_input:
        k_plus = ''.join(random.choice('01') for _ in range(64))
        print(f"Generated random K+: {k_plus}")
    else:
        k_plus = user_input.strip()
        if len(k_plus) != 64 or not all(c in '01' for c in k_plus):
            print("Invalid input! Please provide a 64-bit binary string.")
            return

    # Input: Round index
    try:
        round_index = int(input("Enter round index (1-16): "))
        if not 1 <= round_index <= 16:
            raise ValueError("Round index out of range!")
    except ValueError as e:
        print(e)
        return

    # Compute the round key
    round_key = generate_round_key(k_plus, round_index)
    print(f"Final Round Key K{round_index}: {round_key}")


if __name__ == "__main__":
    main()
