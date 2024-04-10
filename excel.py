import xlsxwriter

def get_content(fname):
    with open(fname) as f:
        return f.read()

def chars_dict(cnt):
    numbers = {}
    symbols = {}
    vowels = {}
    consonants = {}
    for i in cnt:
        if i.isalpha():
            if i.lower() in "aeoui":
                vowels[i]  = vowels.get(i, 0) + 1
            else:
                consonants[i] = consonants.get(i, 0) + 1
        elif i.isdigit():
            numbers[i] = numbers.get(i, 0) + 1
        else:
            symbols[i] = symbols.get(i, 0) + 1
    return numbers, symbols, vowels, consonants

def create_workbook(output):
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    return workbook, worksheet

def excel(workbook, worksheet, numbers, symbols, vowels, consonants):
    worksheet.write(0, 0, "Letters")
    worksheet.write(1, 0, "Vowels")
    worksheet.write(0, 1, "Numbers")
    worksheet.write(0, 2, "Symbols")

    row = 2
    for v, count in sorted(vowels.items(), key=lambda x: x[1], reverse=True):
        worksheet.write(row, 0, v + ":" + str(count))
        row += 1
        
    worksheet.write(row, 0, "Consonants")
    row += 1
    for c, count in sorted(consonants.items(), key=lambda x: x[1], reverse=True):
        worksheet.write(row, 0, c +":" + str(count))
        row += 1  
    row = 1
    for n, count in sorted(numbers.items(), key=lambda x: x[1], reverse=True):
        worksheet.write(row, 1, n + ":" + str(count))
        row += 1
    row = 1
    for s, count in sorted(symbols.items(), key=lambda x: x[1], reverse=True):
        worksheet.write(row, 2, s + ":" + str(count))
        row += 1

def main():
    cnt = get_content("db.txt")
    numbers, symbols, vowels, consonants = chars_dict(cnt)
    workbook, worksheet = create_workbook('ex.xlsx')
    excel(workbook, worksheet, numbers, symbols, vowels, consonants)
    workbook.close()

if __name__ == "__main__":
    main()

