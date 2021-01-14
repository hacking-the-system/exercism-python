def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_three = []
    while len(scores) > 0 and len(top_three) < 3:
        top = max(scores)
        top_three.append(top)
        scores.remove(top)
    return top_three
