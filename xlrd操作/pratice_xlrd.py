import xlrd
A=[]
B=[]
a=0
def read_excel():
    # global a
    # while a<100:

    # 获取xlsx路径
    filename = r'D:\脚本\FGO.air\账号+密码.xlsx'
    # 打开xlsx文件
    workbook = xlrd.open_workbook(filename)
    # print(workbook.sheet_names())
    # 通过索引获取第一个表格
    sheet = workbook.sheet_by_index(0)
    #删除‘用户名’，引用第一个账号
    username = sheet.col_values(0)
    username_pop = username.pop(0)
    A.append(username_pop)

    # print(username)
    # 删除‘密码’，引用第一个密码
    password = sheet.col_values(1)
    password_pop = password.pop(0)
    B.append(password_pop)
    # print(password)
    # 获取表格所有的用户名，再把获取的赋值，在下面的输入中引用
    for i in range (100):
        IDname=username[i]
        print(IDname)
        IDpassword = password[0]
        print(IDpassword)


    # IDname=username[0]
    # print(IDname)


    # touch  XXX
    # text（IDname）
    # touch  XXX
    # text(IDpassword)

    # a+=1

if __name__ == '__main__':
    read_excel()