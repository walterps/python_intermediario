from classes_bank.conta_poupanca import ContaPoupanca
from classes_bank.conta_corrente import ContaCorrente

cp = ContaPoupanca(1, 1, 0)
cp.depositar(100)
cp.sacar(50)
cp.sacar(50)
cp.sacar(50)


print('#######################')
cc = ContaCorrente(1, 2, 0)
cc.depositar(100)
cc.sacar(50)
cc.sacar(50)
cc.sacar(50)


