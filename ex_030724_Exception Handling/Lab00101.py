#how to write to the file
with open('TestData.txt', 'a') as file:
    file.write("\n hello how are you")

    with open("TestData.txt", "r") as file:
        lines = file.readlines()

    # print all lines
    for line in lines:
        print(line, end=" ")

        import csv

        with open('TD.csv') as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                print(row[0], row[1])

                import csv

                with open('TD.csv') as csvfile:
                    reader = csv.reader(csvfile)
                    for col in reader:
                        print(col[0], col[1], sep=" | ")



