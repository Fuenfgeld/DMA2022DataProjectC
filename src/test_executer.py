from logger import Logger
class TestExecutor:
    testLogger = None
    resultLogger = None

    def __init__(self, logger):
        # The result logger is used to log whether or not a test was successful.
        self.resultLogger = logger

        # The test logger is handed to the unit tests so that they do not log any output.
        # We therefore override the log method so that it does not print anything.
        self.testLogger = Logger()
        self.testLogger.log = lambda _self, _message: None

    def execute(self, description, test):
        try:
            test(self.testLogger)

            self.resultLogger.log(f"✅ Test ran successfully: {description}")
        except Exception as exception:
            self.resultLogger.log(f"❌ Test failed: {description}", exception.args)