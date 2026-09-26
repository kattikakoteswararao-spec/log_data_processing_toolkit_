import time
import logging
from functools import wraps


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        try:
            result = func(*args, **kwargs)

            execution_time = time.time() - start_time

            logging.info(
                f"{func.__name__} completed in "
                f"{execution_time:.4f} seconds"
            )

            return result

        except Exception as error:
            execution_time = time.time() - start_time

            logging.error(
                f"{func.__name__} failed after "
                f"{execution_time:.4f} seconds: {error}"
            )

            raise

    return wrapper
