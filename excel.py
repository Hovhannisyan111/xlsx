import xlsxwriter

def get_content(fname):
    with open(fname) as f:
        return f.read()

def chars_dict(cnt):
    letters = {}
    numbers = {}
    symbols = {}
    for i in cnt:
        if i.isalpha():
            letters[i] = letters.get(i, 0) + 1
        elif i.isdigit():
            numbers[i] = numbers.get(i, 0) + 1
        else:
            symbols[i] = symbols.get(i, 0) + 1
    return letters, numbers, symbols

def create_workbook(output):
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    return workbook, worksheet

def excel(workbook, worksheet, letters, numbers, symbols):
    worksheet.write(0, 0, "Letters")
    worksheet.write(0, 1, "Numbers")
    worksheet.write(0, 2, "Symbols")

    row = 1
    for l, count in sorted(letters.items(), key=lambda x: x[1], reverse=True):
        worksheet.write(row, 0, l + ":" + str(count))
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
    letters, numbers, symbols = chars_dict(cnt)
    workbook, worksheet = create_workbook('ex.xlsx')
    excel(workbook, worksheet, letters, numbers, symbols)
    workbook.close()

if __name__ == "__main__":
    main()
