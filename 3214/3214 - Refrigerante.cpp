#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(nullptr);
    
    int e, f, c;
    cin >> e >> f >> c;
    
    int vazias = e + f;
    int bebidos = 0;
    
    while (vazias >= c) {
        int novas = vazias / c;
        bebidos += novas;
        vazias = novas + (vazias % c);
    }
    
    cout << bebidos << "\n";
    return 0;
}
