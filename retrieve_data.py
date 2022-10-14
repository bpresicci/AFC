import yahooquery as yf

def yahoo_finance(dictionary):
    """
    :param dictionary: dictionary with code of the desired company eg PRDSY
    :return: updated dictionary
    """
    company = yf.Ticker(dictionary["ticker"])
    dictionary["company"] = company
    return dictionary

def income_statement(dictionary):
    """
    :param dictionary: dictionary with the company extracted from yahoo_finance, its code and the path
    :return: income statement of the company and income statement until 2018
    """
    IS = yf.Ticker(dictionary["ticker"]).income_statement(frequency='a')
    IS = IS[:-1] # TOGLIE L'ULTIMA RIGA CHE è 2022
    IS.to_csv(path_or_buf=dictionary["path_is"], na_rep="-", mode="w")
    return IS

def balance_sheet(dictionary):
    """
    :param dictionary: dictionary with the company extracted from yahoo_finance, its code and the path
    :return: the balance sheet (and it saved a csv file of it)
    """
    BS = dictionary["company"].balance_sheet(frequency = 'a')
    BS.to_csv(path_or_buf=dictionary["path_bs"], na_rep="-",mode="w")
    return BS

def cash_flow(dictionary):
    """
    :param dictionary: dictionary with the company extracted from yahoo_finance, its code and the path
    :return: the cash_flow (and it saved a csv file of it)
    """
    CF = dictionary["company"].cash_flow(frequency='a')
    CF = CF[:-1]  # TOGLIE L'ULTIMA RIGA CHE è 2022
    CF.to_csv(path_or_buf=dictionary["path_cf"], na_rep="-",mode="w")
    return CF

