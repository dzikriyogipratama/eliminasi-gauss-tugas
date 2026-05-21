import numpy as np

print("="*50)
print("  ELIMINASI GAUSS - HARGA MAKANAN")
print("="*50)

n = int(input("\nJumlah variabel (2/3): "))
A = []
b = []

print("\nMASUKKAN PERSAMAAN:")
for i in range(n):
    print(f"\nPersamaan {i+1}:")
    baris = []
    for j in range(n):
        baris.append(float(input(f"  x{j+1}: ")))
    b.append(float(input("  Hasil: ")))
    A.append(baris)

x = np.linalg.solve(A, b)

print("\n" + "="*50)
print("HASIL:")
for i in range(n):
    print(f"  x{i+1} = {x[i]:.0f}")
print("="*50)