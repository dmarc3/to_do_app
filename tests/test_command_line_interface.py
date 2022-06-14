""" Unittests for command line interface. Test arguments. """
from unittest.mock import Mock, patch
from to_do_app.command_line_interface import main
__author__ = "Marcus Bakke"


def test_cli_add_task():
    """CLI add_task tests"""
    getattr_mock = Mock()
    getattr_mock.return_value = False
    for arg in ['-a', '--add_task']:
        with patch('to_do_app.command_line_interface.getattr', getattr_mock) as mock:
            main([arg])
            mock.assert_called()
            args = mock.call_args_list[0][0][0]
            assert args.add_task == []
            assert not args.list_tasks
            assert not args.set_start_date
            assert not args.set_due_date
            assert not args.mark_complete
            assert not args.delete_task
            assert not args.change_task_name
            assert not args.change_task_description

def test_cli_list_tasks():
    """CLI list_tasks tests"""
    getattr_mock = Mock()
    getattr_mock.return_value = False
    for arg in ['-l', '--list_tasks']:
        with patch('to_do_app.command_line_interface.getattr', getattr_mock) as mock:
            main([arg])
            mock.assert_called()
            args = mock.call_args_list[1][0][0]
            assert not args.add_task
            assert args.list_tasks
            assert not args.set_start_date
            assert not args.set_due_date
            assert not args.mark_complete
            assert not args.delete_task
            assert not args.change_task_name
            assert not args.change_task_description

def test_cli_set_start_date():
    """CLI set_start_date tests"""
    getattr_mock = Mock()
    getattr_mock.return_value = False
    for arg in ['-ssd', '--set_start_date']:
        with patch('to_do_app.command_line_interface.getattr', getattr_mock) as mock:
            main([arg])
            mock.assert_called()
            args = mock.call_args_list[2][0][0]
            assert not args.add_task
            assert not args.list_tasks
            assert args.set_start_date == []
            assert not args.set_due_date
            assert not args.mark_complete
            assert not args.delete_task
            assert not args.change_task_name
            assert not args.change_task_description

def test_cli_set_due_date():
    """CLI set_due_date tests"""
    getattr_mock = Mock()
    getattr_mock.return_value = False
    for arg in ['-sdd', '--set_due_date']:
        with patch('to_do_app.command_line_interface.getattr', getattr_mock) as mock:
            main([arg])
            mock.assert_called()
            args = mock.call_args_list[3][0][0]
            assert not args.add_task
            assert not args.list_tasks
            assert not args.set_start_date
            assert args.set_due_date == []
            assert not args.mark_complete
            assert not args.delete_task
            assert not args.change_task_name
            assert not args.change_task_description

def test_cli_mark_complete():
    """CLI mark_complete tests"""
    getattr_mock = Mock()
    getattr_mock.return_value = False
    for arg in ['-m', '--mark_complete']:
        with patch('to_do_app.command_line_interface.getattr', getattr_mock) as mock:
            main([arg])
            mock.assert_called()
            args = mock.call_args_list[4][0][0]
            assert not args.add_task
            assert not args.list_tasks
            assert not args.set_start_date
            assert not args.set_due_date
            assert args.mark_complete == []
            assert not args.delete_task
            assert not args.change_task_name
            assert not args.change_task_description

def test_cli_delete_task():
    """CLI delete_task tests"""
    getattr_mock = Mock()
    getattr_mock.return_value = False
    for arg in ['-d', '--delete_task']:
        with patch('to_do_app.command_line_interface.getattr', getattr_mock) as mock:
            main([arg])
            mock.assert_called()
            args = mock.call_args_list[5][0][0]
            assert not args.add_task
            assert not args.list_tasks
            assert not args.set_start_date
            assert not args.set_due_date
            assert not args.mark_complete
            assert args.delete_task == []
            assert not args.change_task_name
            assert not args.change_task_description

def test_cli_change_task_name():
    """CLI change_task_name tests"""
    getattr_mock = Mock()
    getattr_mock.return_value = False
    for arg in ['-cn', '--change_task_name']:
        with patch('to_do_app.command_line_interface.getattr', getattr_mock) as mock:
            main([arg])
            mock.assert_called()
            args = mock.call_args_list[6][0][0]
            assert not args.add_task
            assert not args.list_tasks
            assert not args.set_start_date
            assert not args.set_due_date
            assert not args.mark_complete
            assert not args.delete_task
            assert args.change_task_name == []
            assert not args.change_task_description

def test_cli_change_task_description():
    """CLI change_task_description tests"""
    getattr_mock = Mock()
    getattr_mock.return_value = False
    for arg in ['-cd', '--change_task_description']:
        with patch('to_do_app.command_line_interface.getattr', getattr_mock) as mock:
            main([arg])
            mock.assert_called()
            args = mock.call_args_list[7][0][0]
            assert not args.add_task
            assert not args.list_tasks
            assert not args.set_start_date
            assert not args.set_due_date
            assert not args.mark_complete
            assert not args.delete_task
            assert not args.change_task_name
            assert args.change_task_description == []

class ArgumentParserError(Exception):
    """Custom exception for argparse error test"""

def test_num_args():
    """CLI number of arguments tests"""
    parser_mock = Mock()
    parser_mock.side_effect = ArgumentParserError()
    with patch('argparse.ArgumentParser.error', parser_mock) as mock:
        try:
            main(['-a', 'Task']) # no description provided
        except ArgumentParserError:
            mock.assert_called()
            assert mock.call_args[0][0] == 'add_task must be called ' \
                                            'with 3 arguments or none at all.'
