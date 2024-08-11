def main():
    user_input = input("Write something! ")
    convert_text = convert(user_input)
    print(convert_text)


def convert (text):
    #print("Before conversion:", text)
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    #print("After conversion:", text)
    return text

main()