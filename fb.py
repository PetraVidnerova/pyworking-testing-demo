def fizzbuzz(number):
    ret = ''
    if number % 3 == 0:
        ret += 'fix'
    if number % 5 == 0:
        ret += 'buzz'
    return ret or str(number)
 
