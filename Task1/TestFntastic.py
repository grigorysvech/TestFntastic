def convert(string):
    string = string.lower()
    repeats = dict()
    for i in string:
        if i in repeats.keys():
            repeats[i] += 1
        else:
            repeats[i] = 1
            
    result = ""
    for i in string:
        if repeats[i] > 1:
            result += ")"
        else:
            result += "("
    return result


test = {
    "din":"(((",
    "recede":"()()()",
    "Success":")())())",
    "(( @":"))(("
}


for key, value in test.items():
    if convert(key) == value:
        print(f'Test passed "{key}" => "{value}"')
    else:
        print("----------------------------------")
        print(f'Error    "{key}" => "{convert(key)}"')
        print(f'Expected "{key}" => "{value}"')
        print("----------------------------------")