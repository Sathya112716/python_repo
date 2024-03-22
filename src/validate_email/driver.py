import logging

from util import is_valid_email

def fun(s):
    return is_valid_email(s)

n = int(input().strip())
emails = [input().strip() for _ in range(n)]

valid_emails = sorted(filter(fun, emails))
logging.debug(valid_emails)
