from count_distinct_characters import *
def count_distinct_characters(string):
    return len(set(string.lower())) # returns a set with all unique characters in lowercase, then return its length.