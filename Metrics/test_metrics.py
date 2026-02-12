import pytest
from metrics import collect_metrics

def test_metrics_value():
    metrics = collect_metrics()

    for key in ["timestamp", "cpu_percentage", "memory_percentage", "disk_percentage"]:
        assert key in metrics
    assert isinstance(metrics["cpu_percentage"], float)
    assert isinstance(metrics["memory_percentage"], float)
    assert isinstance(metrics["disk_percentage"], float)
