def sorting_cheeses(**cheeses_dict):
    cheeses_dict = sorted(cheeses_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for cheese, quantity in cheeses_dict:
        result.append(cheese)
        quantity_list = sorted(quantity, reverse=True)
        result += quantity_list

    return "\n".join([str(x) for x in result])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
