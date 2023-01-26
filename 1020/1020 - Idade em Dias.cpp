#include <iostream>
int main() {
    int age;
    std::cin >> age;
    printf("%d ano(s)\n", age/365);
    age %= 365;
    printf("%d mes(es)\n", age/30);
    age %= 30;
    printf("%d dia(s)\n", age);
    return 0;
}
