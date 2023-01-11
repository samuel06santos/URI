#include <iostream>
#include <iomanip>
int main() {
    int km; std::cin >> km;
    double l; std::cin >> l;
    std::cout << std::fixed << std::setprecision(3) << km/l << " km/l" << std::endl;
    return 0;
}