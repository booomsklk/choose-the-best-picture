# [方法1，……方法8，图片序号，选择最优图片，最优图对应的方法，选择次优图片，次优图对应的方法，选择第三优图片，第三优图对应的方法]
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import re
import os

# choice为用户的选择，由0-7组成。表示选择的图像序号
choice_1 = []
choice_2 = []
choice_3 = []
# 记录图像对与用户选择的列表
list_b = []
# 获取测试者的用户名
name = []
age = []
gender = []

step = 0


# 第一个窗口：获取用户名
def get_information():
    name.append(En1.get())
    age.append(En2.get())
    gender.append(En3.get())
    root0.destroy()

root0 = Tk()
# 昵称不要有空格
label = Label(root0, text='请输入您的昵称:', anchor='c').grid(row=0)
En1 = Entry(root0)
En1.grid(row=0, column=1)
label = Label(root0, text='请输入您的年龄:', anchor='c').grid(row=1)
En2 = Entry(root0)
En2.grid(row=1, column=1)
label = Label(root0, text='请输入您的性别:', anchor='c').grid(row=2)
En3 = Entry(root0)
En3.grid(row=2, column=1)
Button(root0, text='确定', anchor='c', width=6, height=1, command=get_information).grid(row=3, column=1)
root0.mainloop()


# 根据方法与原始图片名，找到该方法对应的图片名
def pic_name(var, pic):
    file_list = os.listdir(project_folder + '\\' + var)
    pic += '_'
    for file_name in file_list:
        if pic in file_name:
            return file_name
    return 'error'
    '''
    return {
        'BiGAN': 'step9299_img_' + pic + '.png',
        'cr': pic + '_0.50_cr.png',
        'lg': pic + '_0.50_lg.png',
        'multiop': pic + '_0.50_multiop.png',
        'osa': pic + '_0.50_osa.png',
        'qp': pic + '_0.50_qp.png',
        'sc': pic + '_0.50_sc.png',
        'scl': pic + '_0.50_scl.png',
        'sv': pic + '_0.50_sv.png',
        'warp': pic + '_0.50_warp.png'
    }.get(var, 'error')  # 'error'为默认返回值，可自设置
'''


# "关闭" 按钮对应的指令
def on_exit():
    root.destroy()
    sys.exit()


# "next"按钮对应的指令
def next_window():
    root.destroy()


# “查看各图对应方法”按钮对应的指令
def reveal_label():
    if label_m1['text'] == "图1" and label_m2['text'] == "图2" and label_m3['text'] == "图3" and label_m4['text'] == "图4" and label_m5['text'] == "图5" and label_m6['text'] == "图6" and label_m7['text'] == "图7" and label_m8['text'] == "图8":
        label_m1['text'] = "图1：" + method_dict[list_b[step][0]]
        label_m2['text'] = "图2：" + method_dict[list_b[step][1]]
        label_m3['text'] = "图3：" + method_dict[list_b[step][2]]
        label_m4['text'] = "图4：" + method_dict[list_b[step][3]]
        label_m5['text'] = "图5：" + method_dict[list_b[step][4]]
        label_m6['text'] = "图6：" + method_dict[list_b[step][5]]
        label_m7['text'] = "图7：" + method_dict[list_b[step][6]]
        label_m8['text'] = "图8：" + method_dict[list_b[step][7]]
    else:
        label_m1['text'] = "图1"
        label_m2['text'] = "图2"
        label_m3['text'] = "图3"
        label_m4['text'] = "图4"
        label_m5['text'] = "图5"
        label_m6['text'] = "图6"
        label_m7['text'] = "图7"
        label_m8['text'] = "图8"


# 在窗口上重置图片显示的大小，防止图像过大
def resize(w_box, h_box, picture):
    width, height = picture.size  # 获取图像的原始大小
    f1 = 1.0 * w_box / width
    f2 = 1.0 * h_box / height
    factor = min([f1, f2])
    width = int(width * factor)
    height = int(height * factor)
    return picture.resize((width, height), Image.ANTIALIAS)


# 用字典为所有方法编号
project_folder = '.\RetargetMe_dataset'
path_methods = project_folder
method_list = os.listdir(path_methods)
method_list = [w for w in method_list if not re.search('[\.]', w)]
method_list.remove('original_image')
method_dict = {}
for i in range(1, len(method_list) + 1):
    method_dict[i] = method_list[i - 1]
