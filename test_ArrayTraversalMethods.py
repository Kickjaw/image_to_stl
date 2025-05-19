from ArrayTraversalMethods import BreadthTraversalList

def test_CreateTraversalList_3x3():
    result = BreadthTraversalList(3, 3)
    expected = [
        [0, 0],
        [0, 1], [1, 0],
        [0, 2], [1, 1], [2, 0],
        [1, 2], [2, 1],
        [2, 2]
    ]
    assert result == expected

def test_CreateTraversalList_5x3():
    result = BreadthTraversalList(5, 3)
    expected = [
        [0, 0],
        [0, 1], [1, 0],
        [0, 2], [1, 1], [2, 0],
        [0, 3], [1, 2], [2, 1],
        [0, 4], [1, 3], [2, 2],
        [1, 4], [2, 3],
        [2, 4]
    ]
    assert result == expected

def test_CreateTraversalList_3x5():
    result = BreadthTraversalList(3, 5)
    expected = [
        [0, 0],
        [0, 1], [1, 0],
        [0, 2], [1, 1], [2, 0],
        [1, 2], [2, 1], [3, 0],
        [2, 2], [3, 1], [4, 0],
        [3, 2], [4, 1],
        [4, 2]
    ]
    assert result == expected    


from ArrayTraversalMethods import VerticalDepthTraversalList

def test_VerticalDepthTraversalList_3x3():
    result = VerticalDepthTraversalList(3, 3)
    expected = [
        [0, 0], [0, 1], [0, 2],
        [1, 0], [1, 1], [1, 2],
        [2, 0], [2, 1], [2, 2]
    ]
    assert result == expected

def test_VerticalDepthTraversalList_5x3():
    result = VerticalDepthTraversalList(5, 3)
    expected = [
        [0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
        [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
        [2, 0], [2, 1], [2, 2], [2, 3], [2, 4]
    ]
    assert result == expected

def test_VerticalDepthTraversalList_3x5():
    result = VerticalDepthTraversalList(3, 5)
    expected = [
        [0, 0], [0, 1], [0, 2],
        [1, 0], [1, 1], [1, 2],
        [2, 0], [2, 1], [2, 2],
        [3, 0], [3, 1], [3, 2],
        [4, 0], [4, 1], [4, 2]
    ]
    assert result == expected    

          

from ArrayTraversalMethods import HorizontalDepthTraversalList

def test_HorizontalDepthTraversalList_3x3():
    result = HorizontalDepthTraversalList(3, 3)
    expected = [
        [0, 0], [1, 0], [2, 0],
        [0, 1], [1, 1], [2, 1],
        [0, 2], [1, 2], [2, 2]
    ]
    assert result == expected

def test_HorizontalDepthTraversalList_5x3():
    result = HorizontalDepthTraversalList(5, 3)
    expected = [
        [0, 0], [1, 0], [2, 0],
        [0, 1], [1, 1], [2, 1],
        [0, 2], [1, 2], [2, 2],
        [0, 3], [1, 3], [2, 3],
        [0, 4], [1, 4], [2, 4]
    ]
    assert result == expected

def test_HorizontalDepthTraversalList_3x5():
    result = HorizontalDepthTraversalList(3, 5)
    expected = [
        [0, 0], [1, 0], [2, 0], [3, 0], [4, 0],
        [0, 1], [1, 1], [2, 1], [3, 1], [4, 1],
        [0, 2], [1, 2], [2, 2], [3, 2], [4, 2]
    ]
    assert result == expected


from ArrayTraversalMethods import SnakeVerticalTraversalList

def test_SnakeVerticalTraversalList_3x3():
    result = SnakeVerticalTraversalList(3, 3)
    expected = [
        [0, 0], [0, 1], [0, 2],
        [1, 2], [1, 1], [1, 0],
        [2, 0], [2, 1], [2, 2]
    ]
    assert result == expected

def test_SnakeVerticalTraversalList_5x3():
    result = SnakeVerticalTraversalList(5, 3)
    expected = [
        [0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
        [1, 4], [1, 3], [1, 2], [1, 1], [1, 0],
        [2, 0], [2, 1], [2, 2], [2, 3], [2, 4]
    ]
    assert result == expected

def test_SnakeVerticalTraversalList_3x5():
    result = SnakeVerticalTraversalList(3, 5)
    expected = [
        [0, 0], [0, 1], [0, 2],
        [1, 2], [1, 1], [1, 0],
        [2, 0], [2, 1], [2, 2],
        [3, 2], [3, 1], [3, 0],
        [4, 0], [4, 1], [4, 2]
    ]
    assert result == expected


from ArrayTraversalMethods import SnakeHorizontalTraversalList

def test_SnakeHorizontalTraversalList_3x3():
    result = SnakeHorizontalTraversalList(3, 3)
    expected = [
        [0, 0], [1, 0], [2, 0],
        [2, 1], [1, 1], [0, 1],
        [0, 2], [1, 2], [2, 2]
    ]
    assert result == expected

def test_SnakeHorizontalTraversalList_3x5():
    result = SnakeHorizontalTraversalList(3, 5)
    expected = [
        [0, 0], [1, 0], [2, 0], [3, 0], [4, 0],
        [4, 1], [3, 1], [2, 1], [1, 1], [0, 1],
        [0, 2], [1, 2], [2, 2], [3, 2], [4, 2]
    ]
    assert result == expected

def test_SnakeHorizontalTraversalList_5x3():
    result = SnakeHorizontalTraversalList(5, 3)
    expected = [
        [0, 0], [1, 0], [2, 0],
        [2, 1], [1, 1], [0, 1],
        [0, 2], [1, 2], [2, 2],
        [2, 3], [1, 3], [0, 3],
        [0, 4], [1, 4], [2, 4]
    ]
    assert result == expected


from ArrayTraversalMethods import ClockwiseOuterSpiralTraversalList

def test_ClockwiseOuterSpiralTraversalList_3x3():
    result = ClockwiseOuterSpiralTraversalList(3, 3)
    expected = [
        [0, 0], [1, 0], [2, 0],
        [2, 1], [2, 2], [1, 2],
        [0, 2], [0, 1], [1, 1]
    ]
    assert result == expected

def test_ClockwiseOuterSpiralTraversalList_3x4():
    result = ClockwiseOuterSpiralTraversalList(3, 4)
    expected = [
        [0, 0], [1, 0], [2, 0], [3, 0],
        [3, 1], [3, 2], [2, 2], [1, 2],
        [0, 2], [0, 1], [1, 1], [2, 1]
    ]
    assert result == expected

def test_ClockwiseOuterSpiralTraversalList_4x3():
    result = ClockwiseOuterSpiralTraversalList(4,3)
    expected = [
        [0, 0], [1, 0], [2, 0],
        [2, 1], [2, 2], [2, 3],
        [1, 3], [0, 3], [0, 2],
        [0, 1], [1, 1], [1, 2]
    ]
    assert result == expected