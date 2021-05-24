#include <stdio.h>

int rel(){
    printf("hi");
    return 2;
}

int main(){
    int c = 0;
    int a = 0;
    int b = a + c;
    rel();
    return 0;
}