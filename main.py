import matplotlib.pyplot as plt
import numpy as np


def plot_markers(xpoints,ypoints):
    # plt.plot(xpoints, ypoints, 'o:b')
    # plt.plot(xpoints, ypoints, marker='o', ms=20)  # ms = marker size. long version is markersize.
    # plt.plot(xpoints, ypoints, marker='o', ms=20, mec='r', mfc='c')  # mec = markeredgecolor, mfc = markerfacecolor
    # use hexadecimal color values
    # plt.plot(xpoints, ypoints, marker='o', ms=20, mec='#4CAF50', mfc='#4CAF50')  # mec = markeredgecolor, mfc = markerfacecolor
    # Mark each point with the color named "hotpink":
    plt.plot(xpoints, ypoints, marker='o', ms=20, mec='hotpink', mfc='hotpink')

# note: you can also mention onlt ypoints, and the xpoints will be the index of the ypoints - 1,2...n
# linestyle shortcut is ls, dotted can be written as :, and dashed as --, dashdot as -., and solid as -, none as ''
def plot_line(ypoints):
    # plt.plot(ypoints, linestyle='dotted')
    # plt.plot(ypoints, linestyle='dashed')
    # plt.plot(ypoints, linestyle='')
    # line color parameter - color or c, values similar to those of the marker edge or face color.
    # plt.plot(ypoints, linestyle='dashed', c='r')
#     linewidth parameter - lw, values are float values that indicate the width of the line, each point is 1.33 pixels
    plt.plot(ypoints, linestyle='dashed', c='r', lw=15)


# multiple lines can be achieved by either calling the plot function multiple times, or by passing multiple lines to the plot function
def plot_multiple_lines():
    x1_array = np.array([1, 2, 3, 4])
    y1_array = np.array([3, 8, 1, 10])
    x2_array = np.array([1, 2, 3, 4])
    y2_array = np.array([6, 2, 7, 11])

    # plt.plot(x1_array, y1_array)
    # plt.show()
    # plt.plot(x1_array, y1_array, x2_array, y2_array)
    # same as:
    plt.plot(x1_array, y1_array)
    plt.plot(x2_array, y2_array)
    plt.show()


def plot_line_with_labels_title():
    font1 = {'family': 'serif', 'color': 'g', 'size': 20}
    x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
    y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
    plt.plot(x, y)
    # use param loc to set title position
    plt.title("the plot title", fontdict=font1, loc='center')
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.show()


# its possible to setup line properties for the grid: grid(color = 'color', linestyle = 'linestyle', linewidth = number)
def plot_with_grid():
    x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
    y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
    plt.title("the plot title")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.plot(x, y)
    plt.grid(axis='both', color='g', linestyle='--', linewidth=0.5)
    plt.show()


if __name__ == '__main__':
    # xpoints = np.array([1, 2, 6, 8])
    # ypoints = np.array([3, 8, 1, 10])
    # plot_line(ypoints)
    # plt.show()
    # plot_multiple_lines()
    # plot_line_with_labels_title()
    plot_with_grid()