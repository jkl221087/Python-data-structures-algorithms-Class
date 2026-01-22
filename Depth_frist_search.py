class DFSGraph:
    def __init__(self):
        self.adj = {}

        self.color = {}
        self.pi = {}
        self.d = {}
        self.f = {}


        self.time = 0


# u = node v = 鄰居
#self.adj[u] = [] = u :[]
    def add_edge(self,u, v):
        if u not in self.adj: self.adj[u] = []
        if v not in self.adj: self.adj[v] = []
#self.adj[u] = [] = u :[v]
        self.adj[u].append(v)
        self.adj[v].append(u)
##self.adj[v] = []
        if v not in self.adj: self.adj[v] = []
    

# WHITE = 沒被探訪
# PI = 被探訪過的前一個Node
    def dfs(self):
        for u in self.adj:
            self.color[u] = 'WHITE'
            self.pi[u] = None

        self.time = 0


        for u in sorted(self.adj.keys()):
            if self.color[u] == 'WHITE':
                self.dfs_visit(u)



#GREY被探訪但未結束
#color[u] = 目前狀態
#d[u]discover time node u第一次被發現的時間
    def dfs_visit(self, u):
        self.color[u] = 'GREY'

        self.time += 1
        self.d[u] = self.time
        print(f"被發現node {u} (Time:{self.time})")


        for v in sorted(self.adj.get(u, [])):
            if self.color[v] == 'WHITE':
                self.pi[v] = u
                self.dfs_visit(v)

        #Black = 結束
        self.color[u] = 'BLACK'

        # f[u] finish time node u 結束的時間
        self.time += 1
        self.f[u] = self.time
        print(f"結束node {u} (Time: {self.time})")


if __name__ == "__main__":
    # 建立一個簡單的圖
        # u -> v, x
        # v -> y
        # x -> v
        # y -> x, z
        # z -> z
    g = DFSGraph()
    g.add_edge('u', 'v')
    g.add_edge('u', 'x')
    g.add_edge('v', 'y')
    g.add_edge('x', 'v')
    g.add_edge('y', 'x')
    g.add_edge('y', 'z')
    g.add_edge('z', 'z') # 自環
    
    print("--- 開始 DFS ---")
    g.dfs()
    
    print("\n--- 最終結果 (d/f 時間戳記) ---")
    for node in sorted(g.adj.keys()):
        print(f"Node {node}: d={g.d[node]}, f={g.f[node]}, parent={g.pi[node]}")