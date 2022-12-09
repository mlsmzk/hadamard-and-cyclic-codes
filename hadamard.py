import numpy as np

def hadamard(n, mem):
    # Sylvester construction for Hadamard matrices
    if n in mem:
        return mem[n]
    if n == 0:
        mem[n] = np.array([[1]])
        return mem[n]
    else:
        mem[n] = np.kron(np.array([[1, 1], [1,-1]]), hadamard(n-1,mem))
        return mem[n]

def check_dot_products(m):
    # m = np.matrix.tolist(mat)
    for i,row in enumerate(m):
        for j,row2 in enumerate(m):
            if j > i:
                print(f"Dot product of row {i+1} with row {j+1} is {np.dot(row, row2)}")

def encode_message_vector(x, hm):
    res = []
    for row in hm:
        print(np.dot(x, row))
        res.append(np.dot(x, row))
    # print(f"Your encoded vector is {res}")
    return np.array(res)

if __name__ == "__main__":
    mem = {}
    print(hadamard(1, mem))
    print(hadamard(2, mem))
    a = hadamard(7, mem)
    print(a)
    # check_dot_products(a)
    # encode_message_vector(np.array([0,0,1,1]), a)
