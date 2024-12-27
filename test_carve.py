import pytest 
from seamcarve import SeamCarve


def test_seamcarve():
   
    test_image = [[[255, 255, 255], [0, 0, 0], [125, 125, 125], [0, 0, 0],\
        [255, 255, 255]], [[0, 0, 0], [125, 125, 125], [0, 0, 0],
        [255, 255, 255], [0, 0, 0]], [[255, 255, 255], [125, 125, 125],
        [255, 255, 255], [0, 0, 0], [255, 255, 255]], [[0, 0, 0],
        [255, 255, 255], [125, 125, 125], [255, 255, 255], [0, 0, 0]], 
        [[255, 255, 255], [0, 0, 0], [255, 255, 255], [125, 125, 125],
        [255, 255, 255]]]
    expected_seam = [2, 1, 1, 2, 3]

    my_sc = SeamCarve(image_matrix = test_image)

    importance_vals = my_sc.calculate_importance_values()
    calculated_seam = my_sc.find_least_important_seam(importance_vals)

    test_vals1 = [0, 0, 0, 0, 0]
    test_vals2 = [0, 5, 3, -1, 2]
    test_vals3 = [10, 8, 27, 8, 13]
    test_vals4 = [5]
    test_vals5 = []

    assert my_sc.argmin(test_vals1) == 0
    assert my_sc.argmin(test_vals2) == 3
    assert my_sc.argmin(test_vals3) == 1
    assert my_sc.argmin(test_vals4) == 0

    
    #assert expected_seam == calculated_seam