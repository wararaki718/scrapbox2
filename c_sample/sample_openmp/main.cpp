#include <iostream>
#include <omp.h>

using namespace std;

int main()
{
    int N = 10;
    #pragma omp parallel for
    for(int i = 0; i < N; i++) {
        printf("%d\n", i);
    }
    return 0;
}