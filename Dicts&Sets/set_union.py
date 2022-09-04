from prescription_data import adverse_interactions
# farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
# wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
#
# all_animals = farm_animals | wild_animals
# print(all_animals)

meds_to_watch = set()

for interaction in adverse_interactions:
    # meds_to_watch = meds_to_watch.union(interaction)
    # meds_to_watch = meds_to_watch | interaction
    # meds_to_watch.update(interaction)
    meds_to_watch |= interaction
print(sorted(meds_to_watch))


cool_colors = {"green", "blue", "purple", "violet"}
warm_colors = {"yellow", "orange", "red", "pink"}

# colors = cool_colors | warm_colors
#
# colors_2 = warm_colors.union(colors)
#
# print(colors)
# print(colors_2)

cool_colors.update()
print(cool_colors)
print(warm_colors)
