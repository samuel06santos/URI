#include <iostream>
#include <iomanip>
#include <cmath>

int main() {
    double x1, x2, y1, y2;
    scanf("%lf%*c%lf", &x1, &y1);
    scanf("%lf%*c%lf", &x2, &y2);
    double d = pow( pow(x2 - x1, 2) + pow(y2 - y1, 2), 0.5);
    std::cout << std::fixed << std::setprecision(4) << d << std::endl;
    return 0;
}