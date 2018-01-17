from app.models import WeightedCriteria, Option, Criteria, Answer


def answer_scores(criterion, option):
    return map(lambda answer: answer.score, Answer.objects.filter(criteria=criterion, option=option))


def mean_weight(criterion):
    weights = list(weighted.weight for weighted in WeightedCriteria.objects.filter(criteria=criterion))
    return float(sum(weights)) / len(weights)


def calculate_mean(option):
    criteria = Criteria.objects.filter(decision=option.decision)
    return sum(sum(answer_scores(criterion, option)) * mean_weight(criterion) for criterion in criteria)


def calculate_normal(option):
    criteria = Criteria.objects.filter(decision=option.decision)
    return sum(sum(answer_scores(criterion, option)) * criterion.weight for criterion in criteria)


def group_solution(decision):
    options = Option.objects.filter(decision=decision)
    return max(options, key=lambda option: calculate_mean(option))


def normal_solution(decision):
    options = Option.objects.filter(decision=decision)
    return max(options, key=lambda option: calculate_normal(option))
