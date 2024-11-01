def check_pass_fail(score1: float, score2: float, score3: float) -> str:
    """
    Checks if the average score of three subjects is a pass or fail.

    :param score1: Score of the first subject
    :param score2: Score of the second subject
    :param score3: Score of the third subject
    :return: "Pass" if the average score is 50 or above, "Fail" otherwise
    """
    average_score = (score1 + score2 + score3) / 3
    return "Pass" if average_score >= 50 else "Fail"


# Example usage:
try:
    score1 = float(input("Enter the score for the first subject: "))
    score2 = float(input("Enter the score for the second subject: "))
    score3 = float(input("Enter the score for the third subject: "))

    result = check_pass_fail(score1, score2, score3)
    print(f"The result is: {result}")
except ValueError:
    print("Please enter valid numerical values for the scores.")
