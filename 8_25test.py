i=0
while i<5:
    a= eval(input("请输入0结束循环，你有5次机会：\n"))
    i+=1
    if a == 0:
        print("你触发了break语句，导致else语句不会生效")
        break
else:
    print("五次循环你都用过了，else语句生效了")