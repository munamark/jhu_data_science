/* Qn.1*/
select e.emp_no as employee_number,last_name,first_name, sex,s.salary as employee_salary
from employees e join salaries s on e.emp_no = s.emp_no;

/*Qn.2*/
select first_name, last_name, hire_date from employees
where extract(year from hire_date) = 1986 order by hire_date;

/*Qn.3*/
select n.dept_no, d.dept_name, n.emp_no, e.last_name, e.first_name
from dept_manager n join departments d on n.dept_no = d.dept_no
join employees e on n.emp_no = e.emp_no;

/*Qn.4*/
select d.emp_no, e.last_name, e.first_name, s.dept_name
from employees e join dept_emp d on d.emp_no = e.emp_no
join departments s on s.dept_no = d.dept_no;

/*Qn.5*/
select first_name, last_name, sex from employees
where lower(first_name) = 'hercules' 
and last_name like 'B.%' /* i suspect you intended for this to be the "B" not "B." 
since i don't know which not taking any chances listing as required verbatim*/
;

/*Qn.6*/
select d.emp_no, e.last_name, e.first_name, s.dept_name
from employees e join dept_emp d on d.emp_no = e.emp_no
join departments s on s.dept_no = d.dept_no
where s.dept_name = 'Sales';

/*Qn.7*/
select d.emp_no, e.last_name, e.first_name, s.dept_name
from employees e join dept_emp d on d.emp_no = e.emp_no
join departments s on s.dept_no = d.dept_no
where s.dept_name in ('Sales','Development');


/*Qn.8*/
select distinct(last_name) as last_name, count(last_name) as last_name_count
from employees
group by last_name
order by last_name_count desc;

