import pytest
from testcases.conftest import api_data


@pytest.fixture(scope="function")
def testcase_data(request):
    """根据当前测试函数名,自动获取对应的测试数据"""
    testcase_name = request.function.__name__
    return api_data.get(testcase_name)