# TREES - PATTERN REVISION CHEAT SHEET
# Built from my own solutions (Neetcode 8-Trees + FANG Trees folder)
# Read top to bottom before any tree interview. Each pattern = trigger + my trick + variants.

#############################################
# 0. TRAVERSALS - the base of everything
#############################################

# preorder  (val, left, right)  -> print val first, then go left, then right
# inorder   (left, val, right)  -> keep going left, print, then right
# postorder (left, right, val)  -> print only after BOTH children visited
# All 3 are DFS. DFS = reach the end, backtrack via recursion.

# APPLICATIONS (memorize this mapping):
# preorder  -> print all root-to-leaf paths
# inorder   -> sort a BST (gives ASCENDING order)
# postorder -> delete a tree / prune leaves (free children before parent) -> see sec 11 (1325, 814, 669)

# [IMP] every recursion depth MUST have a return, else None propagates up.
# Read recursive tree code FROM THE BOTTOM (leaf returns first, then stitch up).

#############################################
# 1. ROOT-TO-LEAF PATH pattern (preorder + backtracking)
#############################################
# Trigger: "all paths", "path sum", "root to leaf"
# Trick: stack.append on entry -> if leaf, record -> recurse L,R -> stack.pop() at end
# The list passed as arg stays constant across siblings BECAUSE of the pop (backtrack).

# 257 Binary Tree Paths      -> join stack with "->"
# 113 Path Sum II            -> same, but record only if running sum == target at leaf
# 129 Sum Root to Leaf       -> SAME LOGIC as 257, accumulate num*10+val down
# 988 Smallest String from Leaf (Amazon/Google) -> same path build, compare strings
# 437 Path Sum III (prefix-sum on tree) -> harder, carry prefix-sum hashmap down

#############################################
# 2. BOOL questions - return f(left) AND/OR f(right)
#############################################
# [IMP] For any true/false tree question, ALWAYS return f(root.left) and/or f(root.right).
# Easiest way to propagate True/False UP.
#   AND -> ONE false makes everything false  (use when BOTH sides must hold)
#   OR  -> ONE true makes everything true    (use when ANY side is enough)
# Edge cases FIRST, in this order:
#   not p and not q -> True
#   not p or not q  -> False  (exactly one null)
#   p.val != q.val  -> False
#   then: return f(p.left,q.left) AND f(p.right,q.right)

# 100 Same Tree     -> the template above. (Alt: serialize preorder WITH None markers, compare)
# 101 Symmetric     -> mirror version: f(l.left, r.right) AND f(l.right, r.left)
# 572 Subtree       -> run sameTree at EVERY node, OR the results up.
#                      Best soln (no helper): if sameTree(root,sub): return True
#                      return isSubtree(left) OR isSubtree(right)
#                      Optimize calls: only fire sameTree when root.val == subRoot.val
# 951 Flip Equivalent BT (Google) -> bool + AND/OR with both child orderings

#############################################
# 3. HEIGHT family (postorder, return height + capture side value)
#############################################
# Core: height(root) = 1 + max(height(left), height(right)); null -> 0
# [TIP] When I need height AND another answer, use a helper that RETURNS height
#       and capture the real answer in an array arg max_x=[0] (or nonlocal). Array arg
#       lets me read a value after the call WITHOUT returning it.

# 104 Max Depth        -> 1 + max(L,R). base case.
# 110 Balanced         -> helper returns height, track max_diff[0] = abs(L-R) per node;
#                         answer = max_diff[0] <= 1
# 543 Diameter         -> per node track diameter[0] = max(diameter, L+R);
#                         RETURN 1+max(L,R) (don't return L+R+1, that pollutes height) [THINK]
# 1448 Good Nodes      -> preorder: carry max_val DOWN; res += dfs(L)+dfs(R);
#                         or return left+right+1 when root.val >= max_val
# 124 Binary Tree Max Path Sum (HARD) -> SAME shape as diameter but sum of values, clamp
#                         negatives to 0. (I DON'T have this yet - high value, add it)
# 687 Longest Univalue Path / 1372 Longest ZigZag -> diameter-style, different counter
# 2265 Count Nodes == Avg of Subtree -> postorder return [sum, count] tuple per node

