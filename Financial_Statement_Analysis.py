
# coding: utf-8

# In[9]:


#Data 
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]


# In[13]:


#calculation profit
profit = list([])
for i in range(0, len(revenue)):
    profit.append( revenue[i] - expenses[i])
 
profit


# In[15]:


#calculation tax
tax = [round(i * 0.3,2) for i in profit]
tax


# In[16]:


#profit after tax
profit_after_tax = list([])

for i in range(0, len(profit)):
    profit_after_tax.append(profit[i] - tax[i])
    
profit_after_tax


# In[18]:


#profit margin after tax
profit_margin = list([])

for i in range(0, len(profit)):
    profit_margin.append(profit_after_tax[i] / revenue[i])

profit_margin = [round(i*100 ,2) for i in profit_margin]
profit_margin


# In[20]:


#profit after tax mean
mean_pat = sum(profit_after_tax) / len(profit_after_tax)
mean_pat


# In[21]:


good_months = list([])

for i in range(0, len(profit)):
    good_months.append(profit_after_tax[i] > mean_pat)
    
good_months


# In[22]:


bad_months = list([])

for i in range(0, len(profit)):
    bad_months.append(profit_after_tax[i] < mean_pat)
    
bad_months


# In[29]:


best_month = list([])

for i in range(0, len(profit)):
    best_month.append(profit_after_tax[i] == max(profit_after_tax))
    
best_month


# In[28]:


worst_month = list([])

for i in range(0, len(profit)):
    worst_month.append(profit_after_tax[i] == min(profit_after_tax))
    
worst_month


# In[27]:


#convert all calculatons to units of on thousand dollars 
revenue_1000 = [int(round(i /1000,2)) for i in revenue]
expenses_1000 = [int(round(i /1000,2)) for i in expenses]
profit_1000 = [int(round(i /1000,2)) for i in profit]
profit_after_tax_1000 = [int(round(i /1000,2)) for i in profit_after_tax]


# In[30]:


#print results
print("Revenue: ")
print(revenue_1000)
print("Expenses: ")
print(expenses_1000)
print("Profit: ")
print(profit_1000)
print("Profit_after_tax: ")
print(profit_after_tax_1000)
print("Good months: ")
print(good_months)
print("Bad months: ")
print(bad_months)
print("Best month: ")
print(best_month)
print("Worst month: ")
print(worst_months)

