import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_path = './dataset_diabetes/diabetic_data.csv'
label_name = 'readmitted'


def readmitted_to_num(readm):
    if readm == 'NO':
        return 0
    elif readm == '<30':
        return 1
    elif readm == '>30':
        return 2


def make_count_dict(dataframe, feature_name, label_name):
    feature_count = {}
    missing_cnt = 0
    for index, row in df.iterrows():
        feature = row[feature_name]
        if feature == '?':
            missing_cnt += 1
            continue
        label = readmitted_to_num(row[label_name])
        if feature in feature_count.keys():
            feature_count[feature][label] += 1
        else:
            feature_count[feature] = np.zeros(3)
            feature_count[feature][label] = 1
    return feature_count


def plot_label_count_by_feature(feature_count, feature_name, mode='plot'):
    name_list = sorted(feature_count.keys())
    cnt0 = []
    cnt1 = []
    cnt2 = []
    for feature in name_list:
        cnt0.append(feature_count[feature][0])
        cnt1.append(feature_count[feature][1])
        cnt2.append(feature_count[feature][2])

    width = 0.2
    ind = np.arange(len(name_list))
    print(ind)

    fig, ax = plt.subplots()
    if mode == 'bar':
        rects0 = ax.bar(ind - width, cnt0, width, color='SkyBlue', label='NO')
        rects1 = ax.bar(ind, cnt1, width, color='IndianRed', label='<30')
        rects2 = ax.bar(ind + width, cnt2, width, color='Violet', label='>30')
    elif mode == 'plot':
        rects0 = ax.plot(ind, cnt0, color='SkyBlue', label='NO')
        rects1 = ax.plot(ind, cnt1, color='IndianRed', label='<30')
        rects2 = ax.plot(ind, cnt2, color='Violet', label='>30')
    else:
        rects0 = ax.scatter(ind, cnt0, color='SkyBlue', label='NO')
        rects1 = ax.scatter(ind, cnt1, color='IndianRed', label='<30')
        rects2 = ax.scatter(ind, cnt2, color='Violet', label='>30')

    ax.set_ylabel('Total')
    ax.set_title('Label count group by ' + feature_name)
    ax.set_xticks(ind)
    ax.set_xticklabels(name_list)
    ax.legend()

    def autolabel(rects, xpos='center'):
        """
        Attach a text label above each bar in *rects*, displaying its height.

        *xpos* indicates which side to place the text w.r.t. the center of
        the bar. It can be one of the following {'center', 'right', 'left'}.
        """

        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                    '{}'.format(height), ha=ha[xpos], va='bottom')

    if mode == 'bar':
        autolabel(rects0, 'left')
        autolabel(rects1, 'center')
        autolabel(rects2, 'right')

    plt.savefig('results/label_count_by_feature_' + feature_name + '.png')
    plt.show()


df = pd.read_csv(data_path)
# print(df.head())
# print(df.iloc[0])
feature_names = df.columns
print(feature_names)
for feature_name in feature_names[15:]:
    feature_count_dict = make_count_dict(df, feature_name, label_name)
    plot_label_count_by_feature(feature_count_dict, feature_name)
