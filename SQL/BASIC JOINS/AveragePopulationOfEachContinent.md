### Problem statement
>Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer.


## MYSQL
```sql
SELECT CO.CONTINENT, FLOOR(AVG(C.POPULATION))
FROM CITY C INNER JOIN COUNTRY CO
    ON C.COUNTRYCODE = CO.CODE
GROUP BY CO.CONTINENT;
```