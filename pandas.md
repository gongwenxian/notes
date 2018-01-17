
# pandas#



```python
import pandas as pd
a=pd.Series([1,-2,3,0])
a.rank()
```




    0    3.0
    1    1.0
    2    4.0
    3    2.0
    dtype: float64




```python


```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-5-2382f8552653> in <module>()
    ----> 1 from urllib2 import urlopen
          2 from lxml.html import parse
          3 a=urlopen('http://www.baidu.com')
          4 a


    ModuleNotFoundError: No module named 'urllib2'



```python
import matplotlib.pyplot as plt
from numpy.random import randn

fig=plt.plot(randn(80).cumsum(),'ko--')
fig
```




    [<matplotlib.lines.Line2D at 0x10dff1748>]




![png](output_3_1.png)



```python
from pandas import Series,DataFrame
import numpy as np
df=DataFrame(np.random.randn(10,4).cumsum(0),columns=['a','b','c','d'],index=np.arange(0,100,10))
df.plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x10df145c0>




![png](output_4_1.png)



```python
from matplotlib.mlab import mlab
import numpy as np
x,y,z = np.mgrid[-3:3:100j,-1:1:100j,-3:3:100j]
f=(x**2 + 9.0/4*y**2 + z**2 -1)**3 - x**2 * z**3 -9.0/80 * y**2 * z**3
contour=mlab.contour3d(x,y,z,f,contours=[0],color=(1,0,0)) 
```


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-5-1c287eaebc33> in <module>()
    ----> 1 from matplotlib.mlab import mlab
          2 import numpy as np
          3 x,y,z = np.mgrid[-3:3:100j,-1:1:100j,-3:3:100j]
          4 f=(x**2 + 9.0/4*y**2 + z**2 -1)**3 - x**2 * z**3 -9.0/80 * y**2 * z**3
          5 contour=mlab.contour3d(x,y,z,f,contours=[0],color=(1,0,0))


    ImportError: cannot import name 'mlab'



```python
from pylab import *
import numpy as np

X=np.linspace(-np.pi,np.pi,256,endpoint=True)
C,S=np.cos(X),np.sin(X)

plot(X,C)
plot(X,S)

show()
```


    <matplotlib.figure.Figure at 0x10c483e10>

