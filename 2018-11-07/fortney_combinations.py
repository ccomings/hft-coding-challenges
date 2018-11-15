
# coding: utf-8

# In[27]:


import itertools


# In[29]:


nums = (-1, 0, 1, 2, -1, -4)


# In[33]:


combos_list = list(itertools.combinations(nums, 3))


# In[34]:


def zero_checker(combos):
    
    sum_zero_combos = []
    
    for comb in combos:
        combo_sum = sum(comb)
        if combo_sum == 0:
            sum_zero_combos.append(comb)
    
    return sum_zero_combos


# In[35]:


zero_checker(combos_list)

