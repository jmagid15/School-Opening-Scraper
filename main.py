import logging
from timeit import default_timer as timer
import importlib
import os

# Runs all state scripts that are currently available
if __name__ == '__main__':
    # disabledStates = ["arizona", "virginia"]
    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
    # Currently working states <-- ADD STATES BELOW
    currentStates = ["alabama", "colorado", "illinois", "new_mexico", "maryland", "ohio", "oregon", "south_carolina",
                     "tennessee", "washington", "north_carolina", "connecticut", "rhode_island"]

	# Set-up necessary subdirectories
    for folder in ["temp", "out"]:
        if not os.path.isdir(folder):
            try:
                os.mkdir(folder)
            except OSError:
                logging.error("Failed to create directory %s", folder, exc_info=False)

    # Import module for each state script
    modules = {}
    for state in currentStates:
        try:
            modules[state] = importlib.import_module(state)
            logging.info("Successfully Imported %s", state, exc_info=False)
        except ImportError:
            logging.error("Failed to import %s", state, exc_info=True)

    # Lists to store scripts that either fail or succeed in running
    successes = []
    failures = []

    startTimer = timer() # Begin timer

    # Run scripts for each working state, catch and denote failures
    for state in currentStates:
        try:
            exec("modules['{stateName}'].main()".format(stateName=state))
            successes.append(state)
            logging.info("Successfully Fetched %s", state, exc_info=False)
        except Exception:
            logging.error("Failed to fetch %s", state, exc_info=True)
            failures.append(state)

    endTimer = timer() # End timer
    elapsed = endTimer - startTimer # Calculate elapsed time to fetch state data

    # Print results
    logging.info("Fetched data for " + str(successes) + " in " + str(elapsed) + " seconds.", exc_info=False);
    logging.info("Failed to fetch: " + str(failures), exc_info=False);



