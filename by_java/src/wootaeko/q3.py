def solution(ings, menu, sell):
    answer = 0
    ings_dict = {}
    menu_dict = {}

    for i in ings:
        ings_split = i.split()
        ings_dict[ings_split[0]] = int(ings_split[1])

    for m in menu:
        m_split = m.split()
        name = m_split[0]
        ingredients = m_split[1]
        price = int(m_split[2])
        ing_cost = 0
        for i in ingredients:
            ing_cost += ings_dict[i]
        menu_dict[name] = price - ing_cost

    for s in sell:
        s_split = s.split()
        name = s_split[0]
        sell_count = int(s_split[1])
        answer += menu_dict[name] * sell_count

    return answer


print(solution(["r 10", "a 23", "t 124", "k 9"],
               ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45",
                "JUICE rra 55", "WATER a 20"],
               ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]))

print(solution(["x 25", "y 20", "z 1000"],
               ["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"],
               ["BBBB 3", "TTT 2"]))