#include <iostream>
#include <iomanip>
int main() {
    int a, b; float c;
    std::cin >> a; std::cin >> b; std::cin >> c;
    std::cout << "NUMBER = " << a << std::endl << "SALARY = U$ " << std::fixed << std::setprecision(2)<< b*c <<std::endl;
    return 0;
}
