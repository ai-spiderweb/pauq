# pauq
PAUQ🕷️ = <b>P</b>ioneer d<b>A</b>taset for r<b>U</b>ssian text-to-S<b>Q</b>L. 

The Text-to-SQL dataset in Russian based on <a href="https://yale-lily.github.io/spider">Spider</a>. It contains three components that are modified, localized and enllarged: the NL questions, the SQL queries and the content of the databases. DB, table and column names remain unchanged; values are augmented by new Russian examples differ from existing ones. 

<img src="https://i.ibb.co/gw2qjhD/pauq.jpg" width="600">

## Data Content and Format
<a href="/datasets/pauq_train.json">Train set</a>:  8800 samples

<a href="/datasets/pauq_dev.json">Dev set</a>: 1076 samples

**Structure:**

- <code>id</code> **[str]** </tt> primery key

- <code>db_id</code> **[str]** the database id to which this question is addressed

- <code>source</code> **[str]** "train-spider", "train-others", "dev" or "addition" (new samples, not from Spider)

- <code>type</code> **[str]** "train" or "dev"

- <code>query</code> **Dict[str, str]** SQL query (<code>en</code> English, <code>ru</code> Russian)

- <code>question</code> **Dict[str, str]** the natural language question (<code>en</code> English, <code>ru</code> Russian)

- <code>sql</code> **Dict[str, str]** parsed results of this SQL query using <a href="https://github.com/taoyds/spider/blob/master/process_sql.py">Spider parsing file</a> (<code>en</code> English, <code>ru</code> Russian)

- <code>question_toks</code> **Dict[str, str]** the natural language question tokens (<code>en</code> English, <code>ru</code> Russian)

- <code>query_toks</code> **Dict[str, str]** the SQL query tokens corresponding to the question (<code>en</code> English, <code>ru</code> Russian)

- <code>query_toks_no_values</code> **Dict[str, str]** the SQL query tokens, column values replaced by <VALUE>  (<code>en</code> English, <code>ru</code> Russian)
