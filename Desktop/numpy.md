

```python
import numpy as np
i2=np.eye(3)
i2
np.savetxt("eye,txt",i2)
```

创建单位矩阵，对角线均为1，其余的都是0.
savetxt方法储存为txt文件。


```python
import numpy as np
g,n=np.loadtxt('/Users/simmons/Desktop/1.csv',delimiter=',',usecols=(0,1),unpack=True)
g
n
vwap=np.average(n,weights=g)
mean=np.mean(n)
t=np.arange(len(g))
twap=np.average(n,weights=t)
highest=np.max(n)
δ=np.ptp(n)
δ
```




    20.0



vwap:加权平均数
twap:时间加权平均数
mean:平均数
highest最大值
δ:数组元素中最值的差
ps:
np.msort(数组)顺序排序
np.median(数组)求中位数
np.var(数组)求方差
np.std(数组)求标准差
np.log(数组)求对数
np.diff(数组)数组相邻元素差组成的数组


```python
import datetime 
def getweekday(s):
    return datetime.datetime.strptime(s,"%Y-%m-%d").date().weekday()

getweekday('2018-01-15')
```




    0



datetime.datetime.strptime(s,"格式").date().weekday()
获取当前日期所在周，0123456为 1234567


```python
import numpy as np
A=np.mat('1,2,3;4,5,6;7,8,9')
A
A.T
A.I
B=np.mat(np.arange(9).reshape(3,3))
B
C=np.bmat("A B;B A")
C
```




    matrix([[1, 2, 3, 0, 1, 2],
            [4, 5, 6, 3, 4, 5],
            [7, 8, 9, 6, 7, 8],
            [0, 1, 2, 1, 2, 3],
            [3, 4, 5, 4, 5, 6],
            [6, 7, 8, 7, 8, 9]])



.T:转置矩阵
.I:矩阵的逆
.bmat("A B;B A")创建复合矩阵
np.add.reduce(数组)一维数组求和
np.add.accumulate(数组)多维数组求和
np.divide(a,b)除法且仅保留整数，不做四舍五入处理
np.true_divide(a,b)除法返回浮点数，不做拦截



```python
import numpy as np
a=np.arange(-4,4)
np.remainder(a,2)
```




    array([0, 1, 0, 1, 0, 1, 0, 1])



np.remainder(a,b)a,b俩数组的余数组成的数组、{可以写成a%b}


```python
import numpy as np
F=np.matrix([[1,1],[1,0]])
(F**6)[0,0]
```




    13



np.matrix(array)创建矩阵
np.rint()对浮点取整，结果仍为浮点类型


```python
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import sys

a=8
b=9
t=np.linspace(-np.pi,np.pi,201)
x=np.sin(a * t + np.pi/2)
y=np.sin(b * t)
plot(x,y)
show()
```


![png](output_12_0.png)


sys.argv[]表示从外部获取参数，sys.argv[0]表示python根目录，1表示一个参数
这个图形是个 利萨茹曲线。


```python
import numpy as np
from matplotlib.pyplot import plot,show
import sys

t=np.linspace(-np.pi,np.pi,201)
k=99
f=np.zeros_like(t)
for i in range(len(t)):
    f[i]=np.sum(np.sin(2*np.pi*k*t[i])/k)
f=(-2/np.pi)*f
plot(t,f)
show()

```


![png](output_14_0.png)



```python
import numpy as np
 
A=np.mat("1 -2 1;0 2 -8;-4 5 9")
b=np.array([0,8,-9])
x=np.linalg.solve(A,b)
x
np.linalg.eigvals(A)
np.linalg.eig(A)
```




    (array([ 0.02752148+0.j        ,  5.98623926+6.06922064j,
             5.98623926-6.06922064j]),
     matrix([[-0.86832079+0.j        ,  0.19882910-0.13261668j,
               0.19882910+0.13261668j],
             [-0.48158091+0.j        , -0.71901045+0.j        , -0.71901045-0.j        ],
             [-0.11873850+0.j        ,  0.35826846+0.54547913j,
               0.35826846-0.54547913j]]))



np.linalg.solve(A,b)求解线性方程
线性方程：未知数系数都是一次的
np.dot(A,x)=b,为手动验证结果是否正确的方法
np.linalg.eigvals(A) 求解特征值
np.linalg.eig(A)特征向量


```python
import numpy as np
A=np.mat("4 11 14;8 7 -2;7 7 7")
U,Sigma,V=np.linalg.svd(A,full_matrices=False)
U
V
U*np.diag(Sigma)*V
np.linalg.det(A)
```




    -419.99999999999994



M=UΣV* 奇异值分解 SVD
np.linalg.pinv(A) 求广义逆矩阵
广义逆矩阵与原矩阵相乘，得到一个结果近似为单位矩阵。
np.linalg.det(A) 计算行列式结果


