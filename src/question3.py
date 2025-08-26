
from fractions import Fraction


def get_min_turns(distance: int):
    return (distance + 2) // 3


def get_prob_optimal(distance: int, min_turns: int) -> float:
    ratio = distance % 3
    optimal_count = min_turns
    if ratio == 0:
        optimal_count = 1

    total_sequence_len = 3 ** min_turns
    prob_optimal = Fraction(optimal_count, total_sequence_len)
    prob_optimal_float = float(prob_optimal)
    return prob_optimal_float


def get_loop_free_combination(distance: int) -> int:
    if distance == 1:
        return 1
    elif distance == 2:
        return 2
    
    f0, f1, f2 = 1, 1, 2 # f(0), f(1), f(2)
    for _ in range(3, distance + 1):
        f0, f1, f2 = f1, f2, f0 + f1 + f2
    return f2


def get_game_info(spaces: int) -> dict:

    if not isinstance(spaces, int) or spaces < 3:
        raise ValueError("O valor das casas deve ser maior que 2")
    
    distance = spaces - 1
    min_turns = get_min_turns(distance)
    prob_optimal = get_prob_optimal(distance, min_turns)
    loop_free = get_loop_free_combination(distance)

    return {
        "minimum_turns": min_turns,
        "optimal_probability": prob_optimal, 
        "loop_free_combinations": loop_free, 
    }


if __name__ == "__main__":
    for n in [3, 4, 5, 6, 10]:
        print(f"f({n}): ",get_game_info(n))
    
    
    