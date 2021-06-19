#i) 사용자 정의 함수를 사용하여 계산하여 보세요.
import numpy as np
FV=1000
r=0.05
n=5
m = 2
def get_pv(Fv, r, n, m):
    return FV/(1+r/m*n*m)

print(get_pv(FV, n, r, m))
#ii) numpy의 pv함수를 사용하여 계산하여 보세요.
import numpy as np
FV=1000
r=0.05
n=5
m = 2
def get_pv_np(Fv, r, n, m):
    return np.pv(r/m,n*m,0,Fv)

print(get_pv_np(FV, n, r, m))