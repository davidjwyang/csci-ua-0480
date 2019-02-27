-- 1)List all providers and their ssid's.
SELECT p.name, s.ssid
FROM providers p
INNER JOIN providers_ssids ps on ps.provider = p.name
INNER JOIN ssids s ON ps.ssid = s.ssid;

-- 2) List all the locations that AT&T has hotspots in.
SELECT DISTINCT l.lat, l.long
FROM hotspots h
FULL OUTER JOIN locations l ON l.lat = h.lat AND l.long = h.long
FULL OUTER JOIN providers p ON h.provider = p.name
WHERE p.name = 'AT&T';

-- 3) List the boro with the largest number of hot spots. 
SELECT b.name, count(*)
FROM hotspots h
INNER JOIN locations l ON l.lat = h.lat AND l.long = h.long 
INNER JOIN cities c on c.id = l.city_id
INNER JOIN boroughs b on b.name = c.boro
GROUP BY b.name;
