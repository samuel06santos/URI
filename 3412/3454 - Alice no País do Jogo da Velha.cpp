#include <bits/stdc++.h>
using namespace std;

double calcNota(vector<double>& notas) {
    int len = notas.size();
    if (len == 1) return notas[0] / 2.0;

    double soma = 0.0;
    double valor_minimo = notas[0];
    int indx_min = 0;

    for (int i = 0; i < len; i++) {
        soma += notas[i];
        if (notas[i] < valor_minimo) {
            valor_minimo = notas[i];
            indx_min = i;
        }
    }

    if (len <= 3) {
        return soma / len;
    } else {
        if (notas[3] >= valor_minimo) {
            notas[indx_min] = notas[3];
            notas.pop_back();
        }
        return (notas[0] + notas[1] + notas[2]) / 3.0;
    }
}

int main() {
    int c;
    cin >> c;
    cin.ignore();

    ostringstream output;

    for (int i = 0; i < c; i++) {
        string nome;
        getline(cin, nome);

        vector<double> notas;
        string linha;
        getline(cin, linha);
        istringstream iss(linha);
        double nota;
        while (iss >> nota) {
            notas.push_back(nota);
        }

        double resultado = calcNota(notas);
        output << fixed << setprecision(1);
        output << nome << ": " << resultado << '\n';
    }

    string final_output = output.str();
    if (!final_output.empty() && final_output.back() == '\n') {
        final_output.pop_back();
    }

    cout << final_output << endl;
    return 0;
}
