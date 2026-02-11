import pytest
import weather_checker

class DummyResponse:
    def __init__(self):
        self.data = {"hourly": {"temperature_2m": [1,2,3,4,5]}}
    def json(self):
        return(self.data)
    def raise_for_status(self):
        pass

def dummy_request(*args, **kwargs):
    return DummyResponse()

def test_weather_checker(monkeypatch):
    monkeypatch.setattr(weather_checker.requests, "get", dummy_request)
    forecast = weather_checker.weather_checker()
    forecast_transfered = {f"Hour {k}": v for k, v in forecast.items()}

    assert forecast_transfered == {
        "Hour 0": 1,
        "Hour 1": 2,
        "Hour 2": 3,
        "Hour 3": 4,
        "Hour 4": 5,
    }