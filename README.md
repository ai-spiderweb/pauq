# pauq
PAUQ🕷️ = <b>P</b>ioneer d<b>A</b>taset for r<b>U</b>ssian text-to-S<b>Q</b>L. 

The Text-to-SQL dataset in Russian based on <a href="https://yale-lily.github.io/spider">Spider</a>. It contains three components that are modified, localized and enllarged: the NL questions, the SQL queries and the content of the databases. DB, table and column names remain unchanged; values are augmented by new Russian examples differ from existing ones. 

<img src="https://i.ibb.co/gw2qjhD/pauq.jpg">

## Data Content and Format
<a href="https://yale-lily.github.io/spider"><b>Spider dataset</b></a>

<a href="/dataset/pauq_train.json">PAUQ train set</a>: 8800 samples

<a href="/dataset/pauq_dev.json">PAUQ dev set</a>: 1076 samples

<a href="https://drive.google.com/file/d/1NruQ7yW4NxL0HNQOLYDmssq_8JT5sy-a/view?usp=sharing">Databases</a>

If Spider data is loaded, it can be updated by this instructions:

1. Load the <a href="/dataset/update">"upload" folder</a>.
2. Launch <code>python converter.py --db_path=PATH-TO-DB-FOLDERS</code> (Python 3.5+).

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
