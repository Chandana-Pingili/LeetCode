/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> traversal(TreeNode root,int level,List<List<Integer>> ans)
    {
        if(root==null)
        return ans;
        if(level==ans.size())
        {
            List<Integer> sub=new ArrayList<>();
            sub.add(root.val);
            ans.add(sub);
        }
        else
        {
            ans.get(level).add(root.val);
        }
        ans=traversal(root.left,level+1,ans);
        ans=traversal(root.right,level+1,ans);
        return ans;


    }
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans=new ArrayList<>();
        return traversal(root,0,ans);
    }
}