# 用于选出生成图片中最优图片的评分器
### choose-the-best-picture
A score application to verify pictures generated by different methods</br>

#### 使用说明：

1. 在py文件同级目录下存放评分**项目文件夹**（./project）
2. 在项目文件夹下创建各个**生成方法文件夹**以及**原始图像文件夹**（./project/method）
3. **原始图像文件夹**中存放处理前的原始图像(./project/method/picture.png)
4. **生成方法文件夹**中的图像文件名必须<font color=red>完整包含原图文件名与方法名，之间以下划线的形式分隔开。</font>（例 ./project/method/picture_method.png **or**piture_method_***.png）
5. 运行main.py开始生成图像评分
6. 在评分界面中可查看所有图像的生成方式，及评分进度
7. 评分结束后确认保存即可将评分结果保存在项目文件夹目录下的results_0.50.txt、results_0.75.txt、results_1.25.txt

</br>