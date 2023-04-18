from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=2)               # 7496 pour Live et 7497 pour Paper #

# Se connecter à votre compte IB
accountName = "abtrading3333"
accountPassword = "ZD68gm5h!"
managedAccounts = ib.managedAccounts()
if len(managedAccounts) == 0:
    print("Erreur: Pas de compte géré trouvé.")
    ib.disconnect()
    exit()
account = managedAccounts[0]

# Créer un contrat pour l'action Tesla
contract = Stock('AAPL', 'SMART', 'USD')

# Créer un ordre de limit avec le prix limit
#limitPrice = 150.0  # prix limit
#limitOrder = LimitOrder('BUY', 1, limitPrice)

# Placer l'ordre de limit pour le compte spécifique
#limitTrade = ib.placeOrder(contract, limitOrder)
#ib.sleep(1)
#limitAccount = limitTrade.order.account

# Créer un ordre de stop loss
stopPrice = 155.0  # prix du stop loss
stopLoss = StopOrder('SELL', 1, stopPrice)

# Placer l'ordre de stop loss pour le compte spécifique
stopTrade = ib.placeOrder(contract, stopLoss)
ib.sleep(1)
stopAccount = stopTrade.order.account

# Mettre à jour le portefeuille du compte
limitAccount.updatePortfolio()
print(limitAccount.portfolio)

# Se déconnecter de TWS
ib.disconnect()
