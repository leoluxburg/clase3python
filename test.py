rmd = ['benzema', 'leo', 'vini']
rmd.append('luca')
print(rmd)

rmd.insert(1, 'toni')
print(rmd)

rmd_old = ['raul', 'cr7']

rmd.extend(rmd_old)
print(rmd)

rmd.pop(1)
print(rmd)