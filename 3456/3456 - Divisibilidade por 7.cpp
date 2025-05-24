#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(0);

    ll x;
    cin >> x;
    cout << x << endl;

    while (x >= 10) {
        ll last_d = x % 10;
        ll firsts_d = x / 10;
        x = 3 * firsts_d + last_d;
        cout << x << endl;
    }

    return 0;
}
