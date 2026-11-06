# Query Boundary Lab

An offensive SQL injection experiment paired with its parameterized-query fix, entirely inside an in-memory SQLite database.

Python 3.11+ · Standard library only · MIT · Maintained by [ineedfoundmyway](https://github.com/ineedfoundmyway)

## Run the proof

```sh
python -m unittest -v
python main.py 
python scripts/prove.py
```

The checked-in [execution evidence](proof/report.json), [test transcript](proof/tests.txt), and [source hashes](proof/sha256.json) record a real local execution. Run the same commands to verify the result independently. CI regenerates evidence as an artifact on every push. Local results are not a claim that GitHub Actions has run.

## What you learn

1. Observe an authentication bypass against an intentionally vulnerable query.
2. Run exactly the same input against a query with bound parameters.
3. Inspect the regression tests for apostrophes, empty input and valid credentials.
4. Explain why escaping characters is a weaker design than separating data from SQL syntax.

The fixture stores a plaintext password only to isolate the query lesson. A real login also needs password hashing, rate limits, session protection and authorization. There is no web listener or arbitrary target option.

## Design and limits

This is original educational code inspired by the reading below. Article text, screenshots and third-party tool code are not bundled. Examples use synthetic data and temporary directories. No Internet targets are contacted. Results describe the supplied fixtures and do not certify a production system.

## Reading

- https://www.hackingarticles.in/beginner-guide-sql-injection-part-1/
- https://docs.python.org/3/library/sqlite3.html

## License

MIT. Third-party tools and articles retain their own licenses.
