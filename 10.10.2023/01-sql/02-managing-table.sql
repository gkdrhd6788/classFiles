--테이블 생성
CREATE TABLE examples (
    ExamID INTEGER PRIMARY KEY AUTOINCREMENT,
    LastName varchar(50) NOT NULL,
    FirstName varchar(50) NOT NULL
    );

PRAGMA table_info('examples');

-- 새로운 필드 추가(교재와 달리 NOT NULL을 추가할거면 DEFAULT 추가 해줘야)
ALTER TABLE 
    examples 
ADD COLUMN 
    Country varchar(100) NOT NULL DEFAULT 'unknown';  

ALTER TABLE 
    examples 
ADD COLUMN 
    NickName varchar(100);

ALTER TABLE 
    examples 
ADD COLUMN 
    Age INTEGER NOT NULL DEFAULT 0;

ALTER TABLE 
    examples 
ADD COLUMN 
    Address VARCHAR(100) NOT NULL DEFAULT '';


-- 필드 이름 변경
ALTER TABLE
    examples
RENAME COLUMN
    Address to PostCode;
    
ALTER TABLE 
    examples
DROP COLUMN
    PostCode;

--Insert 
CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(200) NOT NULL,
    createAt DATE NOT NULL

);
INSERT INTO articles(id,title,content,createAt)
VALUES(7,'hello','world','2002-02-02');

INSERT INTO articles(title,content,createAt)
VALUES('hello','world','2002-02-02');

INSERT INTO articles(title,content,createAt)
VALUES
('title1','content1','2002-02-02'),
('title2','content2','2002-02-02');

INSERT INTO 
    articles(title,content,createAt)
VALUES
    ('mytitle','mycontent',DATE());

INSERT INTO articles(title,content,createAt)
VALUES
('title1','content1','1994-02-14'),
('title2','content2','2023-10-10');