#配置一個長度為num的陣列
def GetList(num):
    List = []
    for i in range(num):
        List.append(0)
    return List 

#複製一個List
def CopyList(x):
    newX = []
    for data in x:
        newX.append(data)
    return newX

'''
以下為m取n演算法 
'''
def judge(n,m, index):
    for i in range(n-1,n-m-1,-1):
        if index[i] == 0: 
            return False
    return True

def nGetM(n, m):
    index = GetList(n)
    posibility = []
    num = 0
    for i in range(m):
        index[i] = 1
    posibility.append(CopyList(index))
    while(judge(n,m,index) == False):
        for i in range(n-1):
            if((index[i]==1) and (index[i+1]==0)):
                index[i]=0
                index[i+1]=1
                count=0
                for j in range(i):
                    if(index[j] == 1):
                        index[j]=0;
                        index[count]=1
                        count += 1
                posibility.append(CopyList(index))
                break
    return posibility

def main():
    n = 48
    m = 5
    posibility = nGetM(n,m)
    for index in posibility:
        print(index)

if __name__ == '__main__':
    main()