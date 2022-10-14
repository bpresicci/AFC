from retrieve_data import yahoo_finance, income_statement, balance_sheet, cash_flow
from indicators_benedetta import fun_ebit_margin
prada = {
    "k" : 0.833,
    "ticker": "PRDSY",
    "path_is": r"C:\Users\bened\PycharmProjects\pythonProject1\income_statement.csv",
    "path_bs": r"C:\Users\bened\PycharmProjects\pythonProject1\balance_sheet.csv",
    "path_cf": r"C:\Users\bened\PycharmProjects\pythonProject1\cash_flow.csv"
}

prada = yahoo_finance(prada)
BS = balance_sheet(prada)
IS = income_statement(prada)
CF = cash_flow(prada)
# EVENTUALMENTE AGGIUNGI CORREZIONI QUI
IS['EBIT'] = [323846000,306779000,20061000,489484000]
ebit_margin = fun_ebit_margin(IS)
