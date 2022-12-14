from pprint import pprint
import numpy as np
import pandas as pd

def hadamard(n):
    return hadamard_rec(n, {})

def hadamard_rec(n, mem):
    # Sylvester construction for Hadamard matrices
    if n in mem:
        return mem[n]
    if n == 0:
        mem[n] = np.array([[1]])
        return mem[n]
    else:
        mem[n] = np.kron(np.array([[1, 1], [1,-1]]), hadamard_rec(n-1,mem))
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

def decode_message_vector(x, hm):
    # given a vector x and corresponding codewords matrix C=[H;-H],
    # find which codeword the received vector is nearest to decode it
    c = np.vstack((hm, np.negative(hm))) # stack -H and H
    x[x==0] = -1
    # c[c == -1] = 0 # replace all -1s with 0s 
    n = c.shape[1] # n is the horiz dimension of this array's shape
    for i, row in enumerate(c):
        # if the dot product of two vectors > n/2, then that is
        # the intended vector
        if np.dot(x, row) > (n/2):
            return i
        if np.dot(x, row) == (n/2):
            print("Error detected but can't be corrected")
            return -1
    return -1

if __name__ == "__main__":
    mem = {}
    pprint(hadamard(1))
    pprint(hadamard(2))
    a = hadamard(3)
    pprint(pd.DataFrame(a))
    #check_dot_products(a)
    print("Sending codeword at row 1 with no errors")
    message_vector = np.array([1,0,1,0,1,0,1,0]) # perfect vector
    print(decode_message_vector(message_vector, a))
    print("sending codeword at row 6 with no errors")
    message_vector = np.array([1,1,0,0,0,0,1,1])
    print(decode_message_vector(message_vector, a))
    print("Sending codeword at row 1 with 1 error")
    message_vector = np.array([1,1,1,0,1,0,1,0]) # one error
    print(decode_message_vector(message_vector, a))
    print("Sending codeword at row 1 with 2 errors")
    message_vector = np.array([0,1,1,0,1,0,1,0]) # two error
    print(decode_message_vector(message_vector, a))
