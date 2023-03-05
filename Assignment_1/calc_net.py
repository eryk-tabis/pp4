def calculate_net_value(gross_price, tax):
    if tax >= 0:
        return round(gross_price/(1+tax/100), 2)
    else:
        raise Exception("Tax value should be equal or higher than 0")