#############################################
# 4. TREE DP - return a STATE tuple, not a number
#############################################
# Trick: when a node's answer depends on a CHOICE, return [stateA, stateB] from dfs.
# Kills the need to peek at grandchildren or memoize.

# 337 House Robber III -> dfs returns [rob, skip]
#   rob  = node.val + left_skip + right_skip
#   skip = max(left_rob,left_skip) + max(right_rob,right_skip)
#   answer = max(rob, skip) at root. O(n) time, O(h) space.

#############################################
# 5. VALIDATE BST - min/max window (NOT local compare)
#############################################
# [WRONG] checking only root.left.val < root.val < root.right.val. A deep node can
#         violate an ancestor's bound. Local checks miss it. [THINK]
# [RIGHT] every node has a (min, max) window. Going LEFT -> new max = root.val.
#         Going RIGHT -> new min = root.val. Node must satisfy min < val < max.

# 98 Validate BST -> pass (min,max) as args: validBST(L, min, root.val) AND validBST(R, root.val, max)
#                    BFS alt: queue of [node, min, max].
# 230 Kth Smallest in BST -> inorder gives sorted, return arr[k-1]. (Follow-up: early stop at k)
# 99 Recover BST -> inorder to array, find the 2 swapped nodes (first dip = arr[i-1],
#                   second dip = arr[i], keep updating second), swap their vals.
# 671 Second Min -> dfs, min_val = root.val (root is global min by problem); second = min of vals > min_val
# 938 Range Sum BST -> BST PRUNING, 3 cases:
#       in range  -> root.val + dfs(L) + dfs(R)
#       val < low -> dfs(R) only   (left can't be in range)
#       val > high-> dfs(L) only
#     Iterative stack version is easy once you know the 3 cases.
#     Variant (Meta): range AVERAGE -> return [sum,count] tuple.
# 235 LCA of BST -> look for the SPLIT.
#       both < root -> go left; both > root -> go right; else THIS node is LCA.
#       Iterative is cleaner than recursion here.
# 270 Closest BST Value / 285 Inorder Successor BST / 173 BST Iterator -> LinkedIn/Amazon, all inorder-flavored

#############################################
# 6. LCA - Binary Tree (NO BST property)
#############################################
# 236 LCA of Binary Tree -> postorder, return node if root == p or q.
#       left = lca(L); right = lca(R)
#       both non-null -> root IS the LCA
#       only one non-null -> return that one UP (carries p or q upward)
#       both null -> None
#   Dry run to believe it. This is the canonical Amazon/Google/LinkedIn LCA.
# 1650 LCA III (nodes have parent ptrs, Meta) -> walk up, set of ancestors, or two-pointer like linked-list intersection
# 1123 LCA of Deepest Leaves (Google) / 2096 Step-By-Step Directions (Google/Amazon, LCA + path)

#############################################
# 7. CONSTRUCT a tree
#############################################
# 105 Build from preorder+inorder [MED-HARD]:
#       root = preorder[0]; idx = inorder.index(root)
#       inorder left of idx = left subtree, right of idx = right subtree
#       root.left  = build(pre[1:idx+1], in[:idx])
#       root.right = build(pre[idx+1:], in[idx+1:])
# 106 from postorder+inorder -> root = postorder[-1], same inorder split, slice post accordingly
#   (optimize: use a hashmap for inorder index + pointers instead of slicing -> O(n))
# 108 Sorted Array -> BST: mid = (l+r)//2 = root; recurse halves; l>r -> None (auto-balanced)
# 297 Serialize/Deserialize BT (HARD) -> preorder with null markers; deserialize via iterator.
#   (I DON'T have this yet - it's a top Amazon/Google/LinkedIn problem, ADD IT)
# 449 Serialize/Deserialize BST -> preorder, rebuild using BST bounds (no markers needed)

