""" Command line interface for to_do_app """
import sys
import logging
import argparse
from typing import List
import to_do_app.logger # pylint: disable=unused-import
from to_do_app.main import  add_task, list_tasks, set_start_date
from to_do_app.main import  set_due_date, mark_complete, delete_task
from to_do_app.main import  change_task_name, change_task_description
from to_do_app.task import TaskCollection
from to_do_app import __version__

__author__ = "Marcus Bakke"
_logger = logging.getLogger(__name__)

def update_log_level(loglevel: int):
    """Updates root logger log level per verbosity argument

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logger = logging.getLogger()
    logger.setLevel(loglevel)


def parse_args(arguments: List[str]) -> argparse.Namespace:
    """Parse command line parameters

    Args:
      arguments (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Application to track todo tasks.",
        formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=90)
    )
    # Add version command
    parser.add_argument(
        "--version",
        action="version",
        version=f"to_do_app {__version__}",
    )
    # Add silent command
    parser.add_argument(
        "-s",
        "--silent",
        dest="loglevel",
        help="set loglevel to CRITICAL",
        action="store_const",
        const=logging.CRITICAL,
        default=logging.INFO,
    )
    # Add verbosity command
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
        default=logging.INFO,
    )
    # Add custom commands
    commands = [["-a", "--add_task", add_task.__doc__, ('NAME DESCRIPTION PRIORITY')],
                ["-ssd", "--set_start_date", set_start_date.__doc__, ('TASK_ID START_DATE')],
                ["-sdd", "--set_due_date", set_due_date.__doc__, ('TASK_ID DUE_DATE')],
                ["-m", "--mark_complete", mark_complete.__doc__, ('TASK_ID CLOSED_DATE')],
                ["-d", "--delete_task", delete_task.__doc__, ('TASK_ID CLOSED_DATE')],
                ["-cn", "--change_task_name", change_task_name.__doc__, ('TASK_ID NAME')],
                ["-cd", "--change_task_description", change_task_description.__doc__,
                ('TASK_ID DESCRIPTION')]]
    for command in commands:
        parser.add_argument(command[0],
                            command[1],
                            help=command[2],
                            type=str,
                            nargs='*',
                            default=False,
                            metavar=command[3])
    parser.add_argument("-l",
                        "--list_tasks",
                        help=list_tasks.__doc__,
                        action='store_true')
    return parser.parse_args(arguments), parser


def main(arguments: List[str]):
    """Wrapper allowing functions to be called with string arguments in a CLI fashion

    Args:
      arguments (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "42"]``).
    """
    arguments, parser = parse_args(arguments)
    # Set verbosity level
    update_log_level(arguments.loglevel)
    _logger.debug(
        'Executing todo with the following arguments: %s',
        ', '.join(['--'+a+' '+str(v) for a, v in vars(arguments).items() if getattr(arguments, a)])
    )
    # Initialize Tasks class
    tasks = TaskCollection()
    # Process arguments
    funcs = {add_task: [3],
             list_tasks: None,
             set_start_date: [2],
             set_due_date: [2],
             mark_complete: [1, 2],
             delete_task: [1, 2],
             change_task_name: [2],
             change_task_description: [2]}
    for func, num in funcs.items():
        call_args = getattr(arguments, func.__name__)
        if isinstance(call_args, list) or call_args:
            # Confirm appropriate number of arguments provided
            if num and len(call_args) not in [0]+num:
                parser.error(func.__name__+f' must be called with {" or ".join([str(n) for n in num])} arguments'\
                            ' or none at all.')
            _logger.info("Executing %s: %s...", func.__name__, func.__doc__)
            if func(tasks, call_args):
                _logger.info("%s completed successfully.", func.__name__)
            else:
                _logger.error("%s completed unsuccessfully.", func.__name__)


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`
    """
    main(sys.argv[1:])
