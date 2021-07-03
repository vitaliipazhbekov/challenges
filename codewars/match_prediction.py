# Match score is X:Y, user prediction is A:B.
# If user predicts the result of the match - user gets 10 point
# If user predicts the win or lose or draw - user gets 5 point
# If user make a mistake - user gets nothing


def f(x, y, a, b):
    score = 0

    if x == a and b == y:
        score = 10

    elif x > y and a > b or y > x and b > a or a == b and x == y:
        score = 5

    return score