# print(method_dict)

# 用字典为所有图片编号
original_folder = '\original_image'
path_pictures = project_folder + original_folder
picture_list = os.listdir(path_pictures)
picture_list = [re.sub('\.png', '', w) for w in picture_list]
picture_dict = {}
for i in range(1, len(picture_list) + 1):
    picture_dict[i] = picture_list[i - 1]
# print(picture_dict)

method_num = len(method_list)  # 方法数量
picture_num = len(picture_list)  # 图片数量

for k in range(1, picture_num + 1):
    # 将8种方法打乱顺序
    tmp = []
    for i in range(1, method_num + 1):
        tmp += [i]
    random.shuffle(tmp)
    # 每张图片都要经过tmp的组合进行比较，用list_b来记录，元素格式为：[方法1, …… 方法8, 图片序号]
    list_b += [tmp + [k]]

random.shuffle(list_b)

# for i in range(len(list_b)):
#     print(list_b[i])


note_s = '''用户对图1至图8进行偏好选择，依据：图像是否自然、美观、无明显的扭曲变形，以及完整地保持了原始图像中的重要内容'''


while step < len(list_b):
# for i in range(len(list_b)):
    path_original_pic = project_folder + original_folder + "\\" + picture_dict[list_b[step][8]] + ".png"
    path_1_pic = project_folder + "\\" + method_dict[list_b[step][0]] + "\\" + pic_name(method_dict[list_b[step][0]],
                                                                                       picture_dict[list_b[step][8]])
    path_2_pic = project_folder + "\\" + method_dict[list_b[step][1]] + "\\" + pic_name(method_dict[list_b[step][1]],
                                                                                        picture_dict[list_b[step][8]])
    path_3_pic = project_folder + "\\" + method_dict[list_b[step][2]] + "\\" + pic_name(method_dict[list_b[step][2]],
                                                                                        picture_dict[list_b[step][8]])
    path_4_pic = project_folder + "\\" + method_dict[list_b[step][3]] + "\\" + pic_name(method_dict[list_b[step][3]],
                                                                                        picture_dict[list_b[step][8]])
    path_5_pic = project_folder + "\\" + method_dict[list_b[step][4]] + "\\" + pic_name(method_dict[list_b[step][4]],
                                                                                        picture_dict[list_b[step][8]])
    path_6_pic = project_folder + "\\" + method_dict[list_b[step][5]] + "\\" + pic_name(method_dict[list_b[step][5]],
                                                                                        picture_dict[list_b[step][8]])
    path_7_pic = project_folder + "\\" + method_dict[list_b[step][6]] + "\\" + pic_name(method_dict[list_b[step][6]],
                                                                                        picture_dict[list_b[step][8]])
    path_8_pic = project_folder + "\\" + method_dict[list_b[step][7]] + "\\" + pic_name(method_dict[list_b[step][7]],
                                                                                        picture_dict[list_b[step][8]])

    if os.path.exists(path_original_pic) and os.path.exists(path_1_pic) and os.path.exists(path_2_pic) and os.path.exists(path_3_pic) and os.path.exists(path_4_pic) and os.path.exists(path_5_pic) and os.path.exists(path_6_pic) and os.path.exists(path_7_pic) and os.path.exists(path_8_pic) :
        root = Tk()

        # 加载原图
        load_0 = Image.open(path_original_pic)
        load_0 = resize(350, 350, load_0)
        render_0 = ImageTk.PhotoImage(load_0)
        img_0 = Label(root, image=render_0)
        img_0.image = render_0
        img_0.place(x=10, y=0)  # 设置图片放置位置

        # 加载图1。路径与list_b中的列表项有关
        load_1 = Image.open(path_1_pic)
        load_1 = resize(250, 250, load_1)
        render_1 = ImageTk.PhotoImage(load_1)
        img_1 = Label(root, image=render_1)
        img_1.image = render_1
        img_1.place(x=390, y=0)  # 设置图片放置位置

        # 加载图2。路径与list_b中的列表项有关
        load_2 = Image.open(path_2_pic)
        load_2 = resize(250, 250, load_2)
        render_2 = ImageTk.PhotoImage(load_2)
        img_2 = Label(root, image=render_2)
        img_2.image = render_2
        img_2.place(x=610, y=0)  # 设置图片放置位置

        # 加载图3。路径与list_b中的列表项有关
        load_3 = Image.open(path_3_pic)
        load_3 = resize(250, 250, load_3)
        render_3 = ImageTk.PhotoImage(load_3)
        img_3 = Label(root, image=render_3)
        img_3.image = render_3
        img_3.place(x=830, y=0)  # 设置图片放置位置

        # 加载图4。路径与list_b中的列表项有关
        load_4 = Image.open(path_4_pic)
        load_4 = resize(250, 250, load_4)
        render_4 = ImageTk.PhotoImage(load_4)
        img_4 = Label(root, image=render_4)
        img_4.image = render_4
        img_4.place(x=1050, y=0)  # 设置图片放置位置

        # 加载图5。路径与list_b中的列表项有关
        load_5 = Image.open(path_5_pic)
        load_5 = resize(250, 250, load_5)
        render_5 = ImageTk.PhotoImage(load_5)
        img_5 = Label(root, image=render_5)
        img_5.image = render_5
        img_5.place(x=390, y=280)  # 设置图片放置位置
        
        # 加载图6。路径与list_b中的列表项有关
        load_6 = Image.open(path_6_pic)
        load_6 = resize(250, 250, load_6)
        render_6 = ImageTk.PhotoImage(load_6)
        img_6 = Label(root, image=render_6)
        img_6.image = render_6
        img_6.place(x=610, y=280)  # 设置图片放置位置

        # 加载图7。路径与list_b中的列表项有关
        load_7 = Image.open(path_7_pic)
        load_7 = resize(250, 250, load_7)
        render_7 = ImageTk.PhotoImage(load_7)
        img_7 = Label(root, image=render_7)
        img_7.image = render_7
        img_7.place(x=830, y=280)  # 设置图片放置位置

        # 加载图8。路径与list_b中的列表项有关
        load_8 = Image.open(path_8_pic)
        load_8 = resize(250, 250, load_8)
        render_8 = ImageTk.PhotoImage(load_8)
        img_8 = Label(root, image=render_8)
        img_8.image = render_8
        img_8.place(x=1050, y=280)  # 设置图片放置位置

        label_original = Label(root, text="原始图像：" + picture_dict[list_b[step][8]], width=int(load_0.size[0] / 8), height=1, bg="LightSteelBlue", font=("黑体", 11))
        label_m1 = Label(root, text="图1", width=int(load_1.size[0] / 8), height=1, bg="LightSteelBlue", font=("黑体", 11))
        label_m2 = Label(root, text="图2", width=int(load_2.size[0] / 8), height=1, bg="LightSteelBlue", font=("黑体", 11))
        label_m3 = Label(root, text="图3", width=int(load_3.size[0] / 8), height=1, bg="LightSteelBlue", font=("黑体", 11))
        label_m4 = Label(root, text="图4", width=int(load_4.size[0] / 8), height=1, bg="LightSteelBlue", font=("黑体", 11))
        label_m5 = Label(root, text="图5", width=int(load_5.size[0] / 8), height=1, bg="LightSteelBlue", font=("黑体", 11))
        label_m6 = Label(root, text="图6", width=int(load_6.size[0] / 8), height=1, bg="LightSteelBlue", font=("黑体", 11))
        label_m7 = Label(root, text="图7", width=int(load_7.size[0] / 8), height=1, bg="LightSteelBlue", font=("黑体", 11))
        label_m8 = Label(root, text="图8", width=int(load_8.size[0] / 8), height=1, bg="LightSteelBlue", font=("黑体", 11))
     
        label_original.place(x=12, y=load_0.size[1] + 2)
        label_m1.place(x=392, y=load_1.size[1] + 2)
        label_m2.place(x=612, y=load_2.size[1] + 2)
        label_m3.place(x=832, y=load_3.size[1] + 2)
        label_m4.place(x=1052, y=load_4.size[1] + 2)
        label_m5.place(x=392, y=load_1.size[1] + 30 + load_5.size[1] + 2)
        label_m6.place(x=612, y=load_2.size[1] + 30 + load_6.size[1] + 2)
        label_m7.place(x=832, y=load_3.size[1] + 30 + load_7.size[1] + 2)
        label_m8.place(x=1052, y=load_4.size[1] + 30 + load_8.size[1] + 2)


        # “查看各图对应方法”按钮
        reveal_button = Button(root, text="查看各图对应方法", width=23, height=1, font=("黑体", 11),
                               bg="Azure", command=reveal_label)
        reveal_button.place(x=10, y=load_0.size[1] + 90)


        # 设置窗口的大小
        width = 1263
        height = 640

        #固定窗口位置与大小
        root.geometry("+2+5")
        root.geometry('%dx%d' % (width, height))
        root.title("Choose The Best Picture" + '                                                                                                                                 ' +
                   "Progress: " + str(step) + " / " + str(len(list_b)))    # 显示当前的评分进度


        # 最优、次优、第三的标签
        first_label = Label(root, text="最优：", width=44, height=1, bg="Azure", font=("黑体", 11))
        first_label.place(x=10, y=405)
        second_label = Label(root, text="次优：", width=44, height=1, bg="Azure", font=("黑体", 11))
        second_label.place(x=10, y=454)
        third_label = Label(root, text="第三：", width=44, height=1, bg="Azure", font=("黑体", 11))
        third_label.place(x=10, y=504)


        data_1 = IntVar()
        data_1.set(0)
        # 最优的图像
        pic_1_button_1 = Radiobutton(root, text="1", width=2, height=1, variable=data_1, value=0,
                                  bg="white", font=("黑体", 12))
        pic_2_button_1 = Radiobutton(root, text="2", width=2, height=1, variable=data_1, value=1,
                                   bg="white", font=("黑体", 12))
        pic_3_button_1 = Radiobutton(root, text="3", width=2, height=1, variable=data_1, value=2,
                                   bg="white", font=("黑体", 12))    
        pic_4_button_1 = Radiobutton(root, text="4", width=2, height=1, variable=data_1, value=3,
                                   bg="white", font=("黑体", 12))                       
        pic_5_button_1 = Radiobutton(root, text="5", width=2, height=1, variable=data_1, value=4,
                                   bg="white", font=("黑体", 12))    
        pic_6_button_1 = Radiobutton(root, text="6", width=2, height=1, variable=data_1, value=5,
                                   bg="white", font=("黑体", 12))     
        pic_7_button_1 = Radiobutton(root, text="7", width=2, height=1, variable=data_1, value=6,
                                   bg="white", font=("黑体", 12))    
        pic_8_button_1 = Radiobutton(root, text="8", width=2, height=1, variable=data_1, value=7,
                                   bg="white", font=("黑体", 12))     

        pic_1_button_1.place(x=10, y=425)
        pic_2_button_1.place(x=55, y=425)
        pic_3_button_1.place(x=100, y=425)
        pic_4_button_1.place(x=145, y=425)
        pic_5_button_1.place(x=190, y=425)
        pic_6_button_1.place(x=235, y=425)
        pic_7_button_1.place(x=280, y=425)
        pic_8_button_1.place(x=325, y=425)


        # 次优的图像
        data_2 = IntVar()
        data_2.set(0)        
        pic_1_button_2 = Radiobutton(root, text="1", width=2, height=1, variable=data_2, value=0,
                                  bg="white", font=("黑体", 12))
        pic_2_button_2 = Radiobutton(root, text="2", width=2, height=1, variable=data_2, value=1,
                                   bg="white", font=("黑体", 12))
        pic_3_button_2 = Radiobutton(root, text="3", width=2, height=1, variable=data_2, value=2,
                                   bg="white", font=("黑体", 12))    
        pic_4_button_2 = Radiobutton(root, text="4", width=2, height=1, variable=data_2, value=3,
                                   bg="white", font=("黑体", 12))                       
        pic_5_button_2 = Radiobutton(root, text="5", width=2, height=1, variable=data_2, value=4,
                                   bg="white", font=("黑体", 12))    
        pic_6_button_2 = Radiobutton(root, text="6", width=2, height=1, variable=data_2, value=5,
                                   bg="white", font=("黑体", 12))     
        pic_7_button_2 = Radiobutton(root, text="7", width=2, height=1, variable=data_2, value=6,
                                   bg="white", font=("黑体", 12))    
        pic_8_button_2 = Radiobutton(root, text="8", width=2, height=1, variable=data_2, value=7,
                                   bg="white", font=("黑体", 12))     

        pic_1_button_2.place(x=10, y=475)
        pic_2_button_2.place(x=55, y=475)
        pic_3_button_2.place(x=100, y=475)
        pic_4_button_2.place(x=145, y=475)
        pic_5_button_2.place(x=190, y=475)
        pic_6_button_2.place(x=235, y=475)
        pic_7_button_2.place(x=280, y=475)
        pic_8_button_2.place(x=325, y=475)

        # 第三的图像
        data_3 = IntVar()
        data_3.set(0)
        pic_1_button_3 = Radiobutton(root, text="1", width=2, height=1, variable=data_3, value=0,
                                  bg="white", font=("黑体", 12))
        pic_2_button_3 = Radiobutton(root, text="2", width=2, height=1, variable=data_3, value=1,
                                   bg="white", font=("黑体", 12))
        pic_3_button_3 = Radiobutton(root, text="3", width=2, height=1, variable=data_3, value=2,
                                   bg="white", font=("黑体", 12))    
        pic_4_button_3 = Radiobutton(root, text="4", width=2, height=1, variable=data_3, value=3,
                                   bg="white", font=("黑体", 12))                       
        pic_5_button_3 = Radiobutton(root, text="5", width=2, height=1, variable=data_3, value=4,
                                   bg="white", font=("黑体", 12))    
        pic_6_button_3 = Radiobutton(root, text="6", width=2, height=1, variable=data_3, value=5,
                                   bg="white", font=("黑体", 12))     
        pic_7_button_3 = Radiobutton(root, text="7", width=2, height=1, variable=data_3, value=6,
                                   bg="white", font=("黑体", 12))    
        pic_8_button_3 = Radiobutton(root, text="8", width=2, height=1, variable=data_3, value=7,
                                   bg="white", font=("黑体", 12))     

        pic_1_button_3.place(x=10, y=525)
        pic_2_button_3.place(x=55, y=525)
        pic_3_button_3.place(x=100, y=525)
        pic_4_button_3.place(x=145, y=525)
        pic_5_button_3.place(x=190, y=525)
        pic_6_button_3.place(x=235, y=525)
        pic_7_button_3.place(x=280, y=525)
        pic_8_button_3.place(x=325, y=525)


        

        # Next按钮
        next_button = Button(root, text="Next", font=("黑体", 10), width=10, height=1, command=next_window)
        next_button.pack(side=BOTTOM, pady=10)
        note = Label(root, text=note_s, width=200, height=2, font=("黑体", 11))
        note.pack(side=BOTTOM)

        root.protocol("WM_DELETE_WINDOW", on_exit)
        root.mainloop()
        choice_1.append(data_1.get())
        choice_2.append(data_2.get())
        choice_3.append(data_3.get())
    step += 1


