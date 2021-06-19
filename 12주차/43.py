""" ----------------------- 파이썬 금융통계 실습 ---------------------------"""
# 현금흐름, 이자율과 시간가치
# 재무나 금융 의사결정은 주어진 금융상품 또는 프로젝트에 대하여
# i) 미래에 발생할 현금흐름을 예측하고
# ii) 그 현금흐름의 현재가치 또는 미래가치(시간가치)를 평가하여 비교하는 것
# 이러한 현금흐름의 시간가치를 평가하기 위해서는 이자율이 필요하며, 
# 시간가치를 계산하는 방법에는 단리와 복리가 존재

#%% ============================================================================= 
# 1. 단리이자 계산
# ============================================================================= 
# 단리는 원금에 대하여 이자율을 곱해 이자를 계산하고 주기적으로 원금에 대한 이자를
# 지급하는 방식
# 년기준단리: 미래가치=현재가치*(1+년간이자율*년(year)의 수) ==> FV=PV*(1+r*n)
# 여기서 반드시 주의해야 할 사항은
# 이자율이 적용되는 기간(기간이자율)과 "기간의 수"를 계산하는 기간이 정확히 일치해야 함. 
# 예를 들어 이자율이 1년 짜리 이자율(년이자율)이라면 n을 계산할 때 년(year)의 수를 셈. 
# 이자율이 6개월 짜리 이자율이라면 n을 계산할 때는 6개월의 수를 셈.
#년이자율 예시: 원금(현재가치) 1000을 년이자율 5%인 계좌에 5년 동안 저축했다고 하자. 
# 이자가 1년에 한번 단리로 계산된다면 5년 후 이 저축계좌의 미래가치는 얼마인가?
PV=1000
r=0.05
n=5
FV_simple_1=PV*(1+r*n)
print(FV_simple_1)
interest_on_PV_simple_1 = FV_simple_1 - PV # 원금에 대한 5년 동안의 이자
print(interest_on_PV_simple_1)

#%%
# m-기간 기준단리: 미래가치=원금*(1+년간이자율/m*n*m-기간(year)의 수) 
# ==> FV=PV*(1+r/m*n*m)
# 여기서 m은 1년에 이자계산 기간이 들어가는 횟수
# ==> 예) 이자가 6개월마다 계산된다면 이면 6개월은 1년에 2번 있으므로 m=2
# 일반적으로 금융시장에서는 이자율을 년기준으로 표시하며, 
# 만약 이자율을 1년에 한 번이 아니라 6개월에 한 번 하는 경우
# 이자율을 6개월에 해당하는 이자로 변환하고(r --> r/m)
# 년의 갯수도 6개월의 갯수로 변환 (n --> n*m)
""" 반기이자율 예시: 원금(현재가치) 1000을 년이자율 5%인 계좌에 5년 동안 저축했다고 하자.
 이자가 6개월에 한번 단리로 계산된다면 5년 후 이 저축계좌의 미래가치는
얼마인가?
""" 
PV=1000
r=0.05
n=5
m=2
FV_simple_2=PV*(1+r/m*n*m)
print(FV_simple_2)
interest_on_PV_simple_2 = FV_simple_2 - PV # 원금에 대한 5년 동안의 이자
print(interest_on_PV_simple_2)
# 위에서 FV_simple_2은 FV_Simple_1과 동일한 결과를 준다. 왜냐하면, 두 가지 경우 모두
# 단리방식이며 이자계산만 6개월마다 하는지 또는 1년 마다 하는지 차이이기 때문이다.
# ============================================================================= # #%% 2. 복리이자 계산
# ============================================================================= # 복리는 원금에 대한 이자 뿐만 아니라 이자에 대한 이자도 지급하는 방식
# 년기준복리: 미래가치=현재가치*(1+년간이자율)**년(year)의 수 ==> FV=PV*(1+r)**n
# m-기간 기준복리: 미래가치=원금*(1+년간이자율/m)**(n*m) ==> FV=PV*(1+r/m)*(n*m)

#%%
""" 년이자율 예시: 원금(현재가치) 1000을 년이자율 5%인 계좌에 5년 동안 저축했다고 하자.
 이자가 1년에 한번 복리로 계산된다면 5년 후 이 저축계좌의 미래가치는 얼마인가? """ 
