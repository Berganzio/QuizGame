question_data = [
    {"category": "Entertainment: Japanese Anime & Manga",
     "type": "boolean",
     "difficulty": "easy",
     "question": "In the 1988 film 'Akira';, ""Tetsuo ends up destroying Tokyo.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
     "question": "A person can get sunburned on a cloudy day.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "The common software-programming acronym 'I18N'; "
                 "comes from the term 'Interlocalization';.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Mythology", "type": "boolean", "difficulty": "easy",
     "question": "In Norse mythology, Thor once dressed as a woman.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
     "question": "The Great Wall of China is visible from the moon.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Entertainment: Music", "type": "boolean", "difficulty": "medium",
     "question": "Soulja Boy's 'Crank That' won a Grammy for Best Rap Song in 2007.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "History", "type": "boolean", "difficulty": "medium",
     "question": "The two atomic bombs dropped on Japan by the United States "
                 "in August 1945 were named 'Little Man' and 'Fat Boy'.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Music", "type": "boolean", "difficulty": "medium",
     "question": "The cover of The Beatles album 'Abbey Road' featured a Volkswagen Beetle in the background.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "History", "type": "boolean", "difficulty": "medium",
     "question": "The first televised presidential debate was between Jimmy Carter and Gerald Ford.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
     "question": "Super Mario Bros. was released in 1990.", "correct_answer": "False",
     "incorrect_answers": ["True"]}, {"category": "Politics", "type": "boolean", "difficulty": "easy",
                                      "question": "The S in Harry S. Truman stands for &quot;Samuel&quot;.",
                                      "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "Israel is 7 hours ahead of New York.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
     "question": "The Ace Attorney trilogy was suppose to end with 'Phoenix Wright:"
                 " Ace Attorney Trials and Tribulations' as its final game.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "hard",
     "question": "'Number 16 Bus Shelter' was a child's"
                 " name that was approved by the New Zealand government.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
     "question": "Anatomy considers the forms of macroscopic structures such as organs and organ systems.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "medium",
     "question": "The Xenomorph from the science fiction film 'Alien' has acidic blood.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Politics", "type": "boolean", "difficulty": "easy",
     "question": "Despite being seperated into multiple countries,"
                 " The Scandinavian countries are unified by all having the same monarch.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Mythology", "type": "boolean", "difficulty": "medium",
     "question": "According to Norse mythology, Loki is a mother.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
     "question": "In 2010, Twitter and the United States Library of "
                 "Congress partnered together to archive every tweet by American citizens.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "History", "type": "boolean", "difficulty": "easy",
     "question": "Former United States Presidents John Adams and Thomas Jefferson died within hours of each other.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Politics", "type": "boolean", "difficulty": "easy",
     "question": "Russia passed a law in 2013 which outlaws telling children that homosexuals exist.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
     "question": "Sitting for more than three hours a day can cut two years off a person's life expectancy.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "'Mongolia' was a part of the now non-existent U.S.S.R.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "Toronto is the capital city of the North American country of Canada.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "The capital of the US State Ohio is the city of Chillicothe.", "correct_answer": "False",
     "incorrect_answers": ["True"]}, {"category": "Geography", "type": "boolean", "difficulty": "easy",
                                      "question": "St. Louis is the capital of the US State Missouri.",
                                      "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "You could walk from Norway to North Korea while only passing through Russia.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy",
     "question": "In Pokemon, Ash's Pikachu refuses to go into a pokeball.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Board Games", "type": "boolean", "difficulty": "easy",
     "question": "There is a Donald Trump Board Game, which was made in 1989.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
     "question": "In the original Star Wars trilogy, Alec Guinness provided the voice for Darth Vader.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy",
     "question": "The name of the attack 'Kamehameha' in "
                 "Dragon Ball Z was named after a famous king of Hawaii.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "hard",
     "question": "The names of Roxas's Keyblades in Kingdom"
                 " Hearts are 'Oathkeeper' and 'Oblivion'.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "In the game Dead by Daylight, the killer Michael Myers is refered to as 'The Shape'.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Music", "type": "boolean", "difficulty": "easy",
     "question": "A Saxophone is a brass instrument.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "medium",
     "question": "Joan Cusack starred in the 2009 disaster movie, '2012'.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Animals", "type": "boolean", "difficulty": "easy",
     "question": "Cats have whiskers under their legs.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Television", "type": "boolean", "difficulty": "medium",
     "question": "Bob Ross was a US Air Force pilot.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "medium",
     "question": "In 'JoJo's Bizarre Adventure',"
                 " Father Enrico Pucchi uses a total of 3 stands in Part 6: Stone Ocean.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science & Nature", "type": "boolean", "difficulty": "hard",
     "question": "The value of one Calorie is different than the value of one calorie.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Cartoon & Animations", "type": "boolean", "difficulty": "easy",
     "question": "Waylon Smithers from 'The Simpsons'"
                 " was originally black when he first appeared in the series.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "'Metal Gear Solid 3: Snake Eater' was released in 2004.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Music", "type": "boolean", "difficulty": "hard",
     "question": "Pete Townshend's solo album, 'White City:"
                 " A Novel', is set in the metropolitan area of Chicago.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
     "question": "Haggis is traditionally ate on Burns Night.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "Mythology", "type": "boolean", "difficulty": "hard",
                                       "question": "Janus was the Roman god of doorways and passageways.",
                                       "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "Rhode Island is actually located on the US mainland, despite its name.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Cartoon & Animations", "type": "boolean", "difficulty": "medium",
     "question": "Nutcracker Suite was one of the musical pieces featured in Disney's 1940's film Fantasia.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
     "question": "The British organisation CAMRA stands for The Campaign for Real Ale.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "hard",
     "question": "In 'Minecraft', gold tools are faster than diamond tools.",
     "correct_answer": "True", "incorrect_answers": ["False"]}
]
