# Trees — Pattern Revision Cheat Sheet

Built from my own solutions (NeetCode `8-Trees` + FANG `Trees` folder). Read top to bottom before any tree interview. Each pattern is **trigger → trick → variants**.

---

## 0. Traversals — the base of everything

| Traversal | Order | Application |
|---|---|---|
| Preorder | val, left, right | print all root-to-leaf paths |
| Inorder | left, val, right | sort a BST (ascending) |
| Postorder | left, right, val | delete / prune (free children before parent) → see sec 11 |

All three are DFS. DFS = reach the end, backtrack via recursion.

- Every recursion depth **must** have a return, else `None` propagates up.
- Read recursive tree code **from the bottom**: the leaf returns first, then you stitch up.

---

## 1. Root-to-leaf path (preorder + backtracking)

**Trigger:** "all paths", "path sum", "root to leaf".

**Trick:** `append` on entry → if leaf, record → recurse L, R → `pop()` at the end. The list passed as an arg stays correct across siblings *because* of the pop (backtrack).

| LC | Problem | Note |
|---|---|---|
| 257 | Binary Tree Paths | join stack with `->` |
| 113 | Path Sum II | record only if running sum == target at leaf |
| 129 | Sum Root to Leaf | same as 257, accumulate `num*10 + val` down |
| 988 | Smallest String from Leaf | Amazon/Google, same path build, compare strings |
| 437 | Path Sum III | harder, carry a prefix-sum hashmap down |

---

## 2. Bool questions — return `f(left)` AND/OR `f(right)`

For any true/false tree question, always return `f(root.left)` and/or `f(root.right)`. Easiest way to propagate True/False up.

- **AND** → one false makes everything false (use when *both* sides must hold).
- **OR** → one true makes everything true (use when *any* side is enough).

Edge cases first, in this order:

```python
if not p and not q: return True
if not p or not q:  return False   # exactly one null
if p.val != q.val:  return False
return f(p.left, q.left) and f(p.right, q.right)
```

| LC | Problem | Note |
|---|---|---|
| 100 | Same Tree | the template above (alt: serialize preorder with None markers, compare) |
| 101 | Symmetric | mirror: `f(l.left, r.right) and f(l.right, r.left)` |
| 572 | Subtree | run sameTree at every node, OR up. Best (no helper): `if sameTree(root,sub): return True` else `isSubtree(left) or isSubtree(right)`. Optimize: only fire sameTree when `root.val == subRoot.val` |
| 951 | Flip Equivalent BT | Google, bool + AND/OR with both child orderings |

---

## 3. Height family (postorder, return height + capture side value)

Core: `height(root) = 1 + max(height(left), height(right))`, null → 0.

When I need height **and** another answer, use a helper that *returns* height and capture the real answer in an array arg `max_x=[0]` (or `nonlocal`). The array arg lets me read a value after the call without returning it.

