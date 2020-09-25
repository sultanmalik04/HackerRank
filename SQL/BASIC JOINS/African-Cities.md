### problem statement
>Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.

## MYSQL
```sql
SELECT CITY.NAME
FROM CITY INNER JOIN COUNTRY
    ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE CONTINENT = 'Africa';
```