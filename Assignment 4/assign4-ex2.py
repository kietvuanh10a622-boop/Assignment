def check_prototype(prototype):
    if prototype[0] != '#':
        return False
    elif len(prototype) != 7:
        return False
    check = prototype[1:]
    hex_real = "0123456789abcdefABCDEF"
    for char in check:
      if char not in hex_real:
          return False
    return True


print(check_prototype('#abc123'))

