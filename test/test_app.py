# 测试代码
import numpy as np

def test_numpy():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = a + b
    assert np.all(c == [5, 7, 9])
