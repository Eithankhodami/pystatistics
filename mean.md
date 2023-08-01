# Calculating the mean

The mean is the average of the numbers. It is easy to calculate: add up all the numbers, then divide by how many numbers there are. In other words it is the sum divided by the count.

the formula for calculating the mean is:

$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i$$

where:
- $\bar{x}$ is the mean
- $n$ is the number of observations
- $x_i$ is the i-th observation
- $\sum_{i=1}^{n}$ is also the sum from ${i=1}$ to ${n}$ 

This formula calculates the average of a set of numbers. To calculate the mean, you add up all the numbers in the set and divide by the total number of observations. The result is the mean.

but in python we have an easy way to calculate mean using the numpy library. The numpy library has a function called `mean()` which takes a list as an argument and returns the mean of the list.

to use the numpy library we have to import it first using the following procedure:

1. open the python or your favorite IDE
2. type the following command in the python shell or in the IDE
```
import numpy as np
```
3. now you can use the numpy library by typing the following command
```
np.mean()
```

Lets have an example of creating a set of as a list and then calculating the mean using the numpy library.

```python
import numpy as np
x = [1,2,3,4,5,6,7,8,9,10]         #this is a list with 10 numbers
np.mean(x)
```
<h3><span style="color: #ff0000;">if you do not have an idea how the list is working</span></h3> 

[Follow the link for more about lists](list.md)

The result is <b><span style="color:green"> 5.5 </span></b>

now lets try to calculate the mean of the first 5 numbers in the list.

```python
import numpy as np
x = [1,2,3,4,5,6,7,8,9,10]
np.mean(x[:5])
```
The result is <b><span style="color:green"> 3.0 </span></b>

Now lets try to calculate the mean of the last 5 numbers in the list.

```python
import numpy as np
x = [1,2,3,4,5,6,7,8,9,10]
np.mean(x[5:])
```
The result is <b><span style="color:green"> 8.0 </span></b>

code for this calculation is saved in the file [mean.py](mean.py)