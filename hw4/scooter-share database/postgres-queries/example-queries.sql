-- 1.
select s.scooter_id, c.name, c.founded, st.model, st.weight, st.max_speed,
s.acquired_date, s.retired
from scooter as s 
inner join scooter_type as st on s.scooter_type_id = st.scooter_type_id
inner join company as c on st.company_id = c.company_id
limit 10; 

-- 2.
select retired, count(*) 
from scooter
group by retired; 

-- 3.
select to_char(acquired_date, 'YYYY-MM'), count(*) 
from scooter 
group by to_char(acquired_date, 'YYYY-MM');
having count(*) > 2

-- 4. 
select c.company_id, count(*)
from company as c
inner join scooter_type st on st.company_id = c.company_id
group by c.company_id

-- 5.
select scooter_type.model, agg.m
from scooter_type
inner join 
	(select scooter_type.company_id as c_id, max(scooter_type.max_speed) as m 
	from scooter_type 
	group by scooter_type.company_id) as agg
on scooter_type.max_speed = agg.m and scooter_type.company_id = agg.c_id 
inner join company as c on agg.c_id = c.company_id;

-- 6.
select c.name, count(*)
from company as c 
inner join scooter_type st on st.company_id = c.company_id
group by c.company_id 