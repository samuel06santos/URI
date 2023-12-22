SELECT acc.id, acc.password, MD5(acc.password)
FROM account acc