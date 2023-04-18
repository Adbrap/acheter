from ib_insync import *

ib = IB()
ib.connect('192.168.10.220', 7497, clientId=2)               # 7496 pour Live et 7497 pour Paper #

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
contract = Stock(f'GOOG', "SMART", "USD")

# Créer un ordre d'achat avec quantité d'action                                            # SCRIPT POUR ACHETER #

order = MarketOrder("BUY", 1)

# Placer l'ordre pour le compte spécifique
trade = ib.placeOrder(contract, order)
ib.sleep(1)
tradeAccount = trade.order.account
tradeAccount.updatePortfolio()
print(tradeAccount.portfolio)

# Se déconnecter de TWS
ib.disconnect()

#