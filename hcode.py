from hadamard import *
import numpy as np
import time

if __name__ == "__main__":
    d = {}
    lookup = {}
    reverse_lookup = []
    m = hadamard(5, d)
    # print(type(m))
    mn = np.negative(m)
    # print(mn)
    # print(type(mn))
    cw = np.concatenate((m, mn))
    # print(lookup)
    for k in range(64):
        # encoding: each grayscale value is assigned a row of the hadamard matrix or the negative hadamard matrix
        lookup[k] = cw[k]
        reverse_lookup.append(cw[k])
    # print(reverse_lookup)
    # RGB to Grayscale

    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    def rgb2gray(rgb):
        return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

    img = mpimg.imread('chocolatechipcookie3.png')
    gray = rgb2gray(img)
    # print(gray)
    new = [[0 for j in range(len(gray[i]))] for i in range(len(gray))]
    for i in range(len(gray)):
        for j in range(len(gray[i])):
            new[i][j] = round(63 * gray[i][j])
    
    dims = (len(new), len(new[0]))
    veclen = dims[0]*dims[1]
    new = np.reshape(new, veclen)
    # print(new)
    # print(np.array(new).shape)
    plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    plt.title("Grayscale image before transmission")
    plt.show()
    # time.sleep(7)
    # probability of an error

    import random
    def noisify(vec, p=0.34):
        for idx in range(len(vec)):
            flip = random.random()
            if flip <= p:
                vec[idx] = -1*vec[idx]

        return vec

    message = []
    received = []
    for idx in range(len(new)):
        pixel = lookup[new[idx]]
        message.append(pixel)
        received.append(noisify(pixel))

    final = []
    for vec in received:
        for i, row in enumerate(cw):
            if np.dot(row, vec) > 16:
                final.append(i)
                break

    final = np.array(final)
    final = np.reshape(final, dims)
    final = final/63
    # print(final)
    
    plt.imshow(final, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    plt.title("Grayscale image after transmission")
    plt.show()
    