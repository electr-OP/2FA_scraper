import pygsheets
gc = pygsheets.authorize(service_file='google_sheets_key.json')


def update_rowss(gsheet, values):
    sh = gc.open(gsheet)
    wks = sh[0]
    cells = wks.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')
    last_row = len(cells)
    wks.insert_rows(last_row, number=len(values), values=values, inherit=False)

def get_sheetcol_values(gsheet, col):
    #open the google spreadsheet
    sh = gc.open(gsheet)
    wks = sh[0]
    k = wks.get_col(col, returnas='matrix', include_tailing_empty=False)
    return k