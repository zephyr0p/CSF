import re

emails = open("input.txt", "r")  # opens the file to analyze
results = open("op.txt", "w")  # creates new file for search results

resultsList = []

for line in emails:
    if (
        "From - " in line
    ):  # recgonizes the beginning of a email message and adds a linebreak
        newMessage = re.findall(r"\w\w\w\s\w\w\w.*", line)
        if newMessage:
            resultsList.append("\n\t*** EMAIL HEADER DETAILS ***\n")

    if "From: " in line:
        address = re.findall(r"[\w.-]+@[\w.-]+", line)
        if address:
            resultsList.append("\n\nFrom : ")
            resultsList.append(address)
            resultsList.append(";")

    if "To: " in line:
        if "Delivered-To:" not in line:  # avoids confusion with 'Delivered-To:' tag
            address = re.findall(r"[\w.-]+@[\w.-]+", line)
            if address:
                resultsList.append("\n\nTo : ")

                for person in address:
                    resultsList.append(person)
                    resultsList.append("; ")

    if "Bcc: " in line:
        address = re.findall(r"[\w.-]+@[\w.-]+", line)
        if address:
            resultsList.append("\n\nBcc : ")
            resultsList.append(address)
            resultsList.append(";")

    if "Date: " in line:
        address = re.findall(r"\w\w\w\,.*", line)
        if address:
            resultsList.append("\n\nDate : ")
            resultsList.append(address)
            resultsList.append(";")

    if "Subject: " in line:
        address = re.findall(r"[\w\s.-]+[\w.-]+", line)
        if address:
            resultsList.append("\n\nSub : ")
            resultsList.append(address)

for result in resultsList:
    results.writelines(result)


emails.close()
results.close()