```python
import numpy as np
from matplotlib.pyplot import plot,show

x=np.linspace(0.2*np.pi,30)
wave=np.cos(x)
transformed=np.fft.fft(wave)
plot(transformed,lw=2)
#show()
#print(np.all(np.abs(np.fft.ifft(transformed) - wave)<10**-9))
shifted=np.fft.fftshift(transformed)
plot(shifted,lw=3)
show()
```

    /usr/local/lib/python3.6/site-packages/numpy/core/numeric.py:531: ComplexWarning: Casting complex values to real discards the imaginary part
      return array(a, dtype, copy=False, order=order)



![png](output_19_1.png)


np.fft快速傅里叶变换模块
np.fft.fft()快速傅里叶变化
np.fft.ifft()逆操作还原信号
np.all()比较，有一个不为true就为false
np.fft.fftshift()移频操作
np.fft.ifftshift()移频逆操作
np.abs()绝对值


```python
import numpy as np
from matplotlib.pyplot import plot ,show
cash=np.zeros(10000)
cash[0]=1000
outcome=np.random.binomial(9,0.5,size=len(cash))

for i in range(1,len(cash)):
    if outcome[i] <5:
        cash[i]=cash[i-1] -1
    elif outcome[i] <10:
        cash[i]=cash[i-1]+1
    else:
        raise AssertionError("Unexpected:"+outcome)
outcome
plot(np.arange(len(cash)),cash)
show()
```


![png](output_21_0.png)


np.random.binomial(n,p,N)二项分布，n成功次数p成功一次概率N总次数
np.random.hypergeometric(n1,n2,n,N)超几何分布，离散分布。不放回抽出指定数量的分布。
n1第一次摸出的数量总个数n2第二类物品总个数n指定每次摸几个N总次数



```python
import numpy as np
from matplotlib.pyplot import plot,show

N=np.zeros(100)
p=np.random.hypergeometric(25,1,3,size=len(N))

for i in range(len(N)):
    if p[i]==3:
        N[i]=N[i-1]+1
    elif p[i]==2:
        N[i]=N[i-1]-6
    else:
        print("wrong")
        
plot(np.arange(len(N)),N)
show()
```


![png](output_23_0.png)



```python
import numpy as np
import matplotlib.pyplot as plt

N=10000
normal_values=np.random.lognormal(size=N)
dummy,bins,dummy=plt.hist(normal_values,np.sqrt(N),normed=False,lw=1)
sigma=1
mu=0
x=np.linspace(min(bins),max(bins),len(bins))
pdf=np.exp(-(np.log(x)-mu)**2 / (2*sigma**2)) /(x*sigma*np.sqrt(2*np.pi))
plt.plot(x,pdf,lw=3)
plt.show()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-83-d061eb2b93c7> in <module>()
          4 N=10000
          5 normal_values=np.random.lognormal(size=N)
    ----> 6 dummy,bins,dummy=plt.hist(normal_values,np.sqrt(N),normed=False,lw=1)
          7 sigma=1
          8 mu=0


    /usr/local/lib/python3.6/site-packages/matplotlib/pyplot.py in hist(x, bins, range, density, weights, cumulative, bottom, histtype, align, orientation, rwidth, log, color, label, stacked, normed, hold, data, **kwargs)
       3023                       histtype=histtype, align=align, orientation=orientation,
       3024                       rwidth=rwidth, log=log, color=color, label=label,
    -> 3025                       stacked=stacked, normed=normed, data=data, **kwargs)
       3026     finally:
       3027         ax._hold = washold


    /usr/local/lib/python3.6/site-packages/matplotlib/__init__.py in inner(ax, *args, **kwargs)
       1715                     warnings.warn(msg % (label_namer, func.__name__),
       1716                                   RuntimeWarning, stacklevel=2)
    -> 1717             return func(ax, *args, **kwargs)
       1718         pre_doc = inner.__doc__
       1719         if pre_doc is None:


    /usr/local/lib/python3.6/site-packages/matplotlib/axes/_axes.py in hist(***failed resolving arguments***)
       6159             # this will automatically overwrite bins,
       6160             # so that each histogram uses the same bins
    -> 6161             m, bins = np.histogram(x[i], bins, weights=w[i], **hist_kwargs)
       6162             m = m.astype(float)  # causes problems later if it's an int
       6163             if mlast is None:


    /usr/local/lib/python3.6/site-packages/numpy/lib/function_base.py in histogram(a, bins, range, normed, weights, density)
        727 
        728         # Initialize empty histogram
    --> 729         n = np.zeros(bins, ntype)
        730         # Pre-compute histogram scaling factor
        731         norm = bins / (mx - mn)


    TypeError: 'numpy.float64' object cannot be interpreted as an integer



![png](output_24_1.png)

