#!/usr/bin/env python3
"""A function called filter_datum that returns the log message obfuscated"""


import logging


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Filter data function"""
    for field in fields:
        message = re.sub(rf"{field}=(.*?)\{separator}",
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor"""
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Formater"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
