use test;
create table exam(
student_ID int(5) NOT NULL auto_increment,
exam_name varchar(20) NOT NULL,
grade int(5) NOT NULL ,
primary key (student_ID,exam_name));
create table student(
	student_ID int(5) NOT NULL,
	_name varchar(20) NOT NULL,
	sex char(1) NOT NULL,
	age int(3) NOT NULL,
    emotion_state varchar(20) NOT NULL,
    dept_name varchar(20) NOT NULL,
    FOREIGN key NO_1(student_ID) REFERENCES exam(student_ID),
    FOREIGN key NO_2(dept_name) REFERENCES department(dept_name),
    primary key (student_ID));
create table department(
dept_name varchar(20) NOT NULL,
building_budget int(8) NOT NULL,
primary key(dept_name));
alter table department add  budget int(8);
alter table department change  column building_budget building char(1);

    