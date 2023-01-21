#include <iostream>
int main() {
    int age;
    std::cin >> age;
    printf("%d ano(s)\n", age/365);
    age %= 365;
    printf("%d mes(s)\n", age/30);
    age %= 30;
    printf("%d dias(s)\n", age);
    return 0;
}