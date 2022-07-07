-- script that lists all cities contained in the database hbtn_0d_usa
-- lists all cities
SELECT cities.id, cities.name, states.name
    FROM cities AS c
    JOIN states AS s
    WHERE c.state_id = s.id
    ORDER BY c.id;
