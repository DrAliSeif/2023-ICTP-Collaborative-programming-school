#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate a figure of a noisy sinusoidal wave pattern.
"""

import numpy as np
import matplotlib.pyplot as plt
from funcs import get_random_numbers


def main():
    savefig = False
    dpi = 80
    figFormat = "pdf"
    plt.rcParams.update({"font.size": 18})
    num_of_points = 400

    noise = get_random_numbers(num_of_points, 0.5)

    xs = np.linspace(0, 4 * np.pi, num_of_points)
    ys = np.sin(xs) + noise

    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.plot(xs, ys)

    if savefig == True:
        fig.savefig(f"Fig1.{figFormat}", dpi=dpi, transparent=False, format=figFormat)


if __name__ == "__main__":
    main()
