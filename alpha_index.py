def alphabet_position(text):
    return " ".join([str(ord(i.lower()) - 96) for i in text if i.isalpha()])


# return " ".join([string.ascii_lowercase.index(i)+1 for i in text if i.isalpha()])


if __name__ == '__main__':
    print(alphabet_position("Ten one o' clock"))