PV=1000
r=0.05
n=5
m=1
FV_compound_1=PV*(1+r/m)**(n*m)
print(FV_compound_1)
interest_on_interst_compound_1 = FV_compound_1 - PV - interest_on_PV_simple_1
print(interest_on_interst_compound_1)

#%%
""" 반년이자율 예시: 원금(현재가치) 1000을 년이자율 5%인 계좌에 5년 동안 저축했다고 하자.
 이자가 6개월에 한번 복리로 계산된다면 5년 후 이 저축계좌의 미래가치는 얼
마인가?
""" 
PV=1000
r=0.05
n=5
m=2
FV_compound_2=PV*(1+r/m)**(n*m)
print(FV_compound_2)
interest_on_interst_compound_2 = FV_compound_2 - PV - interest_on_PV_simple_1
print(interest_on_interst_compound_2)
# ============================================================================= # 

#%% 3. 연속복리 계산
# ============================================================================= 
# 이제 복리이면서 이자계산 주기를 점점더 짧게 해보자. 
# 예를들어, 이자계산주기를 1년 --> 6개월 --> 3개월 --> .... --> 1초 --> 0.001초 --> ... 
# 우선 복리이자계산 주기를 3개월로 해본 후 일반화 시켜 보자. 
# 위의 공식에서 3개월인 경우는 m=4로 하기만 하면 된다. (1년에 3개월은 4번!)
PV=1000
r=0.05
n=5
m=4
FV_compound_3=PV*(1+r/m)**(n*m)
print(FV_compound_3)

#%% 복리계산주기가 3개월인 경우와 앞의 1년과 6개월인 경우의 결과를 비교해보면
# 5년 후 최종 저축금액이 더 증가하는 것을 볼 수 있는데 이는 이자에 대한 이자가 더
# 붙는 복리효과 때문이다. 
# 자 이제 일반화 시켜 보자. 
PV=1000
r=0.05
n=5
m_max=1200
FV_compound=[]
for m in range(1,m_max+1):
    FV_compound.append(PV*(1+r/m)**(n*m))
print(FV_compound)

#%% m에 따른 FV_compound의 변화 그래프 그리기
import matplotlib.pyplot as plt
fig=plt.figure()
axes1=fig.add_subplot(1,1,1) # add_subplot(행크기, 열크기, 위치)
axes1.plot(range(1,m_max+1),FV_compound)
axes1.set_title("compounding effect")
axes1.set_xlabel('Compounding Frequency - m')
axes1.set_ylabel('Future Value - FV')

#%% 연속복리: FV=PV*exp(r*n) # exp: 자연지수
import numpy as np
PV=1000
r=0.05
n=5
temp=PV*np.exp(r*n)
FV_continuous=np.tile(PV*np.exp(r*n),[m_max,1])
fig=plt.figure()
axes1=fig.add_subplot(1,1,1) # add_subplot(행크기, 열크기, 위치)
axes1.plot(range(1,m_max+1),FV_compound)
axes1.plot(range(1,m_max+1),FV_continuous)
axes1.set_title("Compounding effect")
axes1.set_xlabel('Compounding Frequency - m')
axes1.set_ylabel('Future Value - FV')

# ============================================================================= 
#%% 4. 기존 모듈 이용
# ============================================================================= 
# 복리 계산의 경우 다음과 같이 numpy, scipy 모듈 사용 가능
# 앞의 문제를 다시 보자.
""" 년이자율 예시: 원금(현재가치) 1000을 년이자율 5%인 계좌에 5년 동안 저축했다고 하자.
 이자가 1년에 한번 복리로 계산된다면 5년 후 이 저축계좌의 미래가치는 얼마
인가?
"""
import scipy as sp
import numpy as np
help(sp.fv)
help(np.fv)

pv=1000
r=0.05
n=5
m=1
FV_sp=sp.fv(r,n,0,-pv) # fv(rate, nper, pmt, pv, when='end') #NOTE pmt 중간에 현금흐름이 있는 경우 # when 기초 기준인가 기말기준 인가
# NOTE fv는 빠져나간다는 관점으로 Pv가 마이너스이다.
print(FV_sp)
FV_np=np.fv(r,n,0,-pv)
print(FV_np)

