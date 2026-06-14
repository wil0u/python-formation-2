import operations_basiques.operations as ob
import sys

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    result = ob.multiplier(a, b)

    print(f"Multiplication de {a} et {b} : {result}")
    