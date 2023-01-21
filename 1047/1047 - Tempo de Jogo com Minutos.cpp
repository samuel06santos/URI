#include <iostream>
int main() {
    int hi, mi, hf, mf, th, tm;
    scanf("%d%*c%d%*c%d%*c%d", &hi, &mi, &hf, &mf);
    th = hf - hi;
    tm = mf - mi;
    if (tm < 0) {
        tm += 60;
        th -= 1;
    }
    if (tm == 0 && th <= 0) {
        th += 24;
    }
    if (th < 0) {
        th += 24;
    }
    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", th, tm);
    return 0;
}