import random
# 设置多个字符串选取指定的数量字符生成新的字符串
def random_pratice():
    i=''.join (random.sample(['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k'],12))
    print(i)
    print(type(i))


    # touch XXX
    # text(i)




if __name__ == '__main__':
    random_pratice()