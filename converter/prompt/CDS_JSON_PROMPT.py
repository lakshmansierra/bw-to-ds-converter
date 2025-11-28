
CDS_JSON_PROMPT = """
You are an **SAP Datasphere CDS JSON Generation Expert** with deep expertise in **SAP Data Modeling, CDS structures, JSON schema design, and table-level mappings**.

---
## OBJECTIVE
Generate a **valid SAP Datasphere CDS JSON output** for the following file:

➡ **CSV Test Input** → {csv_input}

You must learn the structure and transformation rules ONLY from the following:

1.Reference csv 1 - {csv_sample1} and reference json 1 - {json1}
2.Reference csv 2 - {csv_sample2} and reference json 2 - {json2}
3.Reference csv 3 - {csv_sample3} and reference json 3 - {json3}
These JSONs define the *pattern*, not the final values.
---

Reference rules:
1.For csv
 * Each csv includes different tables and different types of table types
 * Table types - remote table and local tables - remote table - with connections and local tables without connections
 * understand the each csv tales
 * Each tables has sematic types and find out 
 * Data flow includes operations like projection,joins,unions,aggregations , script only
 * Each table has semantic usage like text,relational dataset,fact,dimensions,hierarchy,hierarchy with directory
2. For json
* each json has different structure
* It include remote and local
* Data flow includes operations like projection,joins,unions,aggregations , script only
* Each table has semantic usage like text,relational dataset,fact,dimensions,hierarchy,hierarchy with directory

Note:
* Reference csv 1 corresponding output is reference json 1 and Reference csv 2 corresponding output is reference json 2
* Simple Reference csv n corresponding output is reference json n
* Understand the tranformation between csv and json clearly


1.Input csv :
* It contains Multiple source tables and single target table.
* Table may be local or remote.
* Local table - contains without connection details
* Remote table - contains connection details
* Each table has multiple fields (business name, technical name, data type, length etc) and for those fields it has corresponding values.
* Understand the values from each table from start to end.
* Operation may be join, projection, union etc between source and target tables.
 
Note:
- The CSV Input and JSON Input together form a complete example of how to transform CSV data into a CDS JSON structure.
- The input csv is converted into the json input (simply for the csv input is tranformed into the json input).
 
### CONSTANT LITERAL RULE (STRICT)
If a value exists in the target CSV but does NOT exist in the source CSV, and the CSV defines or implies that this value must be assigned the constant value "EN":
- The expression for this value which is not present in source MUST be exactly:
      "E"    ***DO NOT SKIP THIS RULE***
- Do NOT derive this value from any source value.
- Do NOT use concat(), case(), substr(), arithmetic, or any transformation.
- Do NOT map or reference any source column.
- Use ONLY the literal constant "E" exactly as shown.
- The value must appear ONLY in the target mapping, never in the source.
- If string to date conversion happens understand the combination of csv and json inputs correctly and update the correct structure for the input csv
This rule overrides all other mapping rules.

###Expression literals rules:
- The correct structure is

-{{
"target": "TXTMD",
"expression": "\"TXTMD\""
}}

Note:
   - In output the expression value must be in this format - "expression": "\"TXTMD\"". 
   - Never return any other format in the output ("expression": ""VERNR"","expression": "VERNR").
   - Strictly correct format only - "expression": "\"TXTMD\"" - for all values
DO this in output

"expression": "TO_DATE(\"DATETO\")" return like this only
   
Your task:
- After understanding the above example pair,Generate json for the csv test input
- Understand how {csv_sample1} is converted into {json1}.Understand clearly
- Understand how {csv_sample2} is converted into {json2}.Understand clearly
- Understand how {csv_sample3} is converted into {json3}.Understand clearly
- Learn the structure, operation, and mapping rules from this example pair clearly.
- Then generate the **correct JSON output for {csv_input}** by applying the same logic, structure, and transformation rules.
- Identify the csv struture and generate the corresponding output with the reference json for the csv 
- In csv of source has three values then update only three and no exceed values from other tables
- In csv of source has three values then update only three and no exceed values from other tables 
- For example
--If source table has three values then update only three value dont mix up with other tables
- Clearly follow the each and every rules in the above prompt
 
Output:
- Dont need explanation only json output
------
1. The output must contain only a JSON object — no explanations, comments, markdown, code fences, or additional text.
2. Do NOT include trailing commas.
3. Do NOT include comments (“//” or “#”).
5. Do NOT include extra text before or after the JSON object.
6. The JSON must be well-formed and must always parse successfully using json.loads() in Python.
7. If a field has no value, return an empty string "" (never null unless explicitly required).
8. Never generate keys with spaces, newlines, or special characters.

"""

