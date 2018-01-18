
# numpy专用函数
## sort 返回排序后的顺序
## lexsort 根据键值的字典序进行排序
## argsort 返回输入数组排序后的下标
## msort 沿着第一个轴排序
## sort_complex对复数进行先实部后虚部的排序 


```python
import numpy as np

np.random.seed(42)
complex_num=np.random.random(5)+1j*np.random.random(5)
complex_num
np.sort_complex(complex_num)
```




    array([ 0.15601864+0.70807258j,  0.37454012+0.15599452j,
            0.59865848+0.60111501j,  0.73199394+0.86617615j,
            0.95071431+0.05808361j])




```python
import numpy as np

a=np.array(np.arange(9))
np.argmax(a)
```




    8




```python
import numpy as np
from matplotlib.pyplot import plot,show
a=np.pv(0.03/4,5*4,-10,-1000)
b=[]
for i in np.arange(1,10):
    b.append(np.pv(0.03/4,i*4,-10,-1000))
plot(b,'bo')
show()
```


![png](output_3_0.png)


np.pv计算终值，在某个时间点的收益，四个元素，利率，期数，每期需要付的金额和现值


```python
import numpy as np
a=np.random.randint(100,size=5)
a=np.insert(a,0,-100)
b=np.npv(0.03,a)
b
```




    148.49352996524613



np.npv净现值，需要利率，现金流


```python
import numpy as np
a=np.array([-100,38,48,90,17,36])
b=np.irr(a)
b
c=np.pmt(0.03,8,-90)
c
d=round(np.nper(0.03/12,-100,8000),0)
d
```




    89.0



round(fouble,number)小数保留位数
np.irr内部收益率，指的是净现值为0的有效利率，参数每一期的现金流（array类型）
np.pmt()分期付款的金额，利率，期数，总金额
np.ppmt()分期支付每期的本金，利率，所在第几期，总期数，总金额
np.ipmt()分期支付每期的利息，利率，所在第几期，总期数，总金额
np.nper()分期数，利率，每月需要支付的金额，总金额
np.mirr()修正内部收益率，现金流array(且必有一正一负，第一个值当做沉没成本)，利率，回报率
np.rate()利率，付款期数，每期支付资金，现值和中值利率

## 窗函数


```python
import numpy as np
from matplotlib.pyplot import plot,show

windows=np.bartlett(42)
plot(windows)
show()
```


![png](output_10_0.png)


np.bartlett绘制巴特利特窗


```python
import numpy as np
from matplotlib.pyplot import plot,show
n=np.random.randint(100,size=7)
window=np.blackman(80)
plot(window)
show()
```


![png](output_12_0.png)


## 矩形窗Rectangle

矩形窗使用最多，习惯上不加窗就是使信号通过了矩形窗。这种窗的优点是主瓣比较集中，缺点是旁瓣较高，并有负旁瓣，导致变换中带进了高频干扰和泄漏，甚至出现负谱现象。频率识别精度最高，幅值识别精度最低，所以矩形窗不是一个理想的窗。

如果仅要求精确读出主瓣频率，而不考虑幅值精度，则可选用矩形窗，例如测量物体的自振频率等，也可以用在阶次分析中。

## 汉宁窗Hanning

又称升余弦窗。主瓣加宽并降低，旁瓣则显著减小，从减小泄漏观点出发，汉宁窗优于矩形窗．但汉宁窗主瓣加宽，相当于分析带宽加宽，频率分辨力下降。它与矩形窗相比，泄漏、波动都减小了,并且选择性也提高。

是很有用的窗函数。如果测试信号有多个频率分量，频谱表现的十分复杂，且测试的目的更多关注频率点而非能量的大小，需要选择汉宁窗。如果被测信号是随机或者未知的，选择汉宁窗。

## 海明窗（汉明窗）Hamming

与汉宁窗都是余弦窗，又称改进的升余弦窗，只是加权系数不同，使旁瓣达到更小。但其旁瓣衰减速度比汉宁窗衰减速度慢。

与汉明窗类似，也是很有用的窗函数。

## 平顶窗Flap Top

平顶窗在频域时的表现就象它的名称一样有非常小的通带波动。

由于在幅度上有较小的误差，所以这个窗可以用在校准上。

## 凯塞窗Kaiser

定义了一组可调的由零阶贝塞尔Bessel 函数构成的窗函数，通过调整参数β可以在主瓣宽度和旁瓣衰减之间自由选择它们的比重。对于某一长度的Kaiser 窗，给定β，则旁瓣高度也就固定了。

 
## 布莱克曼窗Blackman

二阶升余弦窗，主瓣宽，旁瓣比较低，但等效噪声带宽比汉宁窗要大一点，波动却小一点。频率识别精度最低，但幅值识别精度最高，有更好的选择性。

常用来检测两个频率相近幅度不同的信号。

## 高斯窗Gaussian

是一种指数窗。主瓣较宽，故而频率分辨力低；无负的旁瓣，第一旁瓣衰减达一55dB。常被用来截短一些非周期信号，如指数衰减信号等。

对于随时间按指数衰减的函数，可采用指数窗来提高信噪比。

## 三角窗（费杰窗)Fejer

是幂窗的一次方形式。与矩形窗比较，主瓣宽约等于矩形窗的两倍，但旁瓣小，而且无负旁瓣。

如果分析窄带信号，且有较强的干扰噪声，则应选用旁瓣幅度小的窗函数，如汉宁窗、三角窗等；

## 切比雪夫窗（Chebyshev）

在给定旁瓣高度下，Chebyshev窗的主瓣宽度最小，具有等波动性，也就是说，其所有的旁瓣都具有相等的高度。


```python
import numpy as np
from matplotlib.pyplot import plot,show
window=np.hamming(41)
plot(window)
show()
```


![png](output_14_0.png)



```python
import numpy as np
from matplotlib.pyplot import imshow,show

x=np.linspace(0,4,100)
xx=np.outer(x,x)
v=np.sinc(xx)
imshow(v)
show()
```


![png](output_15_0.png)


# 质量控制


```python
import numpy as np
print(np.testing.assert_almost_equal(0.1222222,0.1222227,decimal=6))
```

    None


np.testing.assert_almost_equal()比较双精浮点是否相等，相等返回None,不等报错。
可以比较两个数字，也可以比较两个数组（形状相同）。decimal表示精度。
np.testing.assert_allclose()比较数组大小，参数rtol（可省略）:相对容差限，atol（可省略）:绝对容差限。
np:
    testing:
        equal对象比较
        string_equal比较字符串
