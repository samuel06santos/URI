#include <iostream>
#include <cstdlib>
int main() {
    int a, b, c;
    std::cin >> a; std::cin >> b; std::cin >> c;
    int maior = (a + b + abs(a-b))/2;
    int maior2 = (maior + c + abs(maior-c))/2;
    std::cout << maior2 << " eh o maior" << std::endl;
    return 0;
}