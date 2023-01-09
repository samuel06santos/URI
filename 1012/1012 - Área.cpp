#include <iostream>
#include <iomanip>
int main() {
    double a, b, c, pi;
    pi = 3.14159;
    scanf("%lf%*c%lf%*c%lf", &a, &b, &c);
    printf("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f\n"
    , (a*c)/2, pi*(c*c), ((a+b)*c)/2.0, b*b, a*b);
    return 0;
}