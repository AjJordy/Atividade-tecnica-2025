
LINEAR_COEFFICIENT = 11
ANGULAR_COEFFICIENT = 7

def get_value_by_position(position: int) -> int:
    return (position - 1) * ANGULAR_COEFFICIENT + LINEAR_COEFFICIENT


if __name__ == "__main__":
    print("f(x=1): ",get_value_by_position(1)) # 11
    print("f(x=2): ",get_value_by_position(2)) # 18
    print("f(x=200): ",get_value_by_position(200)) # 1404
    print("f(x=254): ",get_value_by_position(254)) # 1782
    print("f(x=3542158): ",get_value_by_position(3542158)) # 24.795.110