def simpledeep(d: dict) -> dict:
    """
    return a non- recursive copy of a dictionary
    :param d: dictionary to copy
    :return: copy of dictionary
    """

    new_dict = {}
    for key, value in d.items():
        new_dict[key] = value
    return new_dict


rugrats = {"Tommy": "Leader",
           "Chucky": "Good Friend",
           "Phil": ["gross", "boy twin"],
           "Lill": ["also gross", "girl twin"],
           }

rugrats_copy = simpledeep(rugrats)
rugrats_copy["Angelica"] = "loveable jerk"
rugrats_copy["Dill"] = "baby brother"
rugrats_copy["Phil"] = "possibly into Suzie?"

print(id(rugrats_copy["Phil"]), rugrats_copy["Phil"])
print(id(rugrats["Phil"]), rugrats["Phil"])
print()
