from django.shortcuts import render, render_to_response
from app.models import User, Answer, Option, Weight, Criteria


def questionnairy_page(request):
    questions = [{'id': 5, 'title': 'question1', 'description': 'description1'},
                 {'id': 2, 'title': 'question2', 'description': 'description2'}]
    options = [{'id': 6, 'title': 'option1'}, {
        'id': 7, 'title': 'option2'}, {'id': 10, 'title': 'option3'}]
    return render_to_response('questionnairy.html', {'questions': questions, 'options': options})


def welcome_page(request):
    return render(request, 'welcome.html')


def resu(request):
    #it can only be one leader, otherweise it will bug!!!
    users = User.objects.all()
    answers = Answer.objects.all()
    options = Option.objects.all()
    criterias = Criteria.objects.all()

    def get_results_no_weight(users, answers, options, criterias):
        l = []
        individual_results = {}
        group_results = {}
        for user in users:
            l.append(user)
            maxi = [None, None]
            for option in options:
                l.append(option.name)
                for answer in answers:
                    if answer.user == user and answer.option == option:
                        l.append(answer.magnitude)
                    r_stri = "result " + user.first_name + " " + option.name + ": "
                    l.append(r_stri)
                    n = len(l) - 2
                    m = 0
                    while isinstance(l[n], int):
                        m = m + l[n]
                        n = n - 1
                    l.append(m)
                if option in group_results:
                    group_results[option] += m
                else:
                    group_results[option] = m
                if maxi[0] == None or maxi[1] < m:
                    maxi[0] = r_stri
                    maxi[1] = m
            individual_results[maxi[0]] = maxi[1]
            results = {"individual_results": individual_results,
                       "group_results": group_results}
        return results

    def get_results_with_weight(users, answers, options, criterias):
        l2 = []
        individual_results = {}
        group_results = {}

        for user in users:
            l2.append(user)
            maxi2 = [None, None]
            for option in options:
                l2.append(option.name)
                for c in criterias:
                    for answer in answers:
                        if answer.user == user and answer.option == option and answer.criteria == c:
                            w = Weight.objects.filter(
                                user=user).filter(criteria=c)
                            l2.append(answer.magnitude * w[0].weight)
                r_stri = "result " + user.first_name + " " + option.name + ": "
                l2.append(r_stri)
                n = len(l2) - 2
                m = 0
                while isinstance(l2[n], int):
                    m = m + l2[n]
                    n = n - 1
                l2.append(m)
                if option in group_results:
                    group_results[option] += m
                else:
                    group_results[option] = m
                if maxi2[0] == None or maxi2[1] < m:
                    maxi2[0] = r_stri
                    maxi2[1] = m
            individual_results[maxi2[0]] = maxi2[1]
            results = {"individual_results": individual_results,
                       "group_results": group_results}
        return results

    def get_results_leaders_weight(users, answers, options, criterias):
        l3 = []
        individual_results = {}
        group_results = {}

        for user in users:
            l3.append(user)
            maxi3 = [None, None]
            for option in options:
                l3.append(option.name)
                for c in criterias:
                    for answer in answers:
                        if answer.user == user and answer.option == option and answer.criteria == c:
                            lead = User.objects.filter(leader=1)
                            w = Weight.objects.filter(
                                user=lead).filter(criteria=c)
                            l3.append(answer.magnitude * w[0].weight)
                r_stri = "result " + user.first_name + " " + option.name + ": "
                l3.append(r_stri)
                n = len(l3) - 2
                m = 0
                while isinstance(l3[n], int):
                    m = m + l3[n]
                    n = n - 1
                l3.append(m)
                if option in group_results:
                    group_results[option] += m
                else:
                    group_results[option] = m
                if maxi3[0] == None or maxi3[1] < m:
                    maxi3[0] = r_stri
                    maxi3[1] = m
            individual_results[maxi3[0]] = maxi3[1]
            results = {"individual_results": individual_results,
                       "group_results": group_results}
        return results

    individual_results = get_results_no_weight(
        users, answers, options, criterias)["individual_results"]
    group_results = get_results_no_weight(
        users, answers, options, criterias)["group_results"]
    group_result = {max(group_results, key=group_results.get)                    : group_results[max(group_results, key=group_results.get)]}

    individual_results_with_weight = get_results_with_weight(
        users, answers, options, criterias)["individual_results"]
    group_results_with_weight = get_results_with_weight(
        users, answers, options, criterias)["group_results"]
    group_result_with_weight = {max(group_results_with_weight, key=group_results_with_weight.get): group_results_with_weight[max(group_results_with_weight, key=group_results_with_weight.get)]}

    individual_results_with_leaders_weight = get_results_leaders_weight(
        users, answers, options, criterias)["individual_results"]
    group_results_with_leaders_weight = get_results_leaders_weight(
        users, answers, options, criterias)["group_results"]
    group_result_with_leaders_weight = {max(group_results_with_leaders_weight, key=group_results_with_leaders_weight.get): group_results_with_leaders_weight[max(group_results_with_leaders_weight, key=group_results_with_leaders_weight.get)]}

    return render(request, 'resu.html', {"individual_results": individual_results, "group_result": group_result,
                                         "individual_results_with_weight": individual_results_with_weight, "group_result_with_weight": group_result_with_weight, "individual_results_with_leaders_weight": individual_results_with_leaders_weight, "group_result_with_leaders_weight" : group_result_with_leaders_weight})
