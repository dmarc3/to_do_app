""" Command line interface for to_do_app """
import sys
import logging
import argparse
from typing import List
from to_do_app.main import * # pylint: disable=wildcard-import
from to_do_app import __version__

_logger = logging.getLogger(__name__)


def setup_logging(loglevel: int):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def parse_args(args: List[str]) -> argparse.Namespace:
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Application to track todo tasks.",
        formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=45)
    )
    # Add version command
    parser.add_argument(
        "--version",
        action="version",
        version=f"to_do_app {__version__}",
    )
    # Add verbosity command
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )
    # Add custom commands
    act = 'store_true'
    commands = [["-a", "--add_task", add_task.__doc__, False, act],
                ["-l", "--list_tasks", list_tasks.__doc__, False, act],
                ["-ssd", "--set_start_date", set_start_date.__doc__, False, act],
                ["-sdd", "--set_due_date", set_due_date.__doc__, False, act],
                ["-m", "--mark_complete", mark_complete.__doc__, False, act],
                ["-d", "--delete_task", delete_task.__doc__, False, act],
                ["-cn", "--change_task_name", change_task_name.__doc__, False, act],
                ["-cd", "--change_task_description", change_task_description.__doc__, False, act]]
    for command in commands:
        parser.add_argument(command[0],
                            command[1],
                            help=command[2],
                            required=command[3],
                            action=command[4])
    return parser.parse_args(args)


def main(args: List[str]):
    """Wrapper allowing functions to be called with string arguments in a CLI fashion

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "42"]``).
    """
    args = parse_args(args)
    # Set verbosity level
    setup_logging(args.loglevel)
    # Process arguments
    funcs = [add_task, list_tasks, set_start_date,
            set_due_date, mark_complete, delete_task,
            change_task_name, change_task_description]
    for func in funcs:
        if getattr(args, func.__name__):
            _logger.info("Executing %s: %s...", func.__name__, func.__doc__)
            if func():
                _logger.info("%s completed successfully.", func.__name__)
            else:
                _logger.error("%s completed unsuccessfully.", func.__name__)


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`
    """
    main(sys.argv[1:])
