#CS175L-01
#Taye Kennedy
#Stocks

#Inputs
COMMISSION_RATE = float(input("What is the commission rate?: "))
NUM_SHARES = int(input("What is the number of shares?: "))
PURCHASE_PRICE = float(input("what is the perchase price?: "))
SELLING_PRICE = float(input("what is the selling price?: "))
#Calculations
amountPaidForStock = NUM_SHARES * PURCHASE_PRICE
purchaseCommission = COMMISSION_RATE * amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = NUM_SHARES * SELLING_PRICE
sellingCommission = COMMISSION_RATE * stockSoldFor
totalCommission = purchaseCommission + sellingCommission
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid
#Outputs
print("Amount paid for stock: $", amountPaidForStock)
print("Commission paid on perchase: $", perchaseCommission)
print("Amount the stock sold for: $", stockSoldFor)
print("Commission paid on sale: $", sellingCommission)
print("Total commission paid: $", totalCommission)
print("profit: $", profitOrLoss)
