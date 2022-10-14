from retrieve_data import yahoo_finance, income_statement, balance_sheet, cash_flow
from indicators import fun_ebit_margin

prada = {
    "code": "PRDSY",
    "path_is": r"C:\Users\bened\PycharmProjects\pythonProject1\income_statement.csv",
    "path_bs": r"C:\Users\bened\PycharmProjects\pythonProject1\balance_sheet.csv",
    "path_cf": r"C:\Users\bened\PycharmProjects\pythonProject1\cash_flow.csv"
}

prada = yahoo_finance(prada)
BS = balance_sheet(prada)
IS = income_statement(prada)
CF = cash_flow(prada)

# EVENTUALMENTE AGGIUNGI CORREZIONI QUI
IS.loc['Ebit'] = [489484000,20061000,306779000,323846000]

ebit_margin = fun_ebit_margin(IS)
