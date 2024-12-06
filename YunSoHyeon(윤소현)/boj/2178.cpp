#include <iostream>
#include <queue>

using namespace std;
#define MAX 101
int visited[MAX][MAX];
int map[MAX][MAX];
int moving[MAX][MAX];
int n, m;

queue<pair<int, int>> q;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void bfs(int x, int y){
    visited[x][y] = true;
    q.push(make_pair(x, y));
    moving[x][y]++;

    while(!q.empty()){
        int curX = q.front().first;
        int curY = q.front().second;

        q.pop();

        for(int i = 0; i < 4; i++){
            int nextX = curX + dx[i];
            int nextY = curY + dy[i];

            if((0 <= nextX && nextX < n) && (0 <= nextY && nextY < m) && !visited[nextX][nextY] && map[nextX][nextY] == 1){
                visited[nextX][nextY] = 1;
                q.push(make_pair(nextX, nextY));
                moving[nextX][nextY] = moving[curX][curY] + 1;
            }
        }
    }
}

int main(){
    string str;

    cin >> n >> m;
    for (int i = 0; i < n; i++){
        cin >> str;
        for (int j = 0; j < m; j++)
            map[i][j] = str[j] - '0';
    }

    bfs(0, 0);

    cout << moving[n-1][m-1];
    return 0;
}
