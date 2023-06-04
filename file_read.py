def main():
    with open('referat.txt', "r", encoding='utf-8') as t:
            text = t.read()
            print(len(text))

            cont_l = (text.split())
            print(len(cont_l))

            no_bots = text.replace(".", "!")

            with open("referat2.txt", "w", encoding='utf-8') as tn:
                tn.write(no_bots)

if __name__ == "__main__":
     main()