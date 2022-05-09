from collections import OrderedDict


class User:
    def __init__(self, username="", idx=0):
        self.idx = idx
        self.username = username
        self.count = 0
        self.report_list = []

    def __str__(self):
        return f"{self.username} {self.count} {self.report_list}"

    def __repr__(self):
        return f"{self.username} {self.count} {self.report_list}"


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    user_dict = OrderedDict()
    for idx, user in enumerate(id_list):
        user_dict[user] = user_dict.get(user, User(user, idx))

    for r in report:
        reporting_user, reported_user = r.split(" ")
        if reporting_user in user_dict[reported_user].report_list:
            continue
        user_dict[reported_user].report_list.append(reporting_user)
        user_dict[reported_user].count += 1

    print(user_dict)
    for key, user in user_dict.items():
        if user.count >= k:
            for reporting_user in user.report_list:
                answer[user_dict[reporting_user].idx] += 1
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"],
         ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))

print(solution(["con", "ryan"],
         ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
