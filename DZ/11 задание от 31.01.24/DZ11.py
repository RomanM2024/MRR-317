
olympiad_match = {"Матвей", "Евгения", "Михаил", "Максим", "Наталья"}
olympiad_phys = {"Максим", "Матвей", "Александр"}
winners_all = olympiad_match | olympiad_phys
print(winners_all)
two_winners = olympiad_match & olympiad_phys
print(two_winners)
new_olympiad_phys = olympiad_match & olympiad_phys
print(new_olympiad_phys)
del olympiad_phys


