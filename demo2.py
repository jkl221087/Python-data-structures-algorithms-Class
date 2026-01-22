class DFSGraph:
    def __init__(self):
        # 使用鄰接表 (Adjacency List) 來儲存圖
        self.adj = {}
        
        # 對應圖片中的四個屬性陣列
        self.color = {}  # 顏色：WHITE, GREY, BLACK
        self.pi = {}     # π (前驅節點/父節點)
        self.d = {}      # discover time (發現時間)
        self.f = {}      # finish time (結束時間)
        
        # 全域計時器
        self.time = 0

    def add_edge(self, u, v):
        """加入有向邊 u -> v"""
        if u not in self.adj: self.adj[u] = []
        if v not in self.adj: self.adj[v] = []
        self.adj[u].append(v)
        # 確保 v 也在 adj 中 (即使它沒有連出去的邊)
        if v not in self.adj: self.adj[v] = []

    def dfs(self):
        """對應圖片中的 DFS(G) 主程式"""
        # 1. 初始化所有節點
        # Python 的字典鍵值即為 V[G]
        for u in self.adj:
            self.color[u] = 'WHITE'
            self.pi[u] = None
        
        # 2. 時間歸零
        self.time = 0
        
        # 3. 遍歷所有節點，若為白色則開始探索
        # 為了確保輸出順序固定，這裡先對鍵值排序 (選擇性)
        for u in sorted(self.adj.keys()):
            if self.color[u] == 'WHITE':
                self.dfs_visit(u)
    
    def dfs_visit(self, u):
        """對應圖片中的 DFS-VISIT(u)"""
        # 1. 標記為灰色 (發現)
        self.color[u] = 'GREY'
        
        # 2. 時間 + 1 並紀錄發現時間 d[u]
        self.time += 1
        self.d[u] = self.time
        print(f"發現節點 {u} (Time: {self.time})")

        # 3. 檢查所有鄰居 v
        # get(u, []) 是為了防止 u 是沒有出邊的節點
        for v in sorted(self.adj.get(u, [])):
            if self.color[v] == 'WHITE':
                self.pi[v] = u
                self.dfs_visit(v)
        
        # 4. 標記為黑色 (結束)
        self.color[u] = 'BLACK'
        
        # 5. 時間 + 1 並紀錄結束時間 f[u]
        self.time += 1
        self.f[u] = self.time
        print(f"結束節點 {u} (Time: {self.time})")

# --- 測試範例 ---
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