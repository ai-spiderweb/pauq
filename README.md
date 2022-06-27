# pauq
PAUQ🕷️ = <b>P</b>ioneer d<b>A</b>taset for r<b>U</b>ssian text-to-S<b>Q</b>L. 

The Text-to-SQL dataset in Russian, based on <a href="https://yale-lily.github.io/spider">Spider</a>. All three components have been modified, localized and enllarged: the NL questions, the SQL queries and the content of the databases. 

<img src="https://i.ibb.co/gw2qjhD/pauq.jpg" width="600">

## Data Content and Format
<a href="/datasets/pauq_train.json">Train set</a>:  8800 samples
<a href="/datasets/pauq_dev.json">Dev set</a>: 1076 samples

- <code>id</code>

- <code>db_id</code> the database id to which this question is addressed

- <code>source</code>

- <code>type</code>

- <code>query</code> 

- <code>question</code> the natural language question

- <code>sql</code> parsed results of this SQL query using <a href="https://github.com/taoyds/spider/blob/master/process_sql.py">Spider parsing file</a>

- <code>question_toks</code> the natural language question tokens

- <code>query_toks</code> the SQL query tokens corresponding to the question

- <code>query_toks_no_values</code>

<code>
</code>