#############################################
# 8. BFS / LEVEL ORDER and all the "views"
#############################################
# 102 Level Order -> queue + None sentinel to mark level breaks.
#   [IMP] when you pop a None, push another None ONLY if queue is non-empty,
#         else infinite loop. Append currentOrder, reset, continue.
# Every "view" is just level order + a slice:
#   199 Right Side View  -> level[-1] of each level
#   (Left View)          -> level[0]
#   513 Bottom-Left Value-> levelOrder[-1][0]
# 103 ZigZag Level Order -> level order + flag; reverse alternate levels (currentOrder[::-1])
# 107 Level Order Bottom-Up -> level order, reverse the result list
# 314 Vertical Order (TOP/VERTICAL VIEW) -> BFS with (node, col).
#       left -> col-1, right -> col+1. hashmap[col].append(val).
#       track min_col/max_col, iterate min..max instead of sorting.
#       987 Vertical Order Traversal (HARD) = same + sort within a cell by (row,val). Amazon/FB.
# 662 Max Width of Binary Tree (Amazon) -> level order, index children 2i / 2i+1
# 116/117 Populating Next Right Pointers -> BFS, LINK WHEN POPPING (not on enqueue).
#       reset prev=None at each level change. if prev: prev.next=node; prev=node.
# 958 Check Completeness -> BFS, once a null child is seen, any later NON-null -> False.
# 111 Min Depth -> BFS, first leaf hit = min depth (DFS must guard one-sided children)

#############################################
# 9. STRUCTURE MUTATION
#############################################
# 226 Invert Tree -> swap L,R; recurse; return root.
# 114 Flatten to Linked List -> postorder, RETURN the TAIL of each flattened subtree.
#       leftTail = dfs(L); rightTail = dfs(R)
#       if leftTail: leftTail.right = root.right; root.right = root.left; root.left = None
#       return rightTail or leftTail or root   # the new tail
#   (Tricky, should be Hard not Medium.)
# 156 Binary Tree Upside Down -> niche, rewire left becomes root each level

#############################################
# 10. TREAT THE TREE AS A GRAPH
#############################################
# Trigger: "distance K", "nodes within k", "burn the tree", need to go UPWARD too.
# 863 All Nodes Distance K -> build parent map via dfs first, then BFS from target
#       exploring left, right AND parent. visited set. collect when lv == k.
#       [IMP] do visited logic INSIDE the loop like normal BFS, not right after pop.
#       Let it run till queue empty; TC/SC = O(n).
# 1245 Tree Diameter (graph) / 2385 Amount of Time to Infect (Amazon) -> same parent-map + BFS
# 366 Find Leaves of Binary Tree (LinkedIn/Amazon) -> postorder by height bucket

#############################################
# 11. DELETION / PRUNING
#############################################
# Two flavors: prune leaves bottom-up (BT), or unlink one node keeping BST valid.

# --- 11a. Delete leaves bottom-up (postorder) ---
# 1325 Delete Leaf Nodes (Delete Leaves With a Given Value)
# [IMP] postorder. Recurse L and R FIRST and REASSIGN:
#       root.left  = removeLeafNodes(root.left, target)
#       root.right = removeLeafNodes(root.right, target)
#   then: if leaf and root.val == target -> return None, else return root.
# Why postorder works: after children get pruned, a parent can BECOME a leaf and
# also get pruned. Deletion cascades UP. Pre/inorder would miss the cascade.
# This is the "postorder -> delete" application (sec 0) as an actual LC problem.
#   Same shape:
#   814  Binary Tree Pruning (remove all-0 subtrees)   | Google/Amazon
#   669  Trim a BST to [low,high]                       | BST + prune, return child up
#   1110 Delete Nodes And Return Forest                 | Google, collect orphaned roots

