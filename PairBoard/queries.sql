CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    active BOOLEAN NOT NULL,
    logged_in DATE NOT NULL
);

SELECT COUNT(*) FROM users;
SELECT COUNT(*) FROM users WHERE users.active = true;
SELECT COUNT(*) FROM users WHERE users.logged_in BETWEEN time_start AND time_end