#%% 앞서 직접 작성한 경우와 정확히 동일한 결과!
""" 반기이자율 예시: 원금(현재가치) 1000원을 년이자율 5%인 계좌에 5년 동안 저축했다고 하자.
 이자가 6개월에 한번 복리로 계산된다면 5년 후 이 저축계좌의 미래가치는 얼
마인가?
""" 
pv=1000
r=0.05
n=5
m=2
FV_sp_2=sp.fv(r/m,n*m,0,-pv) # fv(rate, nper, pmt, pv, when='end')
print(FV_sp_2)
FV_np_2=np.fv(r/m,n*m,0,-pv) #PV*(1+r/m)**(n*m)
print(FV_np)

#%% [과제 43-1] 앞서 m에 따른 FV값을 산출하여 그린 그림을 방금 학습한 np.fv함수를
# 사용하여 고쳐 보세요.
import numpy as np
PV=1000
r=0.05
n=5
m_max=1200
FV_compound=[]
for m in range(1,m_max+1):
    FV_compound.append(np.fv(r/m,n*m,0,-pv))

# m에 따른 FV_compound의 변화 그래프 그리기
import matplotlib.pyplot as plt
fig=plt.figure()
axes1=fig.add_subplot(1,1,1) # add_subplot(행크기, 열크기, 위치)
axes1.plot(range(1,m_max+1),FV_compound)
axes1.set_title("compounding effect")
axes1.set_xlabel('Compounding Frequency - m')
axes1.set_ylabel('Future Value - FV')

# ============================================================================= # 
#%% 5. 현재 가치 계산
# ============================================================================= 
# 현재가치(PV: Present Value)를 계산하는 하는 방법은 앞서 학습한 미래가치(FV: FutureValue)를
# 계산하는 공식에서 PV를 중심으로 재배치하면 되는 아주 간단한 문제
# 이러한 현재가치 계산은 NPV(Net Present Value)를 구하거나 주식 또는 모든 금융상품의
# 현재가치를 구하는데 사용 ==> 따라서 매우 중요!
# 년기준단리: FV=PV*(1+r*n) ==> PV=FV/(1+r*n)
# 미래가치(FV) 구하는 문제가 다음과 같다고 하자. 
#년이자율 예시: 원금(현재가치) 1000을 년이자율 5%인 계좌에 5년 동안 저축했다고 하자. 
# 이자가 1년에 한번 단리로 계산된다면 5년 후 이 저축계좌의 미래가치는 얼마인가?
# 위의 문제를 현재가치(PV)구하는 문제로 재구성하면 다음과 같다. 
# 이자가 1년에 한번 단리로 계산되는 년이자율 5%인 계좌에 5년동안 저축하여 5년 후
# 저축한 금액이 1,250원이 되었다고 하자. 최초 원금은 얼마인가?
# 또는
# 이자가 1년에 한번 단리로 계산되고 년이자율이 5%라고 가정하자. 5년 후
# 1250원과 동일한 가치를 갖는 현재가치는 얼마인가?
FV=1250
r=0.05
n=5
PV_simple_1=FV/(1+r*n)
PV_simple_1

#%% m-기간 기준단리: FV=PV*(1+r/m*n*m) ==> PV=FV/(1+r/m*n*m)
# 년기준복리: FV=PV*(1+r)**n ==> PV=FV/(1+r)**n
# m-기간 기준복리: FV=PV*(1+r/m)*(n*m) ==> PV=FV/(1+r/m)*(n*m)
# 기존 모듈 이용
import scipy as sp
import numpy as np
help(sp.pv)
help(np.pv)
fv=1276.2815625000003
r=0.05
n=5
m=1
PV_sp=sp.pv(r,n,0,fv) # pv(rate, nper, pmt, fv=0, when='end')
print(PV_sp)
PV_np=np.pv(r,n,0,fv)
print(PV_np)

#%%[과제 43-2] 이자가 6개월에 한번 복리로 계산되고 년이자율이 5%인 계좌의 5년 후1000원의 현재가치는 얼마인가?
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
# %%
