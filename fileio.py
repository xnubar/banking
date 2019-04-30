def write(filename,list_):
     with open(filename,"w") as fw:
        for i in list_:
            fw.write(i.strip())
            if list_.index(i)!=len(list_)-1:
                fw.write("\n")
            


def read(filename):
    with open(filename,"r") as fr:
        list_ = fr.readlines()
        return list_