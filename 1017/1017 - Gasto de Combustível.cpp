#include <iostream>
#include <iomanip>
int main() {
    int h, vel;
    std::cin >> h; std::cin >> vel;
    std::cout << std::fixed << std::setprecision(3) << (vel*h)/12.0 << std::endl;
    return 0;
}