#include <stdio.h>
#include <string.h>

int d[31][31];
int C(int n, int r) {
    if(n==r || r==0) return 1;
    if(d[n][r]>=0) return d[n][r];
    return d[n][r]=C(n-1,r)+C(n-1,r-1);
}

int main() {
    memset(d,-1,sizeof(d));
    int t;
    scanf("%d",&t);
    while(t--) {
        int n, m;
        scanf("%d %d",&n,&m);
        printf("%d\n",C(m,n));
    }
}