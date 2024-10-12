friendships = {
    "user1": {"user2", "user3", "user4"},
    "user2": {"user1", "user3"},
    "user3": {"user1", "user2", "user4"},
    "user4": {"user1", "user3"}
}
person_1, person_2 = input("Друг А: "), input("Друг Б: ")
if (person_1 and person_2 in friendships):
    print (f"спільні друзі: {friendships[person_1]&friendships[person_2]}")
else:
    print("Таких у базі немає... ")