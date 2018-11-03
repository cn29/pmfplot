import matplotlib.pyplot as plt
import numpy as np
import csv


def readCSV(file_name, plot_num):
    print(1)
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_count = 29*2
        line_count = 0
        tickers = []
        data_matrix = np.zeros([plot_num, row_count], dtype=float)
        for row in csv_reader:
            tickers.append(row[0])
            for i in range(1, plot_num+1):
                data_matrix[i-1][line_count] = float(row[i])
            line_count += 1
        return tickers, data_matrix, line_count


def plotData(tickers, data_matrix, plot_name, figure_title, y_label):
    x = np.arange(1,len(data_matrix[0])+1,1)
    num_plots = len(data_matrix)
    f, axarr = plt.subplots(num_plots, sharex=True, sharey=True)
    f.text(0.04, 0.5, y_label, va='center', rotation='vertical')
    f.suptitle(figure_title)
    for i in range(num_plots):
        axarr[i].bar(x, data_matrix[i], width=0.75)

    i = 0
    for ax in axarr.flat:
        # ax.set(xlabel='x-label', ylabel='y-label')
        ax.set_xticks(x)
        ax.set_xticklabels(tickers)
        ax.set_yscale('log')
        ax.yaxis.set_tick_params(labelsize=8)
        ax.xaxis.set_tick_params(rotation=45, labelsize=8)
        if i == 0:
            ax.xaxis.set_tick_params(labeltop='on')
        i += 1

    # add plot name
    for i in range(num_plots):
        f.text(0.86, 0.19+i*0.132, plot_name[i], ha='right', va='center')

    plt.show()


def spot_select(spot):
    if spot == 'EO':
        file_name = 'EO.csv'
        plot_name = ['Wood burning', 'Traffic/meat cooking', 'EC3', 'Shipping', 'Sea salt/dust', 'Sn', 'Sb']
        figure_title = 'East Oakland'
        y_label = 'Concentration $(\mu g/m^3)$'
        plot_num = 7
    elif spot == 'SP':
        file_name = 'SP.csv'
        plot_name = ['Wood burning/meat cooking', 'Traffic', 'Shipping', 'Sea salt/dust', 'Sn', 'Sb']
        figure_title = 'San Pablo'
        y_label = 'Concentration $(\mu g/m^3)$'
        plot_num = 6
    else:
        file_name = 'LA.csv'
        plot_name = ['Wood burning/meat cooking', 'Traffic', 'Shipping', 'Sea salt/dust', 'Sn', 'Sb']
        figure_title = 'Los Angeles'
        y_label = 'Concentration $(\mu g/m^3)$'
        plot_num = 6
    return file_name, plot_name, figure_title, y_label, plot_num

if __name__ == '__main__':
    file_name, plot_name, figure_title, y_label, plot_num = spot_select('LA')

    tickers, data_matrix, line_count = readCSV(file_name, plot_num)
    plotData(tickers, data_matrix[:,:line_count], plot_name[::-1], figure_title, y_label)