| LC | Problem | Trick |
|---|---|---|
| 104 | Max Depth | `1 + max(L, R)`, base case |
| 110 | Balanced | helper returns height; track `max_diff[0] = abs(L-R)` per node; answer = `max_diff[0] <= 1` |
| 543 | Diameter | track `diameter[0] = max(diameter, L+R)`; **return `1 + max(L,R)`** (don't return `L+R+1`, it pollutes height) |
| 1448 | Good Nodes | preorder: carry `max_val` down; `res += dfs(L)+dfs(R)`; or return `left+right+1` when `root.val >= max_val` |
| 124 | Max Path Sum (HARD) | same shape as diameter but sum of values, clamp negatives to 0. **(don't have yet — add)** |
| 687 / 1372 | Longest Univalue Path / Longest ZigZag | diameter-style, different counter |
| 2265 | Count Nodes == Avg of Subtree | postorder, return `[sum, count]` tuple per node |

---

## 4. Tree DP — return a STATE tuple, not a number

When a node's answer depends on a **choice**, return `[stateA, stateB]` from dfs. Kills the need to peek at grandchildren or memoize.

**337 House Robber III** — dfs returns `[rob, skip]`:

```python
rob  = node.val + left_skip + right_skip
skip = max(left_rob, left_skip) + max(right_rob, right_skip)
# answer = max(rob, skip) at root.  O(n) time, O(h) space.
```

---

## 5. Validate BST — min/max window (NOT local compare)

- **Wrong:** checking only `root.left.val < root.val < root.right.val`. A deep node can violate an ancestor's bound — local checks miss it.
- **Right:** every node has a `(min, max)` window. Going **left** → new `max = root.val`. Going **right** → new `min = root.val`. Node must satisfy `min < val < max`.

| LC | Problem | Trick |
|---|---|---|
| 98 | Validate BST | `validBST(L, min, root.val) and validBST(R, root.val, max)`. BFS alt: queue of `[node, min, max]` |
| 230 | Kth Smallest in BST | inorder is sorted, return `arr[k-1]` (follow-up: early stop at k) |
| 99 | Recover BST | inorder to array, find 2 swapped nodes (first dip = `arr[i-1]`, second dip = `arr[i]`, keep updating second), swap vals |
| 671 | Second Min | dfs, `min_val = root.val` (root is global min); second = min of vals `> min_val` |
| 938 | Range Sum BST | BST pruning, 3 cases: in range → `val + dfs(L) + dfs(R)`; `val < low` → `dfs(R)` only; `val > high` → `dfs(L)` only. Iterative stack version is easy once you know the 3 cases. Meta variant: range average → return `[sum, count]` |
| 235 | LCA of BST | find the split: both `< root` → left; both `> root` → right; else this node is LCA. Iterative is cleaner |
| 270 / 285 / 173 | Closest BST Value / Inorder Successor / BST Iterator | LinkedIn/Amazon, all inorder-flavored |

---

## 6. LCA — Binary Tree (no BST property)

**236 LCA of Binary Tree** — postorder, return node if `root == p or q`:

```python
left  = lca(L)
right = lca(R)
# both non-null    -> root IS the LCA
# only one non-null-> return that one up (carries p or q upward)
# both null        -> None
```

Dry run to believe it. This is the canonical Amazon/Google/LinkedIn LCA.

- **1650** LCA III (nodes have parent ptrs, Meta) → walk up, set of ancestors, or two-pointer like linked-list intersection.
- **1123 / 2096** LCA of Deepest Leaves / Step-By-Step Directions → Google/Amazon, LCA + path.

---

## 7. Construct a tree

**105 — build from preorder + inorder** (med-hard):

```python
root = preorder[0]
idx  = inorder.index(root)          # left of idx = left subtree, right = right subtree
root.left  = build(pre[1:idx+1], inorder[:idx])
root.right = build(pre[idx+1:],  inorder[idx+1:])
```

- **106** from postorder + inorder → `root = postorder[-1]`, same inorder split, slice post accordingly. Optimize: hashmap for inorder index + pointers instead of slicing → O(n).
- **108** Sorted Array → BST: `mid = (l+r)//2 = root`; recurse halves; `l > r` → None (auto-balanced).
- **297** Serialize/Deserialize BT (HARD) → preorder with null markers; deserialize via iterator. **(don't have yet — top Amazon/Google/LinkedIn problem, add it.)**
- **449** Serialize/Deserialize BST → preorder, rebuild using BST bounds (no markers needed).

---

## 8. BFS / level order and all the "views"

**102 Level Order** — queue + `None` sentinel to mark level breaks. When you pop a `None`, push another `None` **only if the queue is non-empty**, else infinite loop. Append `currentOrder`, reset, continue.

Every "view" is just level order + a slice:

| LC | View | Slice / trick |
|---|---|---|
| 199 | Right Side View | `level[-1]` of each level |
| — | Left View | `level[0]` |
| 513 | Bottom-Left Value | `levelOrder[-1][0]` |
| 103 | ZigZag | level order + flag; reverse alternate levels (`currentOrder[::-1]`) |
| 107 | Level Order Bottom-Up | level order, reverse the result list |
| 314 | Vertical / Top View | BFS with `(node, col)`; left → `col-1`, right → `col+1`; `hashmap[col].append(val)`; track min/max col, iterate min..max instead of sorting |
| 987 | Vertical Order Traversal (HARD) | same + sort within a cell by `(row, val)`. Amazon/FB |
| 662 | Max Width | level order, index children `2i` / `2i+1`. Amazon |
| 116/117 | Next Right Pointers | BFS, **link when popping** (not on enqueue); reset `prev=None` at each level change; `if prev: prev.next=node; prev=node` |
| 958 | Check Completeness | BFS, once a null child is seen, any later non-null → False |
| 111 | Min Depth | BFS, first leaf hit = min depth (DFS must guard one-sided children) |

---

## 9. Structure mutation

- **226 Invert Tree** → swap L, R; recurse; return root.
- **114 Flatten to Linked List** → postorder, **return the tail** of each flattened subtree:

```python
leftTail  = dfs(L)
rightTail = dfs(R)
if leftTail:
    leftTail.right = root.right
    root.right = root.left
    root.left = None
return rightTail or leftTail or root   # the new tail
```

  (Tricky — should be Hard, not Medium.)
- **156 Binary Tree Upside Down** → niche, rewire so left becomes root each level.

---

## 10. Treat the tree as a graph

**Trigger:** "distance K", "nodes within k", "burn the tree", or anything needing to go **upward**.

**863 All Nodes Distance K** → build a parent map via dfs first, then BFS from target exploring left, right **and** parent. Use a visited set, collect when `lv == k`.

- Do the visited logic **inside** the loop like normal BFS, not right after pop.
- Let it run till the queue is empty. TC/SC = O(n).

Same idea: **1245** Tree Diameter (graph), **2385** Amount of Time to Infect (Amazon). Related: **366** Find Leaves of Binary Tree (LinkedIn/Amazon) → postorder by height bucket.

---

## 11. Deletion / pruning

Two flavors: prune leaves bottom-up (BT), or unlink one node keeping the BST valid.

### 11a. Delete leaves bottom-up (postorder) — 1325 Delete Leaves With a Given Value

Postorder. Recurse L and R **first and reassign**, then check if the node is now a leaf:

```python
root.left  = removeLeafNodes(root.left, target)
root.right = removeLeafNodes(root.right, target)
if not root.left and not root.right and root.val == target:
    return None
return root
```

Why postorder works: after children get pruned, a parent can *become* a leaf and also get pruned. Deletion cascades up. Pre/inorder would miss the cascade. This is the "postorder → delete" application from sec 0 as a real LC problem.

Same shape: **814** Binary Tree Pruning (Google/Amazon), **669** Trim a BST to `[low, high]` (BST + prune, return child up), **1110** Delete Nodes And Return Forest (Google, collect orphaned roots).

### 11b. Delete a node in a BST — 450 Delete Node in a BST

Step 1, search using BST property (reassign on the way down):

```python
if key < root.val: root.left  = deleteNode(root.left, key)
elif key > root.val: root.right = deleteNode(root.right, key)
```

Step 2, found it (`key == root.val`), 3 cases:

```python
if not root.left:  return root.right
if not root.right: return root.left
# both present: inorder successor = MIN of right subtree
curr = root.right
while curr.left: curr = curr.left
root.val = curr.val
root.right = deleteNode(root.right, curr.val)   # delete the dup recursively
```

Mirror option: predecessor = MAX of left subtree. Either works. Prereqs that make this trivial: BST insert/search + the inorder min/max walk. Related: **700** Search in BST, **701** Insert into BST, **99** Recover BST.

---

## Quick trigger → pattern map

| When the prompt says... | Reach for | Sec |
|---|---|---|
| paths / path sum | preorder + backtracking pop | 1 |
| is X / are equal / valid | bool AND/OR | 2 |
| depth / height / diameter / max | postorder height + side capture | 3 |
| rob / choose, parent affects child | tree DP state tuple | 4 |
| BST + valid / kth / range / closest | inorder OR min/max window OR pruning | 5 |
| lowest common ancestor | BST: split · BT: postorder return-node | 6, 7 |
| build / reconstruct / serialize | root + inorder split | 7 |
| level / view / zigzag / width | BFS + None sentinel + slice | 8 |
| flatten / invert / connect next | structure mutation | 9 |
| distance K / infect / burn | parent map + BFS as graph | 10 |
| delete / prune / trim nodes | postorder cascade (BT) · BST search + 3-case unlink | 11 |

---

## Reusable tricks (the stuff I keep forgetting)

1. Capture a side answer: array arg `max_x=[0]` or `nonlocal`. Read after the call.
2. Backtracking on a path list: append on entry, **pop** at end of function.
3. Return a tail/node up the recursion to stitch (flatten 114, LCA 236).
4. Return a tuple/state up when the answer needs a choice (337, range-avg, 2265).
5. BST = inorder is sorted. Almost every BST problem reduces to this or the min/max window.
6. Level breaks in BFS = `None` sentinel, re-push `None` only if the queue is non-empty.
7. Need to go **up** the tree = build a parent map, then it's a graph BFS.
8. Delete/prune = reassign `root.left` / `root.right` to the recursive call result, return root.

---

## Gaps — high-frequency for my targets, not in my folders yet

Targets: Google L3/L4, Amazon SDE1/2, LinkedIn equivalent.

| LC | Problem | Difficulty | Why |
|---|---|---|---|
| 297 | Serialize and Deserialize Binary Tree | HARD | Amazon/Google/LinkedIn staple. Top priority |
| 124 | Binary Tree Maximum Path Sum | HARD | Google/Amazon. NeetCode-150 tree I skipped. Add |
| 987 | Vertical Order Traversal of a BT | HARD | Amazon/FB. Harder 314 (sort within cell) |
| 1110 | Delete Nodes And Return Forest | MEDIUM | Google favorite (sec 11 follow-up) |
| 669 | Trim a Binary Search Tree | MEDIUM | BST prune (sec 11 follow-up) |
| 173 | Binary Search Tree Iterator | MEDIUM | Amazon/LinkedIn (inorder + design) |
| 285 | Inorder Successor in BST | MEDIUM | LinkedIn/Amazon |
| 2385 | Amount of Time to Infect Binary Tree | MEDIUM | Amazon (sec 10 parent-map BFS) |
| 1026 | Max Diff Between Node and Ancestor | MEDIUM | carry min/max down (good-nodes shape) |