# list_b中元素原本的格式为：[方法1，……方法8，图片序号]，现在加上：选择最优图片，最优图对应的方法，选择次优图片，次优图对应的方法，选择第三优图片，第三优图对应的方法
# 更改后格式：[方法1，……方法8，图片序号，选择最优图片，最优图对应的方法，选择次优图片，次优图对应的方法，选择第三优图片，第三优图对应的方法]
for i in range(len(list_b)):
    list_b[i].append(choice_1[i])
    list_b[i].append(list_b[i][choice_1[i]])
    list_b[i].append(choice_2[i])
    list_b[i].append(list_b[i][choice_2[i]])
    list_b[i].append(choice_3[i])
    list_b[i].append(list_b[i][choice_3[i]])


# print(list_b)

# method_count所记录的是每一个方法由一名用户选择的数量，如：[1, 6, 5]，表示方法1选择1次，方法2选择6次，方法3选择5次
method_count_1 = [0 for i in range(method_num)]
method_count_2 = [0 for i in range(method_num)]
method_count_3 = [0 for i in range(method_num)]
for i in range(len(list_b)):
    method_count_1[list_b[i][-5] - 1] += 1
    method_count_2[list_b[i][-3] - 1] += 1
    method_count_3[list_b[i][-1] - 1] += 1

if not os.path.exists(project_folder + '/results.txt'):
    file = open(project_folder + '/results.txt', 'w')
    file.write(str(method_dict) + '\n')
    file.close()
with open(project_folder + '/results.txt', 'a') as fw:
    fw.write('用户：' + str(name[0]) + '    ' + '年龄：' + str(age[0]) + '    ' + '性别：' + str(gender[0]) + '\n')
    fw.write('最优:\t' + '\t'.join([str(i) for i in method_count_1]) + '\n')
    fw.write('次优:\t' + '\t'.join([str(i) for i in method_count_2]) + '\n')
    fw.write('第三:\t' + '\t'.join([str(i) for i in method_count_3]) + '\n')
    fw.close()

