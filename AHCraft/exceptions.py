class ProcessNotFoundError(Exception):
    """ For when AHK was not able to find the process """
    pass


class AHKMissingError(Exception):
    """ When AHK is missing or not installed """
    pass


class AHKFailedReturnError(Exception):
    """ When AHK grants a return code of 0 """
    pass


class AHKScriptMissingError(Exception):
    """ When the AHK Script has been misplaced or renamed"""
    pass