#第三方模块
from PIL import Image,ImageFilter
im=Image.open(r"C:\Users\Administrator\Desktop\Python学习\素材\0.jpg")#打开图像文件
im2=im.filter(ImageFilter.BLUR)#调用模糊滤镜
im2.save(r"C:\Users\Administrator\Desktop\Python学习\素材\0改.jpg")

#安装卸载第三方模块：pip工具
#pip工具下载：打开命令窗口》》输入python -m pip install --upgrade pip》》回车
#pip工具第三方模块下载：打开命令窗口》》输入pip install 第三方模块包名》》回车
#pip工具第三方模块卸载：打开命令窗口》》输入pip uninstall 第三方模块包名》》回车


#通过https://www.lfd.uci.edu下载第三方模块
#1.打开网址：https://www.lfd.uci.edu》》software》》Python Modules》》wheel packages》》点击对应版本模块下载
#2.找到下载的文件.whl》》按住shift键不放，打开命令窗口》》输入pip install 文件名》》回车
