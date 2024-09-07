def print_triangle(n: int):
    for i in range(n):
        line = ""
        line += (" "*(n-i-1))
        line += ("*")      #首行 print 頂點＊
        if i==n-1:          #最末行底邊全 print ＊
            line +=  (" *"*(i))
        elif i >= 1:        #中間 print 兩邊＊並含空格
            line += (" "*((i*2-1)))
            line += ("*")
        
        print(line)
    

n = int(input("n: "))
print_triangle(n)

