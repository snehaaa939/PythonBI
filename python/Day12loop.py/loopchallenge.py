# Write function to take string as input and provide output with below condition:
# First letter of word always have to be capital
# If preceding letter occurs earlier in dictionary then letter has to be capital
# If preceding letter occurs later in dictionary then letter has to be small
# If preceding letter is same as current letter then no change in case.

# Example: applE is fruit => APple IS FRUiT
# A => 1st Letter(upper), 1st P => Preceding(A) occur earlier (upper),
# 2nd P => Preceding(P) same(no_change), L => Preceding(P) occurs later (small),
# e => Preceding(L) occurs later(small), I => 1st letter(upper) and so on
