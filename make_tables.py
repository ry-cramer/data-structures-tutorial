import pandas as pd

stack_data = {
    'Python Equivalent': ['stack.append()', 'stack.pop()', 'len(stack)'],
    'Operation Efficiency': ['O(1)', 'O(1)', 'O(1)']
}

stack_df = pd.DataFrame(stack_data, index = ['Push new item', 'Pop item off', 'Return size'])

print(stack_df.to_markdown())

bst_data = {
    'Operation Efficiency': ['O(log n)', 'O(log n)', 'O(log n)', 'O(log n)'],
    'Explanation': ['Recursive; searches for spot', 'Recursive; searches for node', 'Recursive; traverse left subtree and then right', 'Recursive; gets height of left and right subtree']
}

bst_df = pd.DataFrame(bst_data, index = ['Insert item', 'Delete item', 'Traverse', 'Get height'])

print(bst_df.to_markdown())