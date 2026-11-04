txt_index = "Ваш індекс Руф'є: "
txt_workheart = "Працездатність серця: "
txt_nodata = '''Немає даних для такого віку '''

txt_res = []
txt_res.append('''Низька. Терміново зверніться до лікаря!''')
txt_res.append('''Задовільна. Зверніться до лікаря!''')
txt_res.append('''Середня. Можливо, варто додатково обстежитись у лікаря.''')
txt_res.append('''Вище середнього''')
txt_res.append('''Висока''')

def index(P1,P2,P3):
    return (4 * (P1 + P2 + P3) - 200) / 10

def level(age):
    norm_age = (min(age, 15) - 7) // 2
    result = 21 - norm_age * 1.5
    return result

def rufier_result(index, level):
    if index >= level:
        return 0

    level = level - 4
    if index >= level:
        return 1

    level = level - 5
    if index >= level:
        return 2

    level = level - 5,5
    if index >= level:
        return 3
    return 4

def test(P1, P2, P3, age):
    if age < 7:
        return txt_index + "0" + txt_nodata
    else:
        ruff_index = index(P1,P2,P3)
        result = txt_res[rufier_result(ruff_index, level(age))]
        res = txt_index + str(ruff_index) + '\n' + txt_workheart + result
        return res