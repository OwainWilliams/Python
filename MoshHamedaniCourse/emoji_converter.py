
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
    ":)": "😊",
    ":(": "😢",
    ";)": "😉",
    ":D": "😁",
    ":x": "😘"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")

emoji_converter(message)
print(emoji_converter(message))