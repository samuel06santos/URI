#include <iostream>
#include <iomanip>
int main() {
    float a, b, c;
    std::cin >> a; std::cin >> b; std::cin >> c;
    std::cout << "MEDIA = " << std::fixed << std::setprecision(1)<< (a*2 + b*3 + c*5 )/10 << std::endl;
    return 0;
}
