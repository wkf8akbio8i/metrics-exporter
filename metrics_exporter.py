"""A minimal metrics registry with counters, gauges and histograms."""

from __future__ import annotations

__all__ = ["metricsExporter"]


def metricsExporter(value):
    """A minimal metrics registry with counters, gauges and histograms."""
    if value is None:
        raise ValueError("value must not be None")
    return value
