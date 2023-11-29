# Extracts the dominant color from an image represented by an array.

## pip install getdominantcolor

### Tested against Windows / Python 3.11 / Anaconda




```python

Parameters:
- x (numpy.ndarray): The input image represented as a NumPy array with shape (height, width, channels - 3).

Returns:
tuple: A tuple representing the dominant color in the RGB format (red, green, blue).

The function reshapes the input array to a two-dimensional array and calculates a numerical code for each pixel
based on its RGB values. The dominant color is then determined by counting the occurrences of these codes and
returning the RGB values of the code with the highest frequency.

Example:
	from getdominantcolor import get_dom_color
	import numpy as np
	np.random.seed(0)
	x = np.random.randint(0, 255, (4000, 4000, 3))
	get_dom_color(x)
	# (81, 101, 238)
```