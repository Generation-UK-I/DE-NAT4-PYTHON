# Example 1.1 - spaced out properly
2 * 4 + 7.0 / 4.0

# Example 1.2 - with brackets to help us see
(2 * 4) + (7.0 / 4.0)

# Example 1.3 - also with a variable
result = (2 * 4) + (7.0 / 4.0)

# Example 2 - laid out clearly (pretend the 'create_person' function and the other variables exist)
person = create_person(
    firstname,
    surname,
    age,
    city,
    nationality,
    gender,
    height
)

# Example 3 - laid out clearly. Each conditional ('and') is at the start of a new line
def get_length_condition(data):
    is_valid = data is not None \
        and data != "" \
        and len(data) > 3 \
        and len(data) < 20
    return is_valid

# Example 3.2 - What does the function do? What is the argument for?
def password_is_valid(candidate_text):
    is_valid = candidate_text is not None \
        and candidate_text != "" \
        and len(candidate_text) > 3 \
        and len(candidate_text) < 20
    return is_valid
