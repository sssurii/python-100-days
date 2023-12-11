questions = [
    [
        "What is the pH value of the human body?",
        ["9.2 to 9.8", "7.0 to 7.8", "6.1 to 6.3", "5.4 to 5.6"],
        ["7.0 to 7.8"],
    ],
    [
        'Which of the following are called "Key Industrial animals"?',
        ["Producers", "Tertiary consumers", "Primary consumers", "None of these"],
        ["Primary consumers"],
    ],
    [
        "Elections to panchayats in state are regulated by",
        [
            "Gram panchayat",
            "Nagar Nigam",
            "Election Commission of India",
            "State Election Commission",
        ],
        ["State Election Commission"],
    ],
    [
        'Which of the following Himalayan regions is called "Shivalik\'s"?',
        ["Upper Himalayas", "Lower Himalayas", "Outer Himalayas", "Inner Himalayas"],
        ["Outer Himalayas"],
    ],
    [
        "Forming of Association in India is",
        ["Legal Right", "Illegal Right", "Natural Right", "Fundamental Right"],
        ["Fundamental Right"],
    ],
    [
        "The Samkhya School of Philosophy was founded by",
        ["Gautam Buddha", "Mahipala", "Gopala", "Kapila"],
        ["Kapila"],
    ],
    [
        "Pustaz grasslands are situated at?",
        ["South Africa", "China", "Hungary", "USA"],
        ["Hungary"],
    ],
    [
        "Right to emergency medical aid is a",
        ["Legal Right", "Illegal Right", "Constitutional Right", "Fundamental Right"],
        ["Fundamental Right"],
    ],
    [
        "Chelaiya Samiti is related to which of the following?",
        ["Banking sector", "Insurance sector", "Health Sector", "Tax reforms"],
        ["Tax reforms"],
    ],
    [
        "Which of the given devices is used for counting blood cells?",
        ["Hmelethometer", "Spyscometer", "Hemocytometer", "Hamosytometer"],
        ["Hemocytometer"],
    ],
    [
        "Which of the given compounds is used to make fireproof clothing?",
        [
            "Aluminum chloride",
            "Aluminum Sulphate",
            "Magnesium Chloride",
            "Magnesium Sulphate",
        ],
        ["Aluminum Sulphate"],
    ],
    [
        "Which of the given cities is located on the bank of river Ganga?",
        ["Patna", "Gwalior", "Bhopal", "Mathura"],
        ["Patna"],
    ],
    [
        "The driving force of an ecosystem is",
        ["Carbon Mono oxide", "Biogas", "Solar Energy", "Carbon dioxide"],
        ["Solar Energy"],
    ],
    [
        "Which of the given is a disease caused by protozoa?",
        ["Cancer", "Typhoid", "Kala-azar", "Chicken Pox"],
        ["Kala-azar"],
    ],
    [
        'The term "Samantas" is usually seen in the medieval history of India about',
        ["Artists", "Big Landlords", "Servants", "Queens"],
        ["Big Landlords"],
    ],
    [
        "Which of the given coins was known as 'Karshapana' in ancient literature?",
        ["Gold coins", "Bronze coins", "Punch marked coins", "Iron coins"],
        ["Punch marked coins"],
    ],
]

reward = 0

for i in range(15):
    print("Q.", questions[i][0], "\n")
    print("Amswers: ")
    for j in range(4):
        print((j + 1), ".", questions[i][1][j], "\n")

    ans = input("Select your anwser: ")
    ans = int(ans)
    if questions[i][1][ans - 1] == questions[i][2][0]:
        if i == 0:
            reward += 100

        reward = reward * 5
        print("Right Anwser!!", "\n")
        print("Your Score is", reward, "\n\n")
    else:
        print("Wrong Anwser!!", "\n\n")
        break

print("Your Total score is:", reward)
