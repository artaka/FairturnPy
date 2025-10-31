import csv
import random

class Human:
    def __init__(self, name, prevLabs, submittingLabs, attended, current):
        try:
            self.name = name.capitalize().split(maxsplit=1)[0]
            self.prevLabs = prevLabs
            self.submittingLabs = int(submittingLabs)
            self.attended = 0
            if(attended.lower() == "да"):
                self.attended = 10
            self.current = current
            self.total = None
        except Exception as ex:
            raise Exception("\033[31mError in Human.__init__(). Invalid data in table!\033[0m")

    def getScore(self):
        if(self.total != None):
            raise Exception("\033[31mError in Human.getScore(). Total score is not empty!\033[0m")
        try:
            self.total = int(self.prevLabs) + int(self.submittingLabs) + self.attended
        except Exception as ex:
            raise Exception("\033[31mError in Human.getScore(). Error while getting total score: " + str(ex) + "\033[0m")

        if(self.submittingLabs == self.current):
            self.total -= 11

        if(self.name == "Мышковец" or self.name == "Макаревич"):
            self.total -= 2

        return self.total

    def getHumanCSVRow(self):
        if(self.total == None):
            raise Exception("\033[31mError in Human.getHumanCSVRow(). Total score is empty!\033[0m")
        return [
            self.name,
            self.prevLabs,
            self.submittingLabs,
            "Да" if self.attended == 10 else "Нет",
            self.current,
            self.total
        ]


def processCsv(currentLab):
    try:
        with open("pathfile.csv", 'r', newline='', encoding='cp1251') as csvfile:
            csv_file_path = csvfile.read().strip()
        if csv_file_path.lower() == 'd' or not csv_file_path:
            csv_file_path = 'output.csv'

        with open(csv_file_path, 'r', encoding='cp1251') as inputFile:
            reader = csv.reader(inputFile)
            rows = list(reader)

        processedHumans = []
        for row in rows:
            processedHumans.append(Human(row[0], row[1], row[2], row[3], currentLab))

        for human in processedHumans:
            human._sort_rand = random.random() ## Pseudorandom number in range(0.0, 1.0) for random sort humans with equals total score
            human.getScore()

        processedHumans.sort(key=lambda human: (human.total, human._sort_rand))

        for human in processedHumans: ## Deleting pseudorandom number
            del human._sort_rand

        with open(csv_file_path, 'w', newline='', encoding='cp1251') as outputFile:
            csvFileWriter = csv.writer(outputFile)
            csvFileWriter.writerow(["Surname", "Prev", "Submitting", "Attended", "Current", "Score"])
            for human in processedHumans:
                csvFileWriter.writerow(human.getHumanCSVRow())



    except Exception as ex:
        raise Exception(f"\033[31mError: {ex}\033[0m")

if __name__ == "__main__":
    processCsv(1)