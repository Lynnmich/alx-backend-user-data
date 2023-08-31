#!/usr/bin/env python3
"""A function called filter_datum that returns the log message obfuscated"""


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Filter data function"""
    for field in fields:
        message = re.sub(rf"{field}=(.*?)\{separator}",
                         f'{field}={redaction}{separator}', message)
    return message
