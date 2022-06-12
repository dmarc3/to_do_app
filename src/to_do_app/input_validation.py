""" Input validation methods """
import logging
from validx import Dict, Str, Int, Datetime, exc

__author__ = "Marcus Bakke"
_logger = logging.getLogger(__name__)

_validator = Dict(
    dict(
        task_id = Int(),
        name = Str(minlen=3, maxlen=100),
        description = Str(minlen=10, maxlen=500),
        start_date = Datetime(format='%Y-%m-%d'),
        due_date = Datetime(format='%Y-%m-%d'),
        status = Str(options=['ACTIVE', 'COMPLETED', 'DELETED']),
        priority = Str(options=[str(x) for x in range(1, 11)]),
    ),
    optional=['task_id', 'name', 'description', 'start_date', 'due_date',
              'status', 'priority']
)
_formatter = exc.format_error

def validate_input(inputs: dict) -> bool:
    """Validates input

    Args:
        inputs (dict): Dictionary containing inputs to be validated.

    Returns:
        bool: Boolean describing validity of input.
    """
    # Convert task_id to integer
    try:
        if 'task_id' in inputs:
            inputs['task_id'] = int(inputs['task_id'])
    except (TypeError, ValueError) as error:
        _logger.error(error.args[0])
    # Pass inputs into validator
    try:
        _validator(inputs)
        # Validator succeeded
        return True
    except exc.ValidationError as error:
        # Log useful error message
        for suberror in error:
            key = suberror.context[0]
            formatted_error = list(_formatter(suberror)[0])
            formatted_error[0] = formatted_error[0].replace('_', ' ').upper() + \
                                ': "' + str(inputs[key]) + '"'
            _logger.error(' -> '.join(formatted_error))
    # Validator failed
    _logger.error('Validation failed.')
    return False

def get_valid_input(attr: str, prompt: str, inputs=dict()) -> dict:
    """Prompts user for valid input

    Args:
        attr (str): Database attribute user is being prompted for input of
        prompt (str): Prompt text
        inputs (dict, optional): Dictionary of inputs to be validated. Defaults to dict().

    Returns:
        dict: Dictionary containing the validated user response
    """
    inputs[attr] = input(prompt)
    while not validate_input(inputs):
        inputs[attr] = input(prompt)
    return inputs
