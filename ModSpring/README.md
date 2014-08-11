ModSpring
=========

With ModSpring we can create an object with a spring shape, using the *modulus* operation

Intuition
=========

*Modular Arithmetic** is an interesting mathematical system. For example, it can be used to represent cyclic events, like the days of the week (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Monday...)

It seems that we can take advantage of this, to produce a spring shape in a simple way!

In this first example we will be using modulus 5 and only 10 numbers:

![Example of ModSpring](https://raw.github.com/rui-silva/MathArt/master/ModSpring/assets/first_example.png)

Take a close attention at 5 and 10. They're bot above 0. Why? Because 5 mod 5 and 10 mod 5 = 0!

Code
====

So, how can we implement this?

We will divide our approach in two steps:
- Compute x and y
- Compute z

Compute x and y
---------------

In order to have achieve the spiral shape, we will take advantage of the cyclic nature of the modulus operation.

We will also use some simple trigonometry - we can achieve a circle shape with (cos(**x**), sin(**x**)), for **x** in [ **0**, **2 pi** ]

Now we just have to merge these two operations! It ends up like this:
- Get a range of numbers **r**
- Apply the modulus operation to **r**
- Normalize **r** to be in the range **0** - **2 pi**
- Apply (cos(**r**), sin(**r**))

Compute z
---------

Computing z is even easier!
We just have to make each point a little higher than the previous one!
Simple, huh?

How to use
==========

```python
mod_spring = ModSpring(height=10, height_spacing=2, radius=7, precision=0.1)
mod_spring.compute()
```

This creates a spring shape with 10 units of height, and 7 units of radius.
The rings will be spaced by 2 units.
Finally, we choose a precision of 0.1. The bigger this parameters, the better.

Then you can use a plotting library (e.g. matplotlib), to draw it.
For example:

```python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

mod_spring = ModSpring(height=10, height_spacing=2, radius=7, precision=0.1)
mod_spring.compute()

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(res[:, 0], res[:, 1], res[:, 2])
plt.show()
```

Inspiration
===========
Got this idea while reading Concepts of Modern Mathematics, Ian Stewart.