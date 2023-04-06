def reverse_words(string):
    slist = string.split()
    new_string = " ".join(slist[::-1])
    print("input is\n\n" + string + "\n\nand the reverse is\n\n" + new_string + "\n")

def main():
    input1 = """Two roads diverged in a yellow wood, And sorry I could not travel both And
be one traveler, long I stood And looked down one as far as I could To where
it bent in the undergrowth;"""
    
    input2 = """Then took the other, as just as fair, And having perhaps the better claim,
Because it was grassy and wanted wear; Though as  for that the passing there
Had worn them really about the same,"""

    reverse_words(input1)
    reverse_words(input2)

if __name__ == "__main__":
    main()
