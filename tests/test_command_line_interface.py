
from to_do_app.command_line_interface import main
__author__ = "Marcus Bakke"


# def test_main_add_task(mocker):
#     """CLI Tests"""
#     # capsys is a pytest fixture that allows asserts agains stdout/stderr
#     # https://docs.pytest.org/en/stable/capture.html
#     add_task = mocker.patch('to_do_app.main.add_task')
#     add_task.return_value = True
#     main(["-a"])
#     pdb.set_trace()
#     add_task.assert_called()