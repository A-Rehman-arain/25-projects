
def mad_lib():
    # Ask user for the missing words

    noun = input("Enter a noun: ")
    adjective = input("Enter and ajective: ")
    verb = input ("Enter a verb: ")

    # Display the story
    madlib = f"I visited {noun} yesterday. It was a very {adjective} experience to {verb} there."
    print('\n',madlib)

# Call the function
mad_lib()  