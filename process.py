import matplotlib.pyplot as plt
from labellines import labelLines
import numpy as np
from scipy.integrate import odeint
import logging

from functions import pend
from radar_diagram import RadarDiagram
from utils import lines

data_sol = []
logger = logging.getLogger('uvicorn.error')


def fill_diagrams(data, initial_equations, restrictions):
    radar1 = RadarDiagram()
    radar1.draw('./static/images/diagram.png', initial_equations, u_list,
                "Характеристики системы в начальный момент времени", restrictions)
    radar1.draw('./static/images/diagram2.png', data[int(len(data) / 4)], u_list,
                "Характеристики системы в 1 четверти", restrictions)
    radar1.draw('./static/images/diagram3.png', data[int(len(data) / 2)], u_list,
                "Характеристики системы во 2 четверти", restrictions)
    radar1.draw('./static/images/diagram4.png', data[int(len(data) / 4 * 3)], u_list,
                "Характеристики системы в 3 четверти", restrictions)
    radar1.draw('./static/images/diagram5.png', data[-1, :], u_list,
                "Характеристики системы в последний момент времени", restrictions)


def create_graphic(t, data):
    fig, axs = plt.subplots(figsize=(20, 12))
    plt.subplot(111)
    for i in range(12):
        plt.plot(t, list(map(lambda elem: 0 if elem < 0 else elem, data[:, i])), color=lines[i][0],
                 linestyle=lines[i][1], label=f"X{i + 1}")
    plt.xlabel("t, время", fontsize=16)
    plt.ylabel("Характеристики", fontsize=16)
    labelLines(plt.gca().get_lines(), fontsize=16)
    plt.xlim([0, 1])
    plt.ylim(bottom=0)
    plt.legend(loc='lower right', bbox_to_anchor=(1, 1), labelspacing=0.1, fontsize=16)
    plt.tight_layout()
    fig.savefig('./static/images/figure.png', bbox_inches='tight')


def cast_to_float(initial_equations, faks, equations, restrictions):
    for i in range(len(initial_equations)):
        initial_equations[i] = float(initial_equations[i])

    for i in range(len(faks)):
        for j in range(len(faks[i])):
            faks[i][j] = float(faks[i][j])

    for i in range(len(equations)):
        for j in range(len(equations[i])):
            equations[i][j] = float(equations[i][j])

    for i in range(len(restrictions)):
        restrictions[i] = float(restrictions[i])

    return initial_equations, faks, restrictions


def process(initial_equations, faks, equations, restrictions):
    global data_sol

    cast_to_float(initial_equations, faks, equations, restrictions)
    t = np.linspace(0, 1)
    data_sol = odeint(pend, initial_equations, t, args=(faks, equations, restrictions))
    create_graphic(t, data_sol)
    fill_diagrams(data_sol, initial_equations, restrictions)


u_list = [
    "Численность группировки сил, участвующих в аварийно-спасательных работах",
    "Количество жилых домов, разрушенных и поврежденных в результате наводнения",
    "Численность населения, эвакуированного из зоны затопления",
    "Количество погибших",
    "Протяженность железных и автомобильных дорог, оказавшихся в зоне затопления",
    "Количество промышленных предприятий в зоне наводнения",
    "Количество транспортных средств, участвующих в аварийно-спасательных работах",
    "Численность населения в зоне затопления",
    "Площадь сельскохозяйственных угодий, охваченных наводнением",
    "Количество погибших сельскохозяйственных животных",
    "Ущерб основным производственным фондам в зоне затопления",
    "Ущерб оборотным производственным фондам в зоне затопления"
]
