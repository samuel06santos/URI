#include <iostream>
#include <iomanip>
int main() {
    double pi = 3.14159;
    double r;
    std::cin >> r;
    std::cout << std::fixed << std::setprecision(4);
    std::cout << "A=" << pi*(r*r) << std::endl;
    return 0;
}
