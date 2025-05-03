#include <iostream>
#include <vector>

using namespace std;

int main(){
    
    vector<int> vetor;
    vector<int> par;
    vector<int> impar;
    int countPar = 0;
    int countImpar = 0;

    for (int i=0; i < 6; i++){
        int valor;
        cout << "Insira um valor: " << endl;
        cin >> valor;
        vetor.push_back(valor);
    }

    for (int i=0; i < vetor.size(); i++){
        if (vetor[i] % 2 == 0){
            countPar ++;
            par.push_back(vetor[i]);
        } else {
            countImpar ++;
            impar.push_back(vetor[i]);
        }
    }

    cout << "Quantidade de numeros pares: " << countPar << endl;
    for (int i = 0; i < par.size(); i++){
        cout << "Numeros pares: " << par[i] << endl;
    }
    cout << "Quantidade de numeros impares: " << countImpar << endl;
    for (int i = 0; i < impar.size(); i++){
        cout << "Numeros impares: " << impar[i] << endl;
    }

    return 0;
}