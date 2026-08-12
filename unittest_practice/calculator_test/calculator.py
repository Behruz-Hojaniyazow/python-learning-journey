class Calculator:
    def __init__(self, logger):
        self.logger = logger

    def safe_divide(self, a, b):
        """Divide a by b, logging and returning None on any failure."""
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            self.logger.error("Division by zero attempted")
            return None
        except TypeError:
            self.logger.error("Invalid types for division")
            return None
        except Exception:
            self.logger.exception("Unexpected error during division")
            return None