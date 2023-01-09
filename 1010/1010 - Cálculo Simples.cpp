#include <iostream>
int main() {
    int c, u1, u2;
    float v1, v2;
    scanf("%d%*c%d%*c%f", &c, &u1, &v1);
    scanf("%d%*c%d%*c%f", &c, &u2, &v2);
    printf("VALOR A PAGAR: R$ %.2f\n", (u1*v1)+(u2*v2));
    return 0;
}