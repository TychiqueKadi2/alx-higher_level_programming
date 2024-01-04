#!/urs/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    com_mod = dir()
    for i in range(0, len(com_mod)):
        if com_mod[i][:2] != "__":
            print("{:s}".format(com_mod[i]))
