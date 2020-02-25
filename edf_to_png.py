import os
from pathlib import Path
import numpy as np
import mne
import matplotlib
import matplotlib.pyplot as plt



dirname = "edf_png/"
time_window = 1


# グラフを描写する際に使うカラーコード
color_list = []
for cname in matplotlib.colors.cnames.values():
    color_list.append(cname)

# 画像ファイルを作成するフォルダをカレントディレクトリに作成
os.makedirs(dirname, exist_ok = True)

# edfdataフォルダ内のedfファイルを読み込み
edf_dir = Path("/Users/keisuke/b3_task/edfdata")
edf = mne.io.read_raw_edf(next(edf_dir.glob("*.edf")),
                          preload = True)
edf.drop_channels('PHOTIC PH')
sfreq = float(edf.info["sfreq"])
ntimes = float(edf.n_times)

#画像作成
def export():
    data = edf.get_data()
    for count in range(int(ntimes/(sfreq * time_window))):
    # for count in range(10):
    #     data = edf.get_data(start = int(edf.time_as_index(count)),
    #                 stop = int(edf.time_as_index(count + 1)))
        for i, ch in enumerate(edf.ch_names):
            plt.plot(data[i, count * time_window * 250 : (count + 1) * time_window * 250],
                label = ch, color = color_list[i])

        plt.savefig(dirname + "file_{0}.png".format(count + 1))
        plt.close()

export()
