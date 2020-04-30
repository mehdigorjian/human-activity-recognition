import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def fig_plot(x_param, y_param, label_name):
    plt.style.use("ggplot")
    plt.figure()
    plt.plot(x_param, y_param, label="train_loss")
    plt.title("Time | Label")
    plt.xlabel("time")
    plt.ylabel(label_name)
    plt.legend(loc="lower left")
    plt.savefig('timeLable.jpg')