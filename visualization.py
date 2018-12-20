import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_path = './dataset_diabetes/diabetic_data.csv'


df = pd.read_csv(data_path)
# print(df.head())
# print(df.iloc[0])
age_count = {}


def readmitted_to_num(readm):
    if readm == 'NO':
        return 0
    elif readm == '<30':
        return 1
    elif readm == '>30':
        return 2

# def make_count_dict(dataframe, feature):


for index, row in df.iterrows():
    age = row['age']
    label = readmitted_to_num(row['readmitted'])
    if age in age_count.keys():
        age_count[age][label] += 1
    else:
        age_count[age] = [0, 0, 0]
        age_count[age][label] = 1
name_list = age_count.keys()
cnt0 = []
cnt1 = []
cnt2 = []
for age in name_list:
    cnt0.append(age_count[age][0])
    cnt1.append(age_count[age][1])
    cnt2.append(age_count[age][2])

width = 0.2
ind = np.arange(len(name_list))
print(ind)

fig, ax = plt.subplots()
# rects0 = ax.bar(ind - width, cnt0, width, color='SkyBlue', label='NO')
# rects1 = ax.bar(ind, cnt1, width, color='IndianRed', label='<30')
# rects2 = ax.bar(ind + width, cnt2, width, color='Violet', label='>30')
rects0 = ax.plot(ind, cnt0, color='SkyBlue', label='NO')
rects1 = ax.plot(ind, cnt1, color='IndianRed', label='<30')
rects2 = ax.plot(ind, cnt2, color='Violet', label='>30')


ax.set_ylabel('Total')
ax.set_title('Label count group by age')
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


# autolabel(rects0, 'left')
# autolabel(rects1, 'center')
# autolabel(rects2, 'right')

plt.savefig('age.png')
plt.show()



