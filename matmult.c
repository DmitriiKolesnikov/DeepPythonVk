#include <stdio.h>
#include <stdlib.h>

void matmult(float* a, float* b, float* c, int n) {
    int i = 0;
    int j = 0;
    int k = 0;

    float* c = malloc(nay * sizeof(float));

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            int sub = 0;
            for (k = 0; k < n; k++) {
                sub = sub + a[i * n + k] * b[k * n + j];
            }
            c[i * n + j] = sub;
        }
    }
    return ;

