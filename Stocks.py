commission_rateStockPurchase = float(input('Enter commission rate percentage (ex 0.03) on stock purchase: '))
commission_rateStockSale = float(input('Enter commission rate percentage (ex 0.03) on stock sale: '))
sharesPurchased = float(input('Enter number of shares purchased: '))
sharesSold = int(input('Enter number of shares sold: '))
sharePurchasePrice = float(input('Enter purchase price per share: '))
shareSellPrice = float(input('Enter sell price per share: '))
amountPaidForStock = sharesPurchased * sharePurchasePrice
print('Amount paid for the stock:',f'${amountPaidForStock:,.2f}')
commissionPaid = commission_rateStockPurchase * amountPaidForStock
print('Commission paid on the purchase:',f'${commissionPaid:,.2f}')
stockSoldFor = sharesSold * shareSellPrice
print('Amount the stock sold for:',f'${stockSoldFor:,.2f}')
sellingCommission = commission_rateStockSale * stockSoldFor
print('Commission paid on the sale:',f'${sellingCommission:,.2f}')
totalReceived = stockSoldFor - sellingCommission
totalPaid = amountPaidForStock + commissionPaid
profitOrLoss = totalReceived - totalPaid
print('Profit (or loss if negative):',f'${profitOrLoss:,.2f}')






