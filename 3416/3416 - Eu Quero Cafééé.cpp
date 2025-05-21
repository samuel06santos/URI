#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(nullptr);
    
    int n, l, d;
    
    cin >> n >> l >> d; 
    int need = n * d;
    int lm = l*1000;
    int r = ceil((double)need / lm) * l;
    
    cout << r << endl;
    return 0;
}
