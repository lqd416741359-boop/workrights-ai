#!/usr/bin/env python3
"""Arithmetic helpers for WorkRights AI.
This module does NOT determine legal eligibility. Verified legal rules and case facts must be supplied by the caller.
"""
from decimal import Decimal, ROUND_HALF_UP


def money(value):
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def multiply(base, factor):
    """Generic transparent multiplication helper, e.g. verified wage base × verified factor."""
    return money(Decimal(str(base)) * Decimal(str(factor)))


def sum_items(items):
    """Sum already-established monetary items."""
    return money(sum(Decimal(str(x)) for x in items))
