from collections import defaultdict

input = list(map(lambda x: x.split("\n"), open("input.txt").read().split("\n\n")))
monkeys = []

for i in input:
    items = list(map(lambda x: int(x), i[1].split(": ")[1].split(", ")))
    operator = i[2].split(": ")[1].split(" ")[3]
    operand = (
        int(i[2].split(": ")[1].split(" ")[4])
        if not i[2].split(": ")[1].split(" ")[4].isalpha()
        else i[2].split(": ")[1].split(" ")[4]
    )
    test_operand = int(i[3].split(": ")[1].split(" ")[2])
    result_operations = defaultdict()
    result_operations["true"] = int(i[4].split(": ")[1].split(" ")[3])
    result_operations["false"] = int(i[5].split(": ")[1].split(" ")[3])
    monkeys.append(
        {
            "items": items,
            "operator": operator,
            "operand": operand,
            "test_operand": test_operand,
            "result_operations": result_operations,
            "inspections": 0,
        }
    )

for _ in range(20):
    for i in range(0, len(monkeys)):
        for item in monkeys[i]["items"]:
            monkeys[i]["inspections"] += 1

            worry_level = (
                eval(
                    f"{item} {monkeys[i]['operator']} {monkeys[i]['operand'] if type(monkeys[i]['operand']) == int else item}"
                )
                // 3
            )

            if worry_level % monkeys[i]["test_operand"] == 0:
                monkeys[monkeys[i]["result_operations"]["true"]]["items"].append(
                    worry_level
                )
            else:
                monkeys[monkeys[i]["result_operations"]["false"]]["items"].append(
                    worry_level
                )

        monkeys[i]["items"] = []

top_two_inspections = sorted(
    list(map(lambda x: x["inspections"], monkeys)), reverse=True
)[:2]

print(top_two_inspections[0] * top_two_inspections[1])
