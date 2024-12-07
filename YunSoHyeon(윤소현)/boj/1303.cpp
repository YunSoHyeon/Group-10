//
// 
//
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

#define MAX 101

bool visited[MAX][MAX];
char map[MAX][MAX];
int n, m;
int dx[4] = {1, -1, 0 , 0};
int dy[4] = {0, 0, 1, -1};
int white, blue;

void bfs(int start, int end, char team){
    queue<pair<int, int>> q;
    visited[start][end] = true;
    q.push({ start, end });

    int cnt = 0;
    while(!q.empty()){
        int curX = q.front().first;
        int curY = q.front().second;
        q.pop();
        cnt++;

        for (int i = 0; i < 4; ++i) {
            int x = curX + dx[i];
            int y = curY + dy[i];

            if((x >= 1 && x <= m) && (y >= 1 && y <= n) && !visited[x][y] && map[x][y] == team){
                visited[x][y] = true;
                q.push(make_pair(x, y));
            }

        }
    }
    if (team == 'W')
        white += cnt * cnt;

    if (team == 'B')
        blue += cnt * cnt;
}
int main(){
    cin >> n >> m;
    for(int i = 1; i <= m; i++)
        for(int j = 1; j <= n; j++)
            cin >> map[i][j];

    for(int i = 1; i <= m; i++)
        for(int j = 1; j <= n; j++)
            if (!visited[i][j])
                bfs(i, j, map[i][j]);

    cout << white << " " << blue;
    return 0;
}
