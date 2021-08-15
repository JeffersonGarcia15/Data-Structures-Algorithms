-- In a SQL db, you have two tables, an employees table and a departments table. 
-- Employees belong to only one department. Write a SQL query that, given a department name, 
-- finds all the employees in that department.

CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

INSERT INTO departments (name) VALUES("Physics");
INSERT INTO departments (name) VALUES("Mathematics");

INSERT INTO employees (name, department_id) VALUES ('Jefferson', 1);
INSERT INTO employees (name, department_id) VALUES ('Adilson', 1);
INSERT INTO employees (name, department_id) VALUES ('Lopez', 2);
INSERT INTO employees (name, department_id) VALUES ('Garcia', 1);


SELECT employees.name FROM employees INNER JOIN departments ON (employees.department_id = departments.id) WHERE departments.name = 'Physics'
