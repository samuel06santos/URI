#include <iostream>
int main() {
    int v;
    int array[] = {100, 50, 20, 10, 5, 2, 1};
    scanf("%d", &v);
    
    printf("%d\n", v);
    for (int i = 0; i<sizeof(array)/4; i++) {
        printf("%d nota(s) de R$ %d,00\n", v/array[i], array[i], v%array[i] );
        v %= array[i];
    }
    return 0;
}