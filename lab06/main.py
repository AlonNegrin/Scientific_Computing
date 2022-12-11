import numpy as np
import matplotlib.pyplot as plt


# u - vector
# e - a group of vectors
# returns - the projection of u on e.
def projection(u, e):
    return sum(np.inner(u, i) * i for i in e)


def run():
    fig, axs = plt.subplots(1, 3, subplot_kw={'projection': '3d'})
    d3_d1(axs[0])
    d3_d2(axs[1])
    d3sphere_d2(axs[2])
    fig.savefig('figure.png')
    plt.show()


def d3_d1(ax):
    u = np.array([5, 3, 2])
    es = np.array([[1, 0, 0]])
    proj = projection(u, es)
    ax.plot([0, 10, 0], [0, 0, 0])
    ax.set_title("3d -> 1d")
    ax.scatter(proj[0], u[0])


def d3_d2(ax):
    u = np.array([5, 3, 2])
    es = np.array([[1, 0, 0], [0, 1, 0]])
    proj = projection(u, es)
    x = np.arange(0, 10, 0.1)
    y = np.arange(0, 10, 0.1)
    x, y = np.meshgrid(x, y)
    z = np.zeros(x.shape)
    ax.plot_surface(x, y, z, color='green', alpha=0.5)
    ax.set_title("3d -> 2d")
    ax.scatter([proj[0], u[0]],
               [proj[1], u[1]],
               [proj[2], u[2]])


def d3sphere_d2(ax):
    es = np.array([[1, 0, 0], [0, 1, 0]])

    r = 2
    x0, y0, z0 = 5, 5, 5

    xSpace = np.arange(0, 10, 0.1)
    ySpace = np.arange(0, 10, 0.1)
    theta, fi = np.meshgrid(xSpace, ySpace)

    x = x0 + (r * np.sin(theta) * np.cos(fi))
    y = y0 + (r * np.sin(theta) * np.sin(fi))
    z = z0 + (r * np.cos(theta))

    x_hat = []
    y_hat = []
    z_hat = []

    for i, j, k in zip(x, y, z):
        for n in range(len(i)):
            hat = projection(np.array([i[n], j[n], k[n]]), es)
            x_hat.append(hat[0])
            y_hat.append(hat[1])
            z_hat.append(hat[2])

    x1 = np.arange(0, 10, 0.1)
    y1 = np.arange(0, 10, 0.1)
    x1, y1 = np.meshgrid(x1, y1)
    z1 = np.zeros(x1.shape)

    ax.plot_surface(x1, y1, z1, color='green', alpha=0.5)
    ax.scatter(x_hat, y_hat, z_hat, marker='.', color='red')
    ax.plot_wireframe(x, y, z)
    ax.set_title("3d sphere -> 2d")


if __name__ == '__main__':
    run()