# --- 11b. Delete a node in a BST (keep it valid) ---
# 450 Delete Node in a BST -> watch: youtube.com/watch?v=LFzAoJJt92M
# Step 1: SEARCH using BST property (reassign on the way down):
#       key < root.val -> root.left  = deleteNode(root.left, key)
#       key > root.val -> root.right = deleteNode(root.right, key)
# Step 2: found it (key == root.val), 3 cases:
#       no left  -> return root.right
#       no right -> return root.left
#       both     -> find inorder successor = MIN of right subtree (curr=root.right; while curr.left: curr=curr.left)
#                   copy succ.val into root.val
#                   then root.right = deleteNode(root.right, succ.val)  # delete the dup recursively
#   (Mirror option: predecessor = MAX of left subtree. Either works.)
# Prereqs that make this trivial: BST insert/search + the inorder min/max walk.
#   Related: 700 Search in BST, 701 Insert into BST, 99 Recover BST (the min/max + inorder ideas).

#############################################
# QUICK TRIGGER -> PATTERN MAP
#############################################
# "paths / path sum"            -> preorder + backtracking pop (sec 1)
# "is X / are equal / valid"    -> bool AND/OR (sec 2)
# "depth/height/diameter/max"   -> postorder height + side capture (sec 3)
# "rob/choose, parent affects"  -> tree DP state tuple (sec 4)
# "BST + valid/kth/range/closest"-> inorder OR min/max window OR pruning (sec 5)
# "lowest common ancestor"      -> BST: split | BT: postorder return-node (sec 6,7)
# "build/reconstruct/serialize" -> root + inorder split (sec 7)
# "level / view / zigzag / width"-> BFS + None sentinel + slice (sec 8)
# "flatten/invert/connect next" -> structure mutation (sec 9)
# "distance K / infect / burn"  -> parent map + BFS as graph (sec 10)
# "delete/prune/trim nodes"     -> postorder cascade (BT) | BST search + 3-case unlink (sec 11)

#############################################
# REUSABLE TRICKS (the stuff I keep forgetting)
#############################################
# 1. Capture a side answer: array arg max_x=[0] OR nonlocal. Read after the call.
# 2. Backtracking on a path list: append on entry, POP at end of function.
# 3. Return a TAIL/NODE up the recursion to stitch (flatten 114, LCA 236).
# 4. Return a TUPLE/STATE up when answer needs a choice (337, range-avg, 2265).
# 5. BST = inorder is sorted. Almost every BST problem reduces to this or min/max window.
# 6. Level breaks in BFS = None sentinel, re-push None only if queue non-empty.
# 7. Need to go UP the tree = build a parent map, then it's a graph BFS.
# 8. Delete/prune = reassign root.left/root.right to the recursive call result, return root.

#############################################
# GAPS - high-frequency for my targets, NOT in my folders yet
# (Google L3/L4, Amazon SDE1/2, LinkedIn)
#############################################
# 297 Serialize and Deserialize Binary Tree  | HARD   | Amazon/Google/LinkedIn staple. TOP priority.
# 124 Binary Tree Maximum Path Sum           | HARD   | Google/Amazon. NeetCode-150 tree I skipped. ADD.
# 987 Vertical Order Traversal of a BT       | HARD   | Amazon/FB. harder 314 (sort within cell).
# 1110 Delete Nodes And Return Forest        | MEDIUM | Google favorite (sec 11 follow-up).
# 669 Trim a Binary Search Tree              | MEDIUM | BST prune (sec 11 follow-up).
# 173 Binary Search Tree Iterator            | MEDIUM | Amazon/LinkedIn (inorder + design).
# 285 Inorder Successor in BST               | MEDIUM | LinkedIn/Amazon.
# 2385 Amount of Time to Infect Binary Tree  | MEDIUM | Amazon (sec 10 parent-map BFS).
# 1026 Max Diff Between Node and Ancestor    | MEDIUM | carry min/max down (good-nodes shape).
