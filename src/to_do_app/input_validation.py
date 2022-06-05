""" Input validation methods """
import logging
from validx import Dict, Str, Int, Datetime, exc

_logger = logging.getLogger(__name__)

_validator = Dict(
    dict(
        task_name = Str(minlen=3, maxlen=100),
        task_description = Str(minlen=10, maxlen=500),
        task_start_date = Datetime(format='%Y-%m-%d'),
        task_due_date = Datetime(format='%Y-%m-%d'),
        task_status = Str(options=['ACTIVE', 'NOT STARTED', 'COMPLETED', 'DELETED']),
        task_priority = Int(min=1, max=10),
    ),
    optional=['task_name', 'task_description', 'task_start_date',
              'task_due_date', 'task_status', 'task_priority']
)

_formatter = exc.format_error

def validate_input(inp: dict) -> bool:
    """Validates input

    Args:
        inp (dict): Dictionary containing inputs to be validated.

    Returns:
        bool: Boolean describing validity of input.
    """
    try:
        if _validator(inp):
            return True
    except exc.ValidationError as error:
        # Log useful error message
        for suberror in error:
            key = suberror.context[0]
            formatted_error = list(_formatter(suberror)[0])
            formatted_error[0] = formatted_error[0].replace('_', ' ').upper() + \
                                 ': "' + inp[key] + '"'
            _logger.error(' -> '.join(formatted_error))
        return False
