import graphviz
dot = graphviz.Digraph('round-table', comment='The Round Table')
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

dot.edges(['AB', 'AL'])
dot.edge('B', 'L', costraing='false')

print(dot.source)

#doctest_mark_exe()
dot.render(directory='doctest-output', view=True).replace('\\', '/')
