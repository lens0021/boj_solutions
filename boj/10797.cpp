#include <cstdio>
int main(void) {
    int day;
    scanf("%d", &day);
    int num = 0, car;
    for(int i = 0; i < 5; i++) {
        scanf(" %d", &car);
        if( car == day ) {
            num++;
        }
    }
    printf("%d", num);
}
