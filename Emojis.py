# Defining a function for the conversion of emojis
def emoji_converter(message):
    words = message.split(" ")
    # Dictionary that contains the Emojis
    emojis = {
        ":)": "😀",
        ":(": "😥",
        ";)": "😉",
        ";/": "🤔",
        ":/": "😐",
        ":||": "😑",
        ":o": "😮",
        ":D": "😁"
    }
    # Leaving a blank space
    output = ""
    # The process of calling the function and returning a value
    for word in words:
        output += emojis.get(word, word) + " "
    return output

# Prompting the user to enter a text
message = input(">")

#Priniting the result
print(emoji_converter(message))
