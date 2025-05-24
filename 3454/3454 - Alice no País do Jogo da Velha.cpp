#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(nullptr);

    string s;
    cin >> s;

    int countX = 0;
    int countO = 0;

    for (char c : s) {
        if (c == 'X') {
            countX++;
        } else if (c == 'O') {
            countO++;
        }
    }

    if (countX == 2 && countO == 1) {
        bool alice_wins = false;
        if ((s[0] == 'X' && s[1] == 'X') || (s[1] == 'X' && s[2] == 'X')) {
            alice_wins = true;
        }

        if (alice_wins) {
            cout << "Alice" << endl;
        } else {
            cout << "*" << endl;
        }
    } else {
        cout << "?" << endl;
    }

    return 0;
}
