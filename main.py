
def  add():
    a = [1, 7, 9, 4, 5]
    s = 9
    for index, i in enumerate(a):
        for index2, j in enumerate(a[index + 1:]):
            if i + j == s:
                print(index + 1, index2 + 2)

if __name__ == '__main__':
    ## 直接运行全部的测试用例
    import pytest
    pytest.main(['-sv'])
