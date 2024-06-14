import pytest

from utils.file_tools import FileTool

"""
conftest.py使用说明
添加了@pytest.fixture的方法，可以在测试用例中使用
def test_a(env_config):
    assert 1 == 1
"""


def pytest_addoption(parser):
    """
    定义一个命令行参数
    :param parser:
    :return:
    """
    parser.addoption("--env", action="store", default="tp", help="Environment to run tests against (q1, tp)")


@pytest.fixture(scope="session")
def env_config(request):
    # yaml_data = FileTool.read_yaml("config")
    env = request.config.getoption("--env")
    # return yaml_data.get("env").get(env)
    return env
