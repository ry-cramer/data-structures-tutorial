import pandas as pd

data = {
    'Python Equivalent': ['stack.append()', 'stack.pop()', 'len(stack)'],
    'Operation Efficiency': ['O(1)', 'O(1)', 'O(1)']
}

df = pd.DataFrame(data, index = ['Push new item', 'Pop item off', 'Return size'])

print(df.to_markdown())