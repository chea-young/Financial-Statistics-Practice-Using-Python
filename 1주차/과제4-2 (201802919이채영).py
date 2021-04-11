for i in range(2, 10):
    for j in range(1, 10):
        answer = i*j
        if(answer%3 == 0):
            print(str(i) +'*'+ str(j) +'= 짝')
        else:
            print(str(i) +'*'+ str(j) +'='+ str(answer))