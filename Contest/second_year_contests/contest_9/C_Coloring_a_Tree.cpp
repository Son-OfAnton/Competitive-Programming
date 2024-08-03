#include <stdio.h>
using namespace std;

int fa[20010],c[20010];
int n,m;

int main(){
    while(scanf("%d",&n)!=EOF){
        fa[1] = 1;
        for(int i = 2; i <= n; ++i){
            scanf("%d",&fa[i]);
        }

        for(int i = 1; i <= n; ++i){
            scanf("%d",&c[i]);
        }

        int ans = 0;
        for(int i = 1; i <= n; ++i){
            if(c[i] != c[fa[i]]){
                ++ans;
            }
        }

        printf("%d\n",ans + 1);
    }
    return 0;
}