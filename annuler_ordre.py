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

# Obtenir les ordres en cours pour le compte spécifique
orders = ib.openOrders()

# Annuler tous les ordres en cours
for order in orders:
    ib.cancelOrder(order)

# Se déconnecter de TWS
ib.disconnect()
