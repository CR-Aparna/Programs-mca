//Prims algorithm

#include<stdio.h>
#include<stdlib.h>
#define MAX 20
 
int i,j,cost[MAX][MAX],n,visited[MAX]={0},a,b,mincost=0;

void main(){
	printf("Enter the number of vertices:");
	scanf("%d",&n);
	printf("Enter the cost adjacency matrix:\n");
	for(i=1;i<=n;i++){
		for(j=1;j<=n;j++){
			scanf("%d",&cost[i][j]);
			if(cost[i][j]==0){
				cost[i][j]=999;
			}
		}
	}
	visited[1]=1;
	for(int k=1;k<=n;k++){
		int min=999;
		for(i=1;i<=n;i++){
			for(j=1;j<=n;j++){
				if(cost[i][j]<min){
					min=cost[i][j];
					a=i;
					b=j;
				}
			}
		}
		if(visited[a]==0||visited[b]==0){
			printf("\nEdge:%d %d-->%d\n",k,a,b);
			printf("\n Cost:%d\n",min);
			mincost=mincost+min;
			visited[b]=1;
		}
		cost[a][b]=999;
	}
	printf("\n Total cost cost is:%d",mincost);
}
