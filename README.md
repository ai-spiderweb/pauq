# pauq
PAUQ🕷️ = <b>P</b>ioneer d<b>A</b>taset for r<b>U</b>ssian text-to-S<b>Q</b>L. 

The Text-to-SQL dataset in Russian based on <a href="https://yale-lily.github.io/spider">Spider</a>. It contains three components that are modified, localized and enllarged: the NL questions, the SQL queries and the content of the databases. DB, table and column names remain unchanged; values are augmented by new Russian examples differ from existing ones. 

<img src="https://i.ibb.co/gw2qjhD/pauq.jpg">

## Data Content and Format
<a href="https://yale-lily.github.io/spider"><b>Spider dataset</b></a>

<a href="/dataset/pauq_train.json">PAUQ train set</a>: 8800 samples

<a href="/dataset/pauq_dev.json">PAUQ dev set</a>: 1076 samples

<a href="https://drive.google.com/file/d/1Xjbp207zfCaBxhPgt-STB_RxwNo2TIW2/view?usp=sharing">Databases</a>

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


### Citation
<a href="https://aclanthology.org/2022.findings-emnlp.175.pdf](https://aclanthology.org/2022.findings-emnlp.175.pdf">Paper link</a>

```
@inproceedings{bakshandaeva-etal-2022-pauq,
    title = "{PAUQ}: Text-to-{SQL} in {R}ussian",
    author = "Bakshandaeva, Daria  and
      Somov, Oleg  and
      Dmitrieva, Ekaterina  and
      Davydova, Vera  and
      Tutubalina, Elena",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2022",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-emnlp.175",
    pages = "2355--2376",
    abstract = "Semantic parsing is an important task that allows to democratize human-computer interaction. One of the most popular text-to-SQL datasets with complex and diverse natural language (NL) questions and SQL queries is Spider. We construct and complement a Spider dataset for Russian, thus creating the first publicly available text-to-SQL dataset for this language. While examining its components - NL questions, SQL queries and databases content - we identify limitations of the existing database structure, fill out missing values for tables and add new requests for underrepresented categories. We select thirty functional test sets with different features that can be used for the evaluation of neural models{'} abilities. To conduct the experiments, we adapt baseline architectures RAT-SQL and BRIDGE and provide in-depth query component analysis. On the target language, both models demonstrate strong results with monolingual training and improved accuracy in multilingual scenario. In this paper, we also study trade-offs between machine-translated and manually-created NL queries. At present, Russian text-to-SQL is lacking in datasets as well as trained models, and we view this work as an important step towards filling this gap.",
}
```

