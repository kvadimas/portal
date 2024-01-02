import time
import requests
import json
import logging

from portal.settings import FORECAST_URL

logger = logging.getLogger("__name__")


class ThrottlingForecasts:
    """Троттлинг для запуска предсказательного сервиса."""
    def __init__(self, limit, interval):
        self.limit = limit
        self.interval = interval  # В секундах
        self.tokens = 0
        self.last_time = time.time()

    def __call__(self):
        current_time = time.time()
        time_passed = current_time - self.last_time
        self.tokens += (time_passed / self.interval) * self.limit
        self.tokens = min(self.tokens, self.limit)
        self.last_time = current_time

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False

    def reset_tokens(self):
        self.tokens = 0


def forecast(message: str):
    try:
        headers = {'content-type': 'application/json'}
        data = json.dumps({"text": message})
        r = requests.post(FORECAST_URL, headers=headers, data=data, timeout=60)

        if r.status_code == 200:
            logger.info(f"Processing from the Forecasting API: HTML {r.status_code}")
            return r.json()
        else:
            logger.warning(f"Processing from the Forecasting API: Error {r.status_code}")
            return {"error": f"Processing from the Forecasting API: Error {r.status_code}"}
    except:
        logger.warning("Error: I can't connect to the forecast service.")
        return {"error": "I can't connect to the forecast service."}
