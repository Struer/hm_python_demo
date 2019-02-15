import os
import multiprocessing


def copy_file(file_name, source_folder_name, new_folder_name):
    print("进程%s 拷贝文件%s" % (os.getpid(), file_name))
    old_f = open(source_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()

def main():
    # 1.获取文件夹名字
    source_folder_name = input("请输入要copy的文件夹的名字:")
    # 2.创建文件夹
    try:
        new_folder_name = source_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass
    # 3.获取文件夹的所有的待copy的文件名字 listdir()
    file_names = os.listdir(source_folder_name)
    print(file_names)
    # 4.创建进程池
    po = multiprocessing.Pool(3)

    # 5.复制源文件夹中的文件，到新文件夹中的文件
    for file_name in file_names:
        po.apply_async(copy_file, args=(file_name, source_folder_name, new_folder_name))

    po.close()
    po.join()


if __name__ == '__main__':
    main()
