## problem statement
> Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

## MYSQL
```sql
SELECT SUM(CITY.POPULATION)
FROM CITY INNER JOIN COUNTRY
    ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'Asia';
```