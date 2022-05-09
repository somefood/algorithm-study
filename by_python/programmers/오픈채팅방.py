class User:
    def __init__(self, status, uid, nickname):
        self.status = None
        self.uid = uid
        self.nickname = nickname

    def __repr__(self):
        return f"{self.uid}, {self.nickname}"

    def __str__(self):
        return f"{self.uid}, {self.nickname}"


def solution(records):
    answer = []
    user_id = {}
    for record in records:
        result = record.split()
        status = result[0]
        uid = result[1]
        if status == "Enter":
            if uid in user_id:
                user_id[uid].nickname = result[2]
            else:
                user_id[uid] = User(status, uid, result[2])
            answer.append((user_id[uid], "님이 들어왔습니다."))
        elif status == "Leave":
            user_id[uid].status = status
            answer.append((user_id[uid], "님이 나갔습니다."))
        elif status == "Change":
            user_id[uid].nickname = result[2]

    return [i[0].nickname + i[1] for i in answer]


print(solution(["Enter uid1234 Muzi",
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan"]))