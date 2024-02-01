psql -h 172.31.88.18 -p 54321 -U postgres -d pubdb01
ALTER SYSTEM SET wal_level = logical;
docker-compose restart
CREATE TABLE tbl_a (c int primary key);
CREATE TABLE tbl_b (c int primary key);
INSERT INTO tbl_a SELECT generate_series(1,100);
INSERT INTO tbl_b SELECT generate_series(1,100);
CREATE PUBLICATION pub_a FOR TABLE tbl_a;
CREATE PUBLICATION pub_b FOR TABLE tbl_b;

\dRp
CREATE ROLE logi_repl_user LOGIN REPLICATION PASSWORD 'logi_repl_user';
GRANT SELECT ON tbl_a TO logi_repl_user;

psql -h 172.31.88.18 -p 54322 -U postgres -d subdb01
ALTER SYSTEM SET wal_level = logical;
docker-compose restart
CREATE TABLE tbl_a (c int primary key);
CREATE TABLE tbl_b (c int primary key);
CREATE SUBSCRIPTION sub_test CONNECTION 'host=172.31.88.18 port=54321 dbname=pubdb01 user=postgres password=postgres' PUBLICATION pub_a, pub_b;

\dRs