""" Unittests for command line interface """
from to_do_app.command_line_interface import main
__author__ = "Marcus Bakke"


def test_cli_add_task(mocker):
    """CLI add_task tests"""
    func = mocker.patch('to_do_app.command_line_interface.getattr')
    func.return_value = True
    for arg in ['-a', '--add_task']:
        main([arg])
        func.assert_called()
        args = func.call_args_list[0][0][0]
        assert args.add_task
        assert not args.list_tasks
        assert not args.set_start_date
        assert not args.set_due_date
        assert not args.mark_complete
        assert not args.delete_task
        assert not args.change_task_name
        assert not args.change_task_description

def test_cli_list_tasks(mocker):
    """CLI list_tasks tests"""
    func = mocker.patch('to_do_app.command_line_interface.getattr')
    func.return_value = True
    for arg in ['-l', '--list_tasks']:
        main([arg])
        func.assert_called()
        args = func.call_args_list[1][0][0]
        assert not args.add_task
        assert args.list_tasks
        assert not args.set_start_date
        assert not args.set_due_date
        assert not args.mark_complete
        assert not args.delete_task
        assert not args.change_task_name
        assert not args.change_task_description

def test_cli_set_start_date(mocker):
    """CLI set_start_date tests"""
    func = mocker.patch('to_do_app.command_line_interface.getattr')
    func.return_value = True
    for arg in ['-ssd', '--set_start_date']:
        main([arg])
        func.assert_called()
        args = func.call_args_list[2][0][0]
        assert not args.add_task
        assert not args.list_tasks
        assert args.set_start_date
        assert not args.set_due_date
        assert not args.mark_complete
        assert not args.delete_task
        assert not args.change_task_name
        assert not args.change_task_description

def test_cli_set_due_date(mocker):
    """CLI set_due_date tests"""
    func = mocker.patch('to_do_app.command_line_interface.getattr')
    func.return_value = True
    for arg in ['-sdd', '--set_due_date']:
        main([arg])
        func.assert_called()
        args = func.call_args_list[3][0][0]
        assert not args.add_task
        assert not args.list_tasks
        assert not args.set_start_date
        assert args.set_due_date
        assert not args.mark_complete
        assert not args.delete_task
        assert not args.change_task_name
        assert not args.change_task_description

def test_cli_mark_complete(mocker):
    """CLI mark_complete tests"""
    func = mocker.patch('to_do_app.command_line_interface.getattr')
    func.return_value = True
    for arg in ['-m', '--mark_complete']:
        main([arg])
        func.assert_called()
        args = func.call_args_list[4][0][0]
        assert not args.add_task
        assert not args.list_tasks
        assert not args.set_start_date
        assert not args.set_due_date
        assert args.mark_complete
        assert not args.delete_task
        assert not args.change_task_name
        assert not args.change_task_description

def test_cli_delete_task(mocker):
    """CLI delete_task tests"""
    func = mocker.patch('to_do_app.command_line_interface.getattr')
    func.return_value = True
    for arg in ['-d', '--delete_task']:
        main([arg])
        func.assert_called()
        args = func.call_args_list[5][0][0]
        assert not args.add_task
        assert not args.list_tasks
        assert not args.set_start_date
        assert not args.set_due_date
        assert not args.mark_complete
        assert args.delete_task
        assert not args.change_task_name
        assert not args.change_task_description

def test_cli_change_task_name(mocker):
    """CLI change_task_name tests"""
    func = mocker.patch('to_do_app.command_line_interface.getattr')
    func.return_value = True
    for arg in ['-cn', '--change_task_name']:
        main([arg])
        func.assert_called()
        args = func.call_args_list[6][0][0]
        assert not args.add_task
        assert not args.list_tasks
        assert not args.set_start_date
        assert not args.set_due_date
        assert not args.mark_complete
        assert not args.delete_task
        assert args.change_task_name
        assert not args.change_task_description

def test_cli_change_task_description(mocker):
    """CLI change_task_description tests"""
    func = mocker.patch('to_do_app.command_line_interface.getattr')
    func.return_value = True
    for arg in ['-cd', '--change_task_description']:
        main([arg])
        func.assert_called()
        args = func.call_args_list[7][0][0]
        assert not args.add_task
        assert not args.list_tasks
        assert not args.set_start_date
        assert not args.set_due_date
        assert not args.mark_complete
        assert not args.delete_task
        assert not args.change_task_name
        assert args.change_task_description
