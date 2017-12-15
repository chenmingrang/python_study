from multiprocessing import process, Pool
import os, sys
import stat


#递归删除一个文件中所有的内容
def delFolder(rootdir):
    # Walk在os模块下面，用来根据提供的文件夹生成一个generator。每次可以得到一个三元tupple，
    # 其中第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件
    #1.先删所有文件
    filelist = os.listdir(rootdir)
    for file in filelist:
        file_path = os.path.join(rootdir, file)
        print(file_path)
        os.chmod(file_path, stat.S_IWRITE)
        if os.path.isdir(file_path):
            if not os.listdir(file_path):
                os.rmdir(file_path)
            else:
                delFolder(file_path)
        else:
            os.remove(file_path)
    os.rmdir(rootdir)
    # for root, dirs, files in os.walk(rootdir, topdown=False):
    #     for name in files:
    #         os.chmod(os.path.join(root, name), stat.S_IWRITE)
    #         os.remove(os.path.join(root, name))

def getFiles(folder):
    os.listdir(folder)

def copyFile(file, new_path):
    #完成一个文件的copy
    fr = open(file)
    fw = open(new_path, 'w')

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()

sys.setrecursionlimit(100)

oldFolderName = input("请输入要复制的文件夹名称：")
newFolderName = oldFolderName + "_test"


#创建一个文件夹
flag = os.path.exists(newFolderName)
if flag:
    delFolder(newFolderName)
os.mkdir(newFolderName)

#获取old文件夹中所有的文件夹
filenames = os.listdir(oldFolderName)
# print(filenames)

# pool = Pool(6)
# pool.apply_async()
#将文件copy到新的文件夹中