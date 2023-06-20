# pick 20% of the top solutions
def selection(lis):
    percentage_of_best_solutions = 0.2
    sorted_list = sorted(lis, key=lambda x: x[1], reverse=True)

    return sorted_list[:round(len(sorted_list) * percentage_of_best_solutions)], sorted_list[round(len(sorted_list) * percentage_of_best_solutions):]
