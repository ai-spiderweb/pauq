<table>
   <tr>
      <td><b>ID</b></td><td><b>Comment</b></td><td><b>Source quesion</b></td><td><b>Source query</b></td><td><b>Corrected quesion</b></td><td><b>Corrected query</b></td>
   </tr>
   <tr>
      <td>TO_7535</td><td>Common knowledge</td><td>which capitals are not major cities</td><td><code>SELECT t2.capital FROM state AS t2 JOIN city AS t1 ON t2.capital  =  t1.city_name WHERE t1.population  <=  150000</code></td><td>which capitals are not major <b>(less than 150 000 people)</b></td><td></td>
    </tr> 
    <tr>
      <td>TS_2263</td><td>Logical connection</td><td>What are the starting years shared by the technicians from the team "CLE" <b>or</b> "CWS"?</td><td><code>SELECT Starting_Year FROM technician WHERE Team  =  "CLE" <b>INTERSECT</b> SELECT Starting_Year FROM technician WHERE Team  =  "CWS"</code></td><td></td><td><code>SELECT Starting_Year FROM technician WHERE Team  =  "CLE" <b>UNION</b> SELECT Starting_Year FROM technician WHERE Team  =  "CWS"</code></td>
    </tr>  
     <tr>
      <td>TS_2530</td><td>Logical connection</td><td>What are the names of all reviewers that have given 3 <b>or</b> 4 stars for reviews?</td><td><code>SELECT T2.name FROM Rating AS T1 JOIN Reviewer AS T2 ON T1.rID  =  T2.rID WHERE T1.stars  =  3 <b>INTERSECT</b> SELECT T2.name FROM Rating AS T1 JOIN Reviewer AS T2 ON T1.rID  =  T2.rID WHERE T1.stars  =  4;</code></td><td></td><td><code>SELECT T2.name FROM Rating AS T1 JOIN Reviewer AS T2 ON T1.rID  =  T2.rID WHERE T1.stars  =  3 <b>UNION</b> SELECT T2.name FROM Rating AS T1 JOIN Reviewer AS T2 ON T1.rID  =  T2.rID WHERE T1.stars  =  4;</code></td>
    </tr> 
      <td>TS_2532</td><td>Logical connection</td><td>What are the names of all movies that received 3 <b>or</b> 4 stars?</td><td><code>SELECT T2.name FROM Rating AS T1 JOIN Reviewer AS T2 ON T1.rID  =  T2.rID WHERE T1.stars  =  3 <b>INTERSECT</b> SELECT T2.name FROM Rating AS T1 JOIN Reviewer AS T2 ON T1.rID  =  T2.rID WHERE T1.stars  =  4;</code></td><td></td><td><code>SELECT T2.name FROM Rating AS T1 JOIN Reviewer AS T2 ON T1.rID  =  T2.rID WHERE T1.stars  =  3 <b>UNION</b> SELECT T2.name FROM Rating AS T1 JOIN Reviewer AS T2 ON T1.rID  =  T2.rID WHERE T1.stars  =  4;</code></td> 
     </tr>
 
</table>
