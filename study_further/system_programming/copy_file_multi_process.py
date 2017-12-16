from multiprocessing import process, Pool, Manager
import os, sys, time
import stat


#递归删除一个文件中所有的内容
def delFolder(rootdir):
    # Walk在os模块下面，用来根据提供的文件夹生成一个generator。每次可以得到一个三元tupple，
    # 其中第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件
    #1.先删所有文件
    filelist = os.listdir(rootdir)
    for file in filelist:
        file_path = os.path.join(rootdir, file)
        # print(file_path)
        #修改文件权限
        os.chmod(file_path, stat.S_IWRITE)
        if os.path.isdir(file_path):
            if not os.listdir(file_path):
                os.rmdir(file_path)
            else:
                delFolder(file_path)
        else:
            os.remove(file_path)
    #2.删除文件
    os.rmdir(rootdir)

#获取一个文件夹内所有的文件
def getFiles(rootdir):
    fileList = []
    dirList = []
    for root, dirs, files in os.walk(rootdir, topdown=False):
        for file in files:
            fileList.append(os.path.join(root, file))
        for item in dirs:
            dirList.append(os.path.join(root, item))
    return fileList, dirList

#文件copy
def copyFile(filename, oldFolderName, newFolderName, queue):
    #完成一个文件的copy
    queue.put("%s 正在传输。。。。。。" % filename)
    fr = open(filename)
    fw = open(filename.replace(oldFolderName, newFolderName), 'w')

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()


if __name__ == "__main__":
    start_time = time.time()
    sys.setrecursionlimit(100)

    oldFolderName = "E:\hangzhouYunQi2017ppt-master"
    newFolderName = oldFolderName + "_bak"


    #创建一个文件夹
    flag = os.path.exists(newFolderName)
    if flag:
        delFolder(newFolderName)
    os.mkdir(newFolderName)

    #获取old文件夹中所有的文件夹
    tu = getFiles(oldFolderName)
    for item in tu[1]:
        item = item.replace(oldFolderName, newFolderName)
        os.makedirs(name=item, exist_ok=True)

    pool = Pool(5)
    queue = Manager().Queue()
    for filename in tu[0]:
        pool.apply_async(copyFile, args = (filename, oldFolderName, newFolderName, queue))

    num = 0
    while num < len(tu[0]):
        print(queue.get(True))
        num += 1

    end_time = time.time()
    print('use %0.2f seconds to complete!' % (end_time - start_time))