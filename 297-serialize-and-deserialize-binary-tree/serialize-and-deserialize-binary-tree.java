public class Codec {

    private String[] values;
    private int index;

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {

        if (root == null) {
            return "null,";
        }

        return root.val + ","
                + serialize(root.left)
                + serialize(root.right);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {

        values = data.split(",");
        index = 0;

        return buildTree();
    }

    private TreeNode buildTree() {

        String value = values[index++];

        if (value.equals("null")) {
            return null;
        }

        TreeNode root = new TreeNode(Integer.parseInt(value));

        root.left = buildTree();
        root.right = buildTree();

        return root;
    }
}