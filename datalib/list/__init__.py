filter_func = lambda x, lst: all(i not in x for i in lst)
select_func = lambda x, lst: any(i in x for i in lst)

"""
select True will return the intercept. otherwise, it will filter
"""
def intercept(list_one, list_two, select=True):
  func = select_func if select else filter_func
  return list(filter(lambda x: func(x, list_one), list_two))
