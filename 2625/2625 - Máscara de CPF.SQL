SELECT
  REGEXP_REPLACE(cpf,
                 '([[:digit:]]{3})([[:digit:]]{3})([[:digit:]]{3})([[:digit:]]{2})',
                 '\1.\2.\3-\4')
FROM natural_person
