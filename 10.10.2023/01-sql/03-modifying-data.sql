UPDATE
    articles
SET 
    title = 'Halo'
WHERE
    id = 1;

UPDATE
    articles
SET 
    title = 'Halo',
    content = 'Worlds!!'
WHERE
    id = 2;

DELETE FROM
    articles
WHERE
    id = 10;

DELETE FROM
    articles
WHERE id IN (
    SELECT id FROM articles
    ORDER BY createAt
    LIMIT 2
    );
