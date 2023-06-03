class ExitFromTheFuelAccessZone(Exception):
    """Exception raised when the drone trying to charge/fill more than 100%"""

    def __init__(self, message="Out from the fuel access zone!"):
        self.message = message
        super().__init__(self.message)
