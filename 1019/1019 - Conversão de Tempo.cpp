#include <iostream>
int main() {
    int sec, h, h2, m, m2, s;
    std::cin >> sec;
    h = sec/3600; h2 = sec % 3600;
    m = h2/60; m2 = h2 % 60;
    s = m2 % 60;
    printf("%d:%d:%d", h, m, s);
    return 0;
}