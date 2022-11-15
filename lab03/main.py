from typing import List
import random
import matplotlib.image
import matplotlib.pyplot as plt
import numpy as np


# ----------- Ex 1 ---------------#
def get_random_word(length: int = 4, abc: List[str] = ['A', 'T', 'G', 'C']) -> str:
    return ''.join(random.choices(abc, k=length))


def count():
    words = {}
    for i in range(257):  # 4^4+1
        word = get_random_word()
        words[word] = words.get(word, 0) + 1
    max_word = max(words.values())
    for word, count in words.items():
        if count == max_word:
            return word, count


print(count())

# ----------- Ex 2 ---------------#

img = matplotlib.image.imread("colors.png")
print(type(img))
print(np.shape(img))

plt.imshow(img)
plt.show()

plt.imshow(img[:, :, 0], cmap='gray')
plt.show()
plt.imshow(img[:, :, 1], cmap='gray')
plt.show()
plt.imshow(img[:, :, 2], cmap='gray')
plt.show()
plt.imshow(img[:, :, 3], cmap='gray')
plt.show()

# alpha changed
img[:, :, 3] = np.random.uniform(size=(1000, 1000))
plt.imshow(img)
plt.show()

# no alpha
img = img[:, :, :3]
plt.show()

# invert
plt.imshow(img[::-1, :, :])
plt.show()

# mirror
plt.imshow(img[:, ::-1, :])
plt.show()

# only red arrow to the left
plt.imshow(np.transpose(img[:, :, 0]), cmap='gray')
plt.show()

# 13
img2 = np.zeros((1000, 1000, 4))
img2[:, :, :3] = img[:, :, :3]

img2[:, :, 0] = np.transpose(img[:, :, 0])

# 14
img2[:, :, 1] = img[:, ::-1, 1]

# 15
img2[:, :, 2] = img[::-1, :, 2]

plt.imshow(img2)
plt.show()

# 18
plt.imshow(img[1:, :, :] - img[:-1, :, :])
plt.show()

# 19
plt.imshow(img[:, 1:, :] - img[:, :-1, :])
plt.show()

# 20
plt.imshow(img[1:, 1:, :] - img[:-1, :-1, :])
plt.show()

# 21
plt.imshow((img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3, cmap='gray')
plt.show()

# 22
plt.imshow(img[:, :, 0] @ img[:, :, 1] @ img[:, :, 2])
plt.show()
