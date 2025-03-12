
// Faça uma função que receba um range de números
// E retorne uma lista com apenas numeros pares

#include <iostream>
#include <vector>
using namespace std;

vector<int> isPair(vector<int> num){
    vector<int> pair;

    for (int i=0; i < num.size(); i++){
        if ( num[i] % 2 == 0){
            pair.push_back(num[i]);
        }
    } return pair;
}

int main(){
    vector<int> rangeNumerico;

    for (int i=0; i < 100; i++){
        rangeNumerico.push_back(i);
    }

    vector<int> numerosPair = isPair(rangeNumerico);

    for (int i=0; i < numerosPair.size(); i++){
        cout << "Elemento Par: " << numerosPair[i] << endl;
    }
    return 0;
}