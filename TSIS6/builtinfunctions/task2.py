def count_case(string):
    upper_case = sum(1 for c in string if c.isupper())
    lower_case = sum(1 for c in string if c.islower())
    return {'upper_case': upper_case, 'lower_case': lower_case}