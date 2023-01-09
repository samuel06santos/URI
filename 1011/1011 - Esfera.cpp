#include <iostream>
#include <iomanip>

int main() {
    double r, pi;
    std::cin >> r;
    pi = 3.14159;
    std::cout << "VOLUME = " << std::fixed << std::setprecision(3) << (4.0/3)*pi*r*r*r << std::endl;
    return 0;
}