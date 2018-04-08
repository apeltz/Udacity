
-- Limits the number of responses returned to 10
SELECT column_1, column_2, column_3
    FROM table_1
    ORDER BY column_2 DESC, column_1
    LIMIT 10;


-- Quiz: ORDER BY Part II
SELECT *
	FROM orders
    ORDER BY occurred_at DESC, total_amt_usd DESC
    LIMIT 5;
    
SELECT *
	FROM orders
    ORDER BY occurred_at DESC, total_amt_usd
    LIMIT 10;


SELECT *
    FROM orders
    WHERE gloss_amt_usd >= 1000
    LIMIT 5;

SELECT *
    FROM orders
    WHERE total_amt_usd < 500
    LIMIT 10;

SELECT name, website, primary_poc
	FROM accounts
    WHERE name = 'Exxon Mobil';

SELECT id,
	account_id,
    standard_amt_usd / standard_qty AS standard_unit_price
    FROM orders
    LIMIT 10;
    
SELECT id, account_id,
	poster_amt_usd / (poster_amt_usd + gloss_amt_usd + standard_amt_usd + 0.000001) AS pct_poster
    FROM orders;


-- % is wildcard for any character or any number of characters
SELECT *
	FROM accounts
    WHERE name LIKE 'C%';

SELECT *
	FROM accounts
    WHERE name LIKE '%one%';
    
SELECT *
	FROM accounts
    WHERE name LIKE '%s';

SELECT name, primary_poc, sales_rep_id
	FROM accounts
    WHERE name IN ('Walmart', 'Target', 'Nordstrom');
    
SELECT *
	FROM web_events
    WHERE channel IN ('organic', 'adwords');


-- Use NOT to exclude values based on queries
SELECT name, primary_poc, sales_rep_id
	FROM accounts
    WHERE name NOT IN ('Walmart', 'Target', 'Nordstrom');
    
SELECT *
	FROM web_events
    WHERE channel NOT IN ('organic', 'adwords');
    
SELECT *
	FROM accounts
    WHERE name NOT LIKE 'C%';
    
SELECT *
	FROM accounts
    WHERE name NOT LIKE '%one%';
    
SELECT *
	FROM accounts
    WHERE name NOT LIKE '%s';


SELECT *
	FROM orders
    WHERE standard_qty > 1000 AND poster_qty = 0 AND gloss_qty = 0;
    
SELECT *
	FROM accounts
    WHERE name NOT LIKE 'C%'
    AND name NOT LIKE '%s';
    
SELECT *
	FROM web_events
    WHERE channel IN ('organic', 'adwords')
    AND occurred_at BETWEEN '2016-01-01' AND '2017-01-01'
    ORDER BY occured_at DESC;

SELECT id
	FROM orders
    WHERE gloss_qty > 4000 OR poster_qty > 4000;
    
SELECT *
	FROM orders
    WHERE standard_qty = 0
    AND (gloss_qty > 1000 OR poster_qty > 1000);
    
SELECT name
	FROM accounts
    WHERE (name LIKE 'C%' OR name LIKE 'W%')
    AND (primary_poc LIKE '%ana%' OR primary_poc LIKE '%Ana%')
    AND primary_poc NOT LIKE '%eana%';