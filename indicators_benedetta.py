def fun_ebit_margin(IS):
    """
    :param IS: income statement of the company
    :return: ebit margin %
    """
    return IS.loc[:,"EBIT"]/IS.loc[:,"TotalRevenue"]*100




# DA QUI IN POI GLI INDICATORI DI BENEDETTA

def fun_quality_of_operating_earning(IS, CF):
    """
    :param CF: cash flow of company
    :param IS: income statement of the company
    :return: quality of operating earning %
    """
    return CF.loc[:,"OperatingCashFlow"]/IS.loc[:,"EBIT"]*100

def fun_asset_turnover_ratio(IS, BS):
    """
    :param IS: income statement of the company
    :param BS: balance sheet of the company
    :return: asset turnover ratio %
    """
    return IS.loc[:,"TotalRevenue"]/BS.loc[:,"TotalAssets"]*100

def fun_debt_to_equity_ratio(BS):
    """
    :param method: boolean choice of how to compute it:
                                                        True -> total liabilities (current + non current)
                                                        False -> NFP (from reclassification of BS) debts with an explicit interest rate - cash and cash equivalents
    :param BS: balance sheet of the company
    :return: debt to equity ratio according to the chosen method
    """
    debt = BS.loc[:,"TotalLiabilitiesNetMinorityInterest"] # DA CONTINUARE CON NFP (METODO FALSE)
    return debt/BS.loc[:,"StockholderEquity"]

def fun_interest_coverage_ratio(IS):
    """
    :param IS: income statement of the company
    :return: interest coverage ratio %
    """
    return IS.loc[:,"EBIT"]/IS.loc[:,"InterestExpenses"]*100

def fun_cost_of_debt(IS, BS):
    """
    :param IS: income statement of the company
    :param BS: balance sheet of the company
    :return:  cost of debt %
    """
    return IS.loc[:,"InterestExpenses"]/BS.loc[:,"TotalAssets"]*100 # NE HO MESSO UNO A CASO PERCHè MANCA IL TERMINE GIUSTO

def fun_effective_tax_rate(IS):
    """
    :param IS: income statement of the company
    :return: effective tax rate %
    """
    Taxation = IS.loc[IS.loc[:,"PretaxIncome"]]-IS.loc[:,"NetIncomeContinuousOperations"] #compute taxation
    return Taxation/IS.loc[:,"PretaxIncome"]*100

def fun_current_ratio(BS):
    """
    :param BS: balance sheet of the company
    :return: current ratio
    """
    return BS.loc[:,"CurrentAssets"]/BS.loc[:,"CurrentLiabilities"]

def fun_quick_ratio(BS):
    """
    :param BS: balance sheet of the company
    :return: quick ratio
    """
    return (BS.loc[:,"CashCashEquivalentsAndShortTermInvestments"]+BS.loc[:,"AccountReceivables"])/BS.loc[:,"CurrentLiabilities"]

def fun_inventory_turnover_ratio(IS, BS):
    """
    :param IS: income statement of the company
    :param BS: balance sheet of the company
    :return: inventory turnover ratio
    """
    return IS.loc[:,"TotalRevenue"]/BS[:,"Inventory"]

def fun_days_sales_outstanding(IS, BS):
    """
    :param IS: income statement of the company
    :param BS: balance sheet of the company
    :return: days sales outstanding
    """
    return BS.loc[:,"AccountReceivables"]/IS.loc[:,"TotalRevenue"]*365

def fun_days_payables_outstanding(IS, BS):
    """
    :param IS: income statement of the company
    :param BS: balance sheet of the company
    :return: days payables outstanding
    """
    return BS.loc[:,"Payables"]/IS.loc[:,"CostOfRevenue"]*365

def fun_residual_income(IS, BS, dictionary):
    """
    :param IS: income statement of the company
    :param BS: balance sheet of the company
    :param dictionary: dictionary of the company
    :return: residual income
    """
    Investments = BS.loc[:,"CashEquivalentsAndShortTermInvestments"] - BS.loc[:,"CashEquivalents"] + BS.loc[:,"LongTermEquityInvestment"]
    return IS.loc[:,"EBIT"] - dictionary["k"]*Investments

