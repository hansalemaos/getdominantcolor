import numexpr as ne
import numpy as np

def get_dom_color(x):
    """
    Extracts the dominant color from an image represented by an array.

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
    """
    def get_color_back(code):
        blue = int(code % 256)
        green = int((code % (256 * 256) - blue) / 256)
        red = int((code - blue - green * 256) / (256 * 256))
        return red, green, blue

    arr = x.reshape(-1, x.shape[-1])
    outa = ne.evaluate('(c1 << 16) + (c2 << 8) + c3', global_dict={},
                       local_dict={'c1': arr[..., 0], 'c2': arr[..., 1], 'c3': arr[..., 2]})
    return get_color_back(np.bincount(outa).argmax())
