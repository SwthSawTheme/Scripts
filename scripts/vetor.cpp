#include <iostream>
#include <vector>

using namespace std;

int main(){
    
    vector<int> vetor;
    int countPar = 0;
    int countImpar = 0;

    for (int i=0; i < 6;i++){
        int valor;
        cout << "Insira um valor: " << endl;
        cin >> valor;
        vetor.push_back(valor);
    }

    for (int i=0; i < vetor.size(); i++){
        if (vetor[i] % 2 == 0){
            countPar ++;
        } else {
            countImpar ++;
        }
    }

    cout << "Quantidade de numeros pares: " << countPar << endl;
    cout << "Quantidade de numeros impares: " << countImpar << endl;

    return 0;
}