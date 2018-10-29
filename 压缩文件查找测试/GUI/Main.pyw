from tkinter import *
from funcation import *  #菜单栏对应的各个子页面
 
class MainPage(object):
	def __init__(self, master=None):
		self.root = master #定义内部变量root
		self.root.geometry('%dx%d' % (900, 900)) #设置窗口大小
		self.createPage()
 
	def createPage(self):
		self.findbak_dan_page = FindbakFrame(self.root) # 创建不同Frame

		self.findbak_dan_page.pack() #默认显示数据录入界面
		menubar = Menu(self.root)
		menubar.add_command(label='备份文件查找-单', command = self.findbak_dan)
		self.root['menu'] = menubar  # 设置菜单栏
 
	def findbak_dan(self):
		self.findbak_dan_page.pack()#其中一个是显示需要显示的窗体，其他的是关闭其他窗体？
		self.queryPage.pack_forget()
		self.zichanchaxun_page.pack_forget()
		self.loudongchaxun_page.pack_forget()

root = Tk()
root.title('MoonLight by rpkr')
MainPage(root)
root.mainloop()
