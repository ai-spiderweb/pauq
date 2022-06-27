<table>
   <tr>
      <td><b>ID</b></td><td><b>Comment</b></td><td><b>Source quesion</b></td><td><b>Source query</b></td><td><b>Corrected quesion</b></td><td><b>Corrected query</b></td>
   </tr>
   <tr>
      <td>TO_7535</td><td>Common knowledge</td><td>which capitals are not major cities</td><td>SELECT t2.capital FROM state AS t2 JOIN city AS t1 ON t2.capital  =  t1.city_name WHERE t1.population  <=  150000;</td><td>which capitals are not major <b>(less than 150 000 people)</b></td><td></td>
    </tr> 
    <tr>
      <td>TS_2263</td><td>What are the starting years shared by the technicians from the team "CLE" <b>or</b> "CWS"?</td><td>SELECT Starting_Year FROM technician WHERE Team  =  "CLE" <b>INTERSECT</b> SELECT Starting_Year FROM technician WHERE Team  =  "CWS";</td><td></td><td>SELECT Starting_Year FROM technician WHERE Team  =  "CLE" <b>UNION</b> SELECT Starting_Year FROM technician WHERE Team  =  "CWS";</td>
    </tr>  
     <tr>
      <td>ID</td><td>Comment</td><td>Source quesion</td><td>Source query</td><td>Corrected quesion</td><td>Corrected query</td>
    </tr> 
     <tr>
      <td>ID</td><td>Comment</td><td>Source quesion</td><td>Source query</td><td>Corrected quesion</td><td>Corrected query</td>
    </tr>  
     <tr>
      <td>ID</td><td>Comment</td><td>Source quesion</td><td>Source query</td><td>Corrected quesion</td><td>Corrected query</td>
    </tr>
    <tr>
      <td>ID</td><td>Comment</td><td>Source quesion</td><td>Source query</td><td>Corrected quesion</td><td>Corrected query</td>
    </tr>  
     <tr>
      <td>ID</td><td>Comment</td><td>Source quesion</td><td>Source query</td><td>Corrected quesion</td><td>Corrected query</td>
    </tr>  
  
</table>
