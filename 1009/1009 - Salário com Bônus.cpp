#include <iostream>
#include <iomanip>
int main() {
    char a[25]; double b, c;
    std::cin >> a; std::cin >> b; std::cin >> c;
    std::cout << "TOTAL = R$ " << std::fixed << std::setprecision(2) << (c*0.15) + b << std::endl;
    return 0;
}
