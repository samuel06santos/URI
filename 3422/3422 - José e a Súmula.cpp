#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        int t;
        string p;
        cin >> t >> p;
      
        if (p == "1T") {
            if (t <= 45) {
                cout << t << endl;
            } else {
                cout << "45+" << (t - 45) << endl;
            }
        } else {
            if (t <= 45) {
                cout << (45 + t) << endl;
            } else {
                cout << "90+" << (t - 45) << endl;
            }
        }
    }
    return 0;
}
