#%% [과제 29-1] sent에서 3번째 문자부터 추출하고 그 이후는 추출한 문자로 부터 3번째 오는 문자들만
# 추출하여 print하는 코드를 작성하세요.
sent='a scratch'
string = sent[2:]
while(True):
    try:
        print(string[2])
        string = string[2:]
    except Exception as e:
        break