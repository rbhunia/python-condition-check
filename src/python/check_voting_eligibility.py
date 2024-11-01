def check_voting_eligibility(age):
    VOTING_AGE_THRESHOLD = 18

    def is_eligible(age):
        return age >= VOTING_AGE_THRESHOLD

    if is_eligible(age):
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")

try:
    input_age = int(input("Please enter your age: "))
    if input_age <= 0:
        raise ValueError("Invalid age")
    check_voting_eligibility(input_age)
except ValueError as e:
    print(e